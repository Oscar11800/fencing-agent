import uuid 
from sqlalchemy.ext.asyncio import AsyncSession
from fencing_agent.db.repositories import get_history, save_message
from fencing_agent.clients.openai import get_chat_response
from fencing_agent.core.prompts import SYSTEM_PROMPT

# TODO: Add limit to history being sent, history context compactor after reaching a certain limit
async def handle_message(db: AsyncSession, session_id: uuid.UUID, user_message: str) -> str:
    history = await get_history(db, session_id)
    # build the prompt
    # start with the system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # supply history
    for msg in history:
        messages.append({"role": msg.role, "content": msg.content})
    
    # current user msg
    messages.append({"role": "user", "content": user_message})
    
    # call OAI API
    response = await get_chat_response(messages)

    await save_message(db, session_id, "user", user_message)
    await save_message(db, session_id, "assistant", response)
    return response
