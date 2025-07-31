from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.services.cv_service import parse_resume

router = APIRouter()

@router.post("/", status_code=status.HTTP_200_OK)
async def review_cv(file: UploadFile = File(...)):
    """
    Endpoint to accept resume upload and return parsed info from RapidAPI.
    """

    ALLOWED_TYPES = [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain"
    ]

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type. Allowed types: PDF, DOC, DOCX, TXT.")

    try:
        contents = await file.read()
        parsed_data = parse_resume(contents, file.filename)
        return parsed_data
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
