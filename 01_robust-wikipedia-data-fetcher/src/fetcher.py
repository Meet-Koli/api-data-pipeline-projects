# Will:

# Build a Wikipedia API URL
# Call the API
# Handle errors (timeouts, 404, etc.)
# Retry if needed
# Return JSON data
# Fail cleanly if everything breaks

import requests
import time
from typing import Dict,Any
from logger import logger

# requests	    Makes HTTP API calls
# time	        Used for retry delays
# Dict, Any 	Type hints for return value
# logger	    Logs events & errors


# API base URL
WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

# Configuration settings
MAX_RETRIES = 3          # Number of retry attempts for failed requests
RETRY_DELAY = 2         # Delay (in seconds) between retries
TIMEOUT = 5             # Timeout (in seconds) for API requests

def fetch_article(title: str) -> Dict[str, Any]:
    """
    Fetches a Wikipedia article summary by title.
    
    Args:
        title (str): The title of the Wikipedia article to fetch.
        
    Returns:
        Dict[str, Any]: The JSON response from the Wikipedia API.
        
    Raises:
        Exception: If the article cannot be fetched after retries.
    """
    url = WIKI_API_URL + title.replace(" ", "%20")  # Why %20: Spaces in URLs must be encoded as %20
    # Difference betn _ and %20: _ is a character, %20 is URL encoding for spaces

    for attempts in range(1, MAX_RETRIES + 1):
        # This loop will run 4 times if MAX_RETRIES is 3 (1 initial + 3 retries)

        try:
            logger.info(f"Fetching article: {title} (Attempt {attempts})")

            HEADERS = { "User-Agent": "WikiDataFetcher/1.0 (contact: meet@example.com)"}

            response = requests.get(url,headers=HEADERS, timeout=TIMEOUT)

            if response.status_code == 200:
                logger.info(f"Successfully fetched article: {title}")
                return response.json()
            
            elif response.status_code == 404:
                logger.warning(f"Article not found: {title} (404)")
                return {} # Return empty dict for not found

            else:
                logger.warning(
                    f"Unexpected status {response.status_code} for {title}"
                )

        except requests.exceptions.Timeout:   
            logger.error(f"Timeout while fetching article: {title}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error for article {title}: {e}") # Log any other request exceptions

        # If we reach here, it means the request failed
        if attempts < MAX_RETRIES:
            logger.info(f"Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
            # it will again start the for loop for next attempt

    # If we exhaust all retries
    logger.critical(f"Failed to fetch article after {MAX_RETRIES} attempts: {title}")
    raise Exception(f"Could not fetch article: {title}")  
      