from fastapi import APIRouter 
from fencing_agent.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/v1")

@router.post("/chat")
async def chat(chat_request: ChatRequest):
    return ChatResponse(
        session_id=chat_request.session_id, 
        response="I'm the fencing agent. I'm not connected to anything yet"
    )

