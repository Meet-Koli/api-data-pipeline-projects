# Each log has a severity level:

# Level   	When to Use
# DEBUG	    Detailed info for developers
# INFO	    Normal program flow
# WARNING	Something odd but not broken
# ERROR	    Something failed
# CRITICAL	System is broken

# This tells you:
# When it happened
# What happened
# How serious it was
# Very useful for debugging.


import logging
from pathlib import Path
from datetime import datetime

# It will create logs directory if it doesn't exist
LOG_DIR=Path("logs")  #path object for logs directory
LOG_DIR.mkdir(exist_ok=True)  #create logs directory if not exists

#Daily log file name
log_file=LOG_DIR / f"Wiki_fetcher_{datetime.now().strftime('%Y-%m-%d')}.log"

# Configure logging settings, it will write logs to the file
logging.basicConfig(
    level=logging.INFO,  # Capture all levels INFO and above
    # Why this level is chosen: INFO is a good default for general application logging. It captures important runtime events without the verbosity of DEBUG.
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",    
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]

    # Log format: timestamp, level, logger name, message    
    # You can adjust level to DEBUG for more detailed logs
    # You can add more handlers (e.g., email, HTTP) as needed
    # In simple words handlers define where the logs go (file, console, etc.
    # logging.FileHandler(log_file, encoding="utf-8"), means logs will be written to the specified log file with utf-8 encoding
    # logging.StreamHandler() means logs will also be printed to the console


)

# # Create a logger instance
logger=logging.getLogger("wiki_fetcher_logger") # it is good practice to name your logger because there can be multiple loggers in a large application

# # This lets the file run standalone for testing.
# if __name__ == "__main__":    
#     logger.info("Logger test: INFO message")
#     logger.warning("Logger test: WARNING message")
#     logger.error("Logger test: ERROR message")
#     logger.critical("Logger test: CRITICAL message")

