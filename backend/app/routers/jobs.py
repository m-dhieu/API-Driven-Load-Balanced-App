import logging
from fastapi import APIRouter, HTTPException, Query
from app.services.job_service import fetch_jobs

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/")
def get_jobs(limit: int = Query(20, ge=1, le=50), offset: int = Query(0, ge=0)):
    """
    Fetch jobs from external API with pagination.
    """
    try:
        jobs = fetch_jobs(limit, offset)
        return jobs
    except Exception as e:
        logger.error(f"Error fetching jobs: {e}")
        raise HTTPException(status_code=503, detail=f"Failed to fetch jobs from external API: {e}")

