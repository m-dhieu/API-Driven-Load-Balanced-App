from fastapi import APIRouter
from app.models import jobs
from app.database import database
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class Job(BaseModel):
    id: int
    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None

@router.get("/", response_model=List[Job])
async def get_jobs():
    query = jobs.select()
    results = await database.fetch_all(query)
    return results

