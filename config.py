# -*- coding: utf-8 -*-
"""
Configuration and setup for logging in the project.

This module sets up logging with different formats for different logging levels.
It uses a custom formatter class to handle this functionality.

@author
Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import logging

class LevelFormatter(logging.Formatter):
    """
    Custom logging formatter to use different formats for different log levels.
    
    Attributes:
        formats (dict): A dictionary mapping logging levels to their corresponding formats.
    """
    def __init__(self, formats, *args, **kwargs):
        """
        Initializes the LevelFormatter with the provided format dictionary.
        
        Args:
            formats (dict): A dictionary mapping logging levels to formats.
        """
        super().__init__(*args, **kwargs)
        self.formats = formats

    def format(self, record):
        """
        Format the log record based on its level.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message.
        """
        # Set the format for this record's level
        log_fmt = self.formats.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def setup_logging():
    """
    Sets up logging for the project with level-specific formats.
    
    Args:
        log_file (str): The file where logs will be saved. Defaults to 'logger.log'.
    """
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