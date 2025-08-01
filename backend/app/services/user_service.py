import hashlib
from app.database import database
from app.models import users
from sqlalchemy import select, insert
from sqlalchemy.exc import IntegrityError

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password_hash: str, provided_password: str) -> bool:
    return stored_password_hash == hash_password(provided_password)

async def signup(username: str, password: str) -> bool:
    query = insert(users).values(
        username=username,
        password_hash=hash_password(password)
    )
    try:
        await database.execute(query)
        return True
    except IntegrityError:
        # If username already exists
        return False

async def login(username: str, password: str):
    query = select(users).where(users.c.username == username)
    user = await database.fetch_one(query)
    if user and verify_password(user.password_hash, password):
        return {"id": user.id, "username": user.username}
    return None
