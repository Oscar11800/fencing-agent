from contextlib import asynccontextmanager

from fastapi import FastAPI

from fencing_agent.api.v1.chat import router as chat_router
from fencing_agent.api.v1.sessions import router as sessions_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title = "Fencing Agent", lifespan=lifespan)
app.include_router(chat_router)
app.include_router(sessions_router)

@app.get("/health")
async def health():
    return{"status": "ok"}
