from fastapi import FastAPI
from contextlib import asynccontextmanager
from fencing_agent.api.v1.chat import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title = "Fencing Agent", lifespan=lifespan)
app.include_router(router)

@app.get("/health")
async def health():
    return{"status": "ok"}
