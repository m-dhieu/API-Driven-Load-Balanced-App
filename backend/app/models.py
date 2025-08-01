from sqlalchemy import Table, Column, Integer, String, Text, DateTime, func
from app.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String, unique=True, index=True, nullable=False),
    Column("password_hash", String, nullable=False),  # store SHA-256 hash
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
)

jobs = Table(
    "jobs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, index=True, nullable=False),
    Column("company", String, index=True),
    Column("location", String, index=True),
    Column("description", Text),
)
