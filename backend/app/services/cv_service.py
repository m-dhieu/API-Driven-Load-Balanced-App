import os
import requests

# Constants for RapidAPI Resume Parser
RAPIDAPI_HOST = "resumeparser.p.rapidapi.com"  # Note correct host from official API
RAPIDAPI_URL = f"https://{RAPIDAPI_HOST}/api/resume"
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

if not RAPIDAPI_KEY:
    raise RuntimeError("Missing RAPIDAPI_KEY environment variable. Please set it before running.")

def parse_resume(file_content: bytes, filename: str) -> dict:
    """
    Sends the resume file to the RapidAPI Resume Parser and Analyzer API.
    Returns the parsed JSON response.
    """
    files = {
        "resume": (filename, file_content),
    }

    headers = {
        "X-RapidAPI-Host": RAPIDAPI_HOST,
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }

    try:
        response = requests.post(RAPIDAPI_URL, headers=headers, files=files, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Log or re-raise with clearer message
        raise RuntimeError(f"Failed to parse resume via RapidAPI: {e}")
