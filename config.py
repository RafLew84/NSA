# -*- coding: utf-8 -*-
"""
config for the project

@author
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import logging

class LevelFormatter(logging.Formatter):
    def __init__(self, formats, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formats = formats

    def format(self, record):
        # Set the format for this record's level
        log_fmt = self.formats.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def setup_logging():
    # Define log formats for each level
    formats = {
        logging.DEBUG: '%(asctime)s - %(name)s - DEBUG - %(message)s',
        logging.INFO: '%(asctime)s - %(name)s - INFO - %(message)s',
        logging.WARNING: '%(asctime)s - %(name)s - WARNING - %(message)s',
        logging.ERROR: '%(asctime)s - %(name)s - ERROR - %(message)s',
        logging.CRITICAL: '%(asctime)s - %(name)s - CRITICAL - %(message)s',
    }

    # Create a single handler
    handler = logging.FileHandler('logger.log')
    handler.setLevel(logging.DEBUG)  # Capture all levels

    # Create and set a LevelFormatter
    formatter = LevelFormatter(formats)
    handler.setFormatter(formatter)

    # Get the root logger and add handler to it
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the base logger level to debug
    logger.addHandler(handler)

# Example usage:
setup_logging()

# Log some messages for testing
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")