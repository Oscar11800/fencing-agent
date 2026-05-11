import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fencing_agent.core.dependencies import get_db
from fencing_agent.core.prompts import WELCOME_MESSAGE
from fencing_agent.db.repositories import create_session, get_history
from fencing_agent.schemas.sessions import SessionResponse
from fencing_agent.schemas.sessions import MessageResponse, HistoryResponse

# api/v1/sessions.py
router = APIRouter(prefix="/api/v1")

@router.post("/sessions")
async def sessions(db: AsyncSession = Depends(get_db)):
    response = await create_session(db)
    return SessionResponse(session_id=str(response.id), welcome_message=WELCOME_MESSAGE)

@router.get("/sessions/{session_id}/history")
async def history(session_id: str, db: AsyncSession = Depends(get_db)):
    messages = await get_history(db, uuid.UUID(session_id))
    
