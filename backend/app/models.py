from sqlalchemy import Table, Column, Integer, String, Text
from .database import metadata

jobs = Table(
    "jobs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, index=True, nullable=False),
    Column("company", String, index=True),
    Column("location", String, index=True),
    Column("description", Text),
)
