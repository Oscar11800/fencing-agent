
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fencing_agent.core.dependencies import get_db
from fencing_agent.core.prompts import WELCOME_MESSAGE
from fencing_agent.db.repositories import create_session
from fencing_agent.schemas.sessions import SessionResponse

# api/v1/sessions.py
router = APIRouter(prefix="/api/v1")

@router.post("/sessions")
async def sessions(db: AsyncSession = Depends(get_db)):
    response = await create_session(db)
    return SessionResponse(session_id=str(response.id), welcome_message=WELCOME_MESSAGE)
