from fastapi import FastAPI
from app.routes import tasks
from app.database import engine, Base

app = FastAPI(title="Task Manager API")

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
