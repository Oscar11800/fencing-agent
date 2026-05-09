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
## session
| Column    | Type     | Notes                              | 
|-----------------------------------------------------------|
| id        | UUID     | PK generated serverside for API    |
| created_at| TIMESTAMP| When session starts                |
| updated_at| TIMESTAMP| Last activity, update on every msg |
| status    | VARCHAR  | "active", "escalated", "closed"    |
| metadata  | JSONB    | optional JSON                      |

## messages
| Column     | Type     | Notes                                   | 
|-----------------------------------------------------------------|
| id         | UUID     | PK                                      |
| session_id | UUID     | FK -> sessions.id                       |
| role       | VARCHAR  | "user" or "assistant"                   |
| content    | TEXT     | Message text                            |
| created_at | TIMESTAMP| When session starts                     |
| flagged    | BOOLEAN  | was this msg flagged by guardrails      |
| flag_reason| VARCHAR  | "prompt_injection", "abuse", "off_topic"|

## documents
| Column     | Type        | Notes                                               | 
|--------------------------------------------------------------------------------|
| id         | UUID        | PK                                                  |
| source_file| UUID        | Which md file did this come from                    |
| chunk_index| INTEGER     | Position of chunk in source file                    |
| content    | TEXT        | Text chunk                                          |
| embedding  | VECTOR(1536)| Vector embedding, 1536 for OAI output, pgvector use |
| created_at | TIMESTAMP   | When embedding was (for staleness)                  |

## flagged_events
| Column     | Type     | Notes                                              | 
|----------------------------------------------------------------------------|
| id         | UUID     | PK                                                 |
| session_id | UUID     | FK -> sessions.id                                  |
| message_id | UUID     | FK -> messages.id, which msg flagged               |
| event_type | VARCHAR  | "prompt_injection", "abuse", "repeat", "escalation"|
| created_at | TIMESTAMP| When session starts                                |
| details    | TEXT     | Description of what happened                       |
| created_at | TIMESTAMP| When session starts                                |

### Relationships
    - one session -> many messages 
    - one session -> many flagged_events 
    - one message -> many flagged_events 

We decide on separate flagged_events table for rich content on flagged event logging and the flagged boolean is mainly for message filtering. Messages can have many flagged_events in case they trigger multiple in a single message. 

# Classes & Modules 

# RAG Pipeline

# Prompt Design

# Guardrails Implementation

# Session Management 

# API Contracts 

# Error Handling

# Config and Env 
