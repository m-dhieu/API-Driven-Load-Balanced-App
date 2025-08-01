from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.user_service import signup, login

router = APIRouter()

class SignupRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/signup")
async def api_signup(request: SignupRequest):
    success = await signup(request.username, request.password)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"message": "Signup successful"}

@router.post("/login")
async def api_login(request: LoginRequest):
    user = await login(request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"user_id": user["id"], "username": user["username"]}
