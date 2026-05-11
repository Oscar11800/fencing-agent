from pydantic import BaseModel


class SessionResponse(BaseModel):
    session_id: str 
    welcome_message: str
