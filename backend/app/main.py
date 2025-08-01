import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import jobs, cv_review, grammar_check, resources, auth
from app.database import engine, metadata, database

logging.basicConfig(level=logging.INFO)

# Load .env file for env variables like RAPIDAPI_KEY
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Job Tracker API")

# Create all tables
metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
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
