from fastapi import APIRouter
from app.models import jobs
from app.database import database
from pydantic import BaseModel

router = APIRouter()

class Job(BaseModel):
    id: int
    title: str
    company: str | None = None
    location: str | None = None
    description: str | None = None

@router.get("/", response_model=list[Job])
async def get_jobs():
    query = jobs.select()
    results = await database.fetch_all(query)
    return results
