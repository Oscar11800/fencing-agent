# Project Structure 
## Layers
    1. API Layer: handles http 
    2. Service Layer: business logic, RAG, guardrails
    3. Data Layer: communicates with DB and OAI API 
    4. Models Layer: defines db schema and models
## Structure 
fencing-agent/
    - docs/
        - architecture.md 
        - prd.md 
        - technical_design.md 
    - knowledge_base/
        - info.md
        - instructions.md 
        - system_prompt.md 
        - rules.md 
        - website.html
        - (more to come, think on this later)
    - src/ 
        - fencing_agent/
            - \_\_init\_\_.py 
            - main.py (create FastAPI app, register routes)
        - api/ (API layer)
            - \_\_init\_\_.py 
            - v1/ 
                - \_\_init\_\_.py 
                - chat.py (/chat, /history)
                - sessions.py (/session)
        - schemas/ (requests/responses shapes)
            - \_\_init\_\_.py 
            - chat.py (ChatRequest, ChatResponse)
            - sessions.py (SessionCreate, SessionResponse)
        - services/ (business logic)
            - \_\_init\_\_.py 
            - agent.py (prompt, LLM call, turn orchestration)
            - guardrails.py (I/O validation)
            - knowledge.py (RAG)
            - session.py    (session)
        - db/  (data)
            - \_\_init\_\_.py 
            - engine.py (SQLAlchemy engine)
            - models.py (ORM models) 
            - repositories.py (DB queries) 
        - core/ (shared)
            - \_\_init\_\_.py 
            - config.py (pydantic settings)
            - dependencies.py (FastAPI)
            - prompts.py (system prompt templates)
        - clients/ (external api wrappers)
            - \_\_init\_\_.py 
            - openai.py (OAI call wrapper)
    - tests/
        - \_\_init\_\_.py 
        - api/ 
        - services/ 
        - db/ 
    - alembic/ 
        - env.py 
        - versions/
    - alembic.ini 
    - .env.example 
    - .env 
    - .gitignore 
    - pyproject.toml (dependencies + metadata)
    - README.md

# Database Schema 

# Classes & Modules 

# RAG Pipeline

# Prompt Design

# Guardrails Implementation

# Session Management 

# API Contracts 

# Error Handling

# Config and Env 
