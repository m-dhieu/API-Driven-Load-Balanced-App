import logging
from fastapi import FastAPI
from app.routers import jobs, cv_review, grammar_check, resources
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, metadata

metadata.create_all(engine)


logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Job Tracker API")

app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])
app.include_router(cv_review.router, prefix="/api/cv-review", tags=["cv-review"])
app.include_router(grammar_check.router, prefix="/api/grammar-check", tags=["grammar-check"])
app.include_router(resources.router, prefix="/api/resources", tags=["resources"])

origins = [
    "http://localhost",  # adjust to your frontend host if needed
    "http://localhost:3000",
    # Add production/deploy frontend URLs here as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

