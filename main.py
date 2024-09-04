# -*- coding: utf-8 -*-
"""
Entry point of the application.

This module serves as the entry point for the application, initializing the necessary configurations,
and starting the main application window.

@author
Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk
import config

from app import App

import logging

def main():
    """
    Main function to start the application.

    This function initializes the logging configuration, creates the Tkinter root window,
    and initializes the main application window.
    """
    try:
        # Initialize logging configuration
        config.setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Logging is set up.")

        # Create the main Tkinter window
        root = tk.Tk()

        # Initialize and start the main application
        app = App(root)
        logger.info("Application started successfully.")

        # Start the Tkinter main event loop
        root.mainloop()

    except Exception as e:
        # Log any unhandled exceptions
        logger = logging.getLogger(__name__)
        logger.critical(f"Unhandled exception in main: {e}")
        print(f"Critical error: {e}")  # Optional: print error message for debugging

if __name__ == '__main__':
    main()