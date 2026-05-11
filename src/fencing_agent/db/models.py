import uuid 
from datetime import datetime 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, Text, String
from pgvector.sqlalchemy import Vector
from typing import Optional

class Base(DeclarativeBase):
    pass

class Session(Base):
    __tablename__ = "sessions"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    status: Mapped[str] = mapped_column(default="active") 

class Message(Base):
    __tablename__ = "messages"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    session_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("sessions.id"))
    role: Mapped[str]
    content: Mapped[str] = mapped_column(Text)
created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    flagged: Mapped[bool] = mapped_column(default=False)
    flag_reason: Mapped[Optional[str]] = mapped_column(default=None) 

class Document(Base):
    __tablename__ = "documents"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    source_file: Mapped[str]
    chunk_index: Mapped[int]
    content: Mapped[str] = mapped_column(Text)
    embedding = mapped_column(Vector(1536))
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    
