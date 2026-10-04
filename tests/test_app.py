from fastapi.testclient import TestClient
from conversation_service.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_conversation_response_contains_conversation_id():
    response = client.post("/conversation", json={
        "conversation_id": "abc",
        "messages": [{"role": "user", "content": "hello"}]
    })
    assert response.status_code == 200
    assert response.json()["conversation_id"] == "abc"
