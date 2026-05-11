from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str 
    message: str 

class ChatResponse(BaseModel):
    session_id: str 
    response: str

class MessageResponse(BaseModel):
    role: str
    content:str
    created_at: str

class HistoryResponse(BaseModel):
    session_id: str
    messages: list[MessageResponse]
