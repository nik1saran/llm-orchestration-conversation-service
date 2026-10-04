# LLM Orchestration and Conversation Service

A FastAPI reference backend for stateful LLM conversations, orchestration, latency controls, and Kubernetes-ready deployment.

## Features

- Typed request and response contracts.
- Clear separation between API, orchestration, validation, and observability layers.
- Local development workflow with tests.
- Container and CI scaffolding for GitHub.

## Quick start

`ash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
pytest
uvicorn conversation_service.main:app --reload
`

## Repository map

| Path | Purpose |
| --- | --- |
| src/conversation_service/ | Application package. |
| 	ests/ | Unit tests for core behavior. |
| docs/architecture.md | Design notes and production considerations. |
| Dockerfile | Container image for deployment. |
| .github/workflows/ci.yml | Python CI workflow. |

## Design goals

- Keep conversation state explicit.
- Make model orchestration replaceable.
- Return trace metadata for supportability.
- Prepare the service for burst traffic through stateless API workers and externalized storage.
