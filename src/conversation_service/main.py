from datetime import datetime, timezone
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="LLM Orchestration and Conversation Service", version="0.1.0")

class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)

class ConversationRequest(BaseModel):
    conversation_id: str = Field(min_length=1)
    messages: list[Message]
    max_tokens: int = Field(default=512, ge=1, le=4096)

class ConversationResponse(BaseModel):
    conversation_id: str
    response: str
    trace_id: str
    created_at: datetime

def build_response(request: ConversationRequest) -> ConversationResponse:
    latest_user_message = next((m.content for m in reversed(request.messages) if m.role == "user"), "")
    response = f"Received request for conversation {request.conversation_id}: {latest_user_message[:160]}"
    return ConversationResponse(
        conversation_id=request.conversation_id,
        response=response,
        trace_id=f"trace-{request.conversation_id}",
        created_at=datetime.now(timezone.utc),
    )

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/conversation", response_model=ConversationResponse)
def conversation(request: ConversationRequest) -> ConversationResponse:
    return build_response(request)
