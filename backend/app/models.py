from sqlalchemy import Table, Column, Integer, String, Text
from app.database import engine, metadata, database

jobs = Table(
    "jobs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, index=True, nullable=False),
    Column("company", String, index=True),
    Column("location", String, index=True),
    Column("description", Text),
)
