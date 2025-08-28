import json
import os
import logging

logger = logging.getLogger(__name__)

def load_json_data(file_path: str):
    """
    Load JSON data from a file
    Args:
        file_path (str): The path to the JSON file.
    Returns:
        dict: The JSON data as a dictionary."""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        logger.error(f"The file {file_path} does not exist.")
    except Exception as e:
        logger.error(f"An error occurred while loading JSON data: {e}", exc_info=True)
