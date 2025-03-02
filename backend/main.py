from config import AppSettings
from contextlib import asynccontextmanager
from database import ensure_database_created, get_context_session
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pipelines import VirginiaLandmarkPipeline
from routers import virginia_router
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = AppSettings()
    ensure_database_created()
    with get_context_session() as session:
        VirginiaLandmarkPipeline().injest(settings=settings, db=session)
    yield


app = FastAPI(
    title="mapvis-api",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)


#include routers
app.include_router(virginia_router, prefix="/api")


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, port=5000)