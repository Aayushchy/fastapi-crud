import logging
import os
from logging.handlers import TimedRotatingFileHandler
import re

from colorlog import ColoredFormatter

log_dir = r"C:\Users\ThinkPad\Documents\Projects\conf\logs"
os.makedirs(log_dir, exist_ok=True)  # Create directory if it doesn't exist

log_file_path = os.path.join(log_dir, "app.log")

def setup_logger():
    # Creating a logger object
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.DEBUG)  # Lowest level to capture all logs

    # Log format
    log_format = "%(asctime)s.%(msecs)03d [%(threadName)s] %(levelname)-5s %(name)s - %(message)s"
    formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d:%H:%M:%S")

    color_formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s [%(threadName)s] %(name)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        reset=True,
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Level for console logs
    console_handler.setFormatter(color_formatter)

    # File handler (TimedRotatingFileHandler)
    file_handler = TimedRotatingFileHandler(
        filename=log_file_path,  # Base log file name
        when="midnight",  # Rotate at midnight
        interval=1,  # Rotate every day
        backupCount=0,  # Do not delete old files
        #Set size: maxBytes=5 * 1024 * 1024,
    )

    # Customize suffix to include date and time
    file_handler.suffix = "%Y-%m-%d_%H-%M-%S.log"

    # Update the regex for matching rotated files (required when modifying suffix)
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$")

    file_handler.setLevel(logging.INFO)  # Set level for file logs
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Initialize the logger
logger = setup_logger()

# Example usage
logger.info("This is an info message")