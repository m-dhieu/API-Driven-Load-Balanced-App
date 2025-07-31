from fastapi import APIRouter, Query, HTTPException
from app.services.resource_service import fetch_resources

router = APIRouter()

@router.get("/")
def get_resources(skill: str = Query(..., min_length=2)):
    """
    Returns learning resources based on the requested skill.
    """
    try:
        resources = fetch_resources(skill)
        return resources
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch resources: {str(e)}")

