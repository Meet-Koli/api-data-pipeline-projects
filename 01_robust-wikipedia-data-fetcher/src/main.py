# It only:

# Takes user input
# Calls fetch_article()
# Validates with WikiArticle
# Saves clean JSON
# Logs the process

import json
from pathlib import Path

from fetcher import fetch_article
from model import WikiArticle
from logger import logger


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "result.json"


def run_pipeline(query: str) -> None:
    """
    Runs the Wikipedia data pipeline:
    1. Fetches raw data from API
    2. Validates using Pydantic
    3. Saves clean JSON output
    """

    logger.info(f"Pipeline started for query: {query}")

    raw_data = fetch_article(query)

    if not raw_data:
        logger.warning("No data received from API. Exiting pipeline.")
        return

    try:
        article = WikiArticle(
            title=raw_data.get("title"),
            summary=raw_data.get("extract"),
            url=raw_data.get("content_urls", {})
               .get("desktop", {})
               .get("page"),
        )

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(article.model_dump(mode="json"), f, indent=2, ensure_ascii=False)

        logger.info(f"Article saved successfully: {article.title}")

    except Exception as e:
        logger.exception(f"Data validation or saving failed: {e}")


if __name__ == "__main__":
    user_query = input("Enter a Wikipedia search term: ")
    run_pipeline(user_query)
