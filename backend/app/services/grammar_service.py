import requests

def check_grammar(text: str) -> dict:
    """
    Calls the free LanguageTool API to check grammar.
    """
    endpoint = "https://api.languagetool.org/v2/check"
    params = {
        "text": text,
        "language": "en-US",
    }
    
    try:
        response = requests.post(endpoint, data=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Raise an exception to be caught by the FastAPI route
        raise RuntimeError(f"LanguageTool API request failed: {e}")

