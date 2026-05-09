# About this document
This architecture document outlines the technical architecture and the goals of the architecture for the fencing agent.

# Goals 
Properties:
- The agent must be free to maintain (assume that model costs are 0) using cheap models and cheap providers, this must be a near 0 cost agent 
- The agent must be easy to maintain for a barely-technical web maintainer who will update the knowledge base and SoT of the agent and push that to github. 
- The agent should be able to provide and field both voice and text and answer based off the knowledge base 
- The agent data must be able to be stored cheaply/near free (or with hobby/free accounts), minimizing third party dependencies 
- The agent is text-first,  voice will come on later iterations 
- The agent must be maintainable by a single non-technical person 
- The agent must be able to be embedded on a static HTML page hosted by UChicago

# Out-of-scope Goals
    - The agent is not a mult-agent system
    - It does not use custom models or LLMs
    - It does not optimize for scale
    - It does not over-optimize for performance, safety, or quality over cost and simplicity 
    - It does not use real-time streaming or expensive features 

# System Overview
## Chat Widget (Browser)
Custom TS widget embedded via <script> tag on static HTML site 
## FastAPI Server
Core backend logic handler 
    - Routes handlers to API endpoints
    - Agent logic: prompt construction, input validation, output guardrails 
    - session manager 
    - knowledge base rag loader 
    - logging service 
## External Dependencies 
OAI API for LLM and voice models 
## Database
PostgreSQL (conversation + logging ) + pgvector (vector embeddings) + alembic + sqlalchemy
## Deployment
Railway 


# Data Flow
    1. (For now, we will only describe the text flow) User types a message into the chat widget 
    2. Widget sends POST requst to the /chat endpoint with the message and session information (id) 
    3. The FastAPI server will look up/create the session
    4a. Input validation: the server checks the user message for signs of abuse
    4b. The server flags/logs inappropriate messages and gives canned response, other wise continue with steps 
    4c. The server querys pgvesctor for relevant docs
    5. The server will construct a prompt including the message history retrieved from memory, knowledge context, guardrails, and system prompt 
    6. The server sends prompt to OpenAI API 
    7. OpenAI API returns response 
    8. Server applies guardrails, checking on appropriateness of response before outputting 
    9. Server logs the exchange with the DB
    10. Server returns response to the widget 

# Key Design Decisions
    - Knowledge base: RAG with vector DB (likely pgvector) for learning purposes as I need to understand how to use, query, etc. with vector DB and how RAG works, cons of this is more complicated for a small PoC agent.  
    - Conversation memory: postgresql database, free and good practice, also provides active session state 
    - Logging: Postgresql database, used in conjunction with conversation, using pgvector as above, sqlalchemy for the python interface, and alembic to handle migrations
    - LLM provider: OAI for solid voice and text APIs 
    - Hosting: PaaS like railway for cheap/free hosting and takes care of postgresql and simplifies deployment 
    - Frontend widget: custom frontend widget in TS with a <script> tag, minimize the scale of this widget for scoping

# API Design 
    - POST /chat: receive user message, returns agent's response 
        - request body: `{session_id "abc123", message: "what's the practice schedule?"}`
        - response body: `{session_id: "abc123", response: "Practices are..." , "links: """}`
    - POST /session: create a new session on chat opening, returns a session ID 
        - request body: `{}`
        - response body: `{session_id: "abc123", welcome_message "Hi!..."}`
    - GET /history: returns conversation history for a session (reloading session) 
        - response body: `{messages: [{role: "user", content: "..."}, {role: "agent", content: "..."}]}`
    - POST /voice: voice input output endpoint (later scoping)
# Questions to consider 
- what models to use from OAI?
- What will the actual api design look like? 
- what will the actual db schema design look like?
- how will we eventually integrate voice 
- how to make this modular for eventual scaling/changes? 
