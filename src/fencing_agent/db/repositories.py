import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fencing_agent.db.models import Message, Session


async def create_session(db: AsyncSession) -> Session: 
    new_session = Session(id=uuid.uuid4(), status="active")
    db.add(new_session)
    # commit after api call ends
    return new_session

async def save_message(
        db: AsyncSession,
        session_id: uuid.UUID,
        role: str,
        content: str
) -> Message:
    new_message = Message(
        id=uuid.uuid4(),
        session_id=session_id,
        role=role, content=content
    )
    db.add(new_message)
    # commit in dependencies, after api call ends
    return new_message

async def get_history(db: AsyncSession, session_id: uuid.UUID) -> list[Message]:
    results = await db.execute(
        select(Message)
        .where(Message.session_id == session_id)
        .order_by(Message.created_at)
    )
    messages = results.scalars().all()
    return messages
