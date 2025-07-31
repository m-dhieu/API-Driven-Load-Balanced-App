import requests

def fetch_jobs(limit: int, offset: int):
    """
    Call the external Himalayas jobs API to fetch job listings with error handling and timeout.
    """
    url = f"https://himalayas.app/jobs/api?limit={limit}&offset={offset}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Raise a RuntimeError with details for the caller to catch and log
        raise RuntimeError(f"Himalayas job API request failed: {e}")

