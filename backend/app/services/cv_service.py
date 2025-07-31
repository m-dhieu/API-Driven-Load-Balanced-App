import os
import requests

RAPIDAPI_HOST = "resumeparser.p.rapidapi.com"
RAPIDAPI_URL = f"https://{RAPIDAPI_HOST}/api/resume"
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

if not RAPIDAPI_KEY:
    raise RuntimeError("Missing RAPIDAPI_KEY env variable. Please set it in your environment.")

def parse_resume(file_content: bytes, filename: str) -> dict:
    files = {
        "resume": (filename, file_content),
    }
    headers = {
        "X-RapidAPI-Host": RAPIDAPI_HOST,
        "X-RapidAPI-Key": RAPIDAPI_KEY,
    }
    try:
        response = requests.post(RAPIDAPI_URL, headers=headers, files=files, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to parse resume via RapidAPI: {e}")
