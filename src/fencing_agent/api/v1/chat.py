import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fencing_agent.core.dependencies import get_db
from fencing_agent.schemas.chat import ChatRequest, ChatResponse
from fencing_agent.services.agent import handle_message


# api/v1/chat.py
router = APIRouter(prefix="/api/v1")

@router.post("/chat")
async def chat(chat_request: ChatRequest, db: AsyncSession = Depends(get_db)):
    response = await handle_message(
        db,
        uuid.UUID(chat_request.session_id),
        chat_request.message
    )
    return ChatResponse(
        session_id=chat_request.session_id, 
        response=response    
    )
