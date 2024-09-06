# -*- coding: utf-8 -*-
"""
Main application module.

This module defines the main application class and the entry point of the application.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from ui.main_window import MainWindow

import logging

logger = logging.getLogger(__name__)

class App:
    """
    Main application class.

    This class represents the main application class and manages its components.

    """

    def __init__(self, root):
        """
        Initialize the main application.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        try:
            self.root = root
            self.root.title("NEtCAT NanoSurface Analyzer")
            
            # Initialize the main window UI
            MainWindow(self.root)
            logger.info("Application initialized successfully.")
        except Exception as e:
            logger.error(f"Error during application initialization: {e}")
            raise  # Optionally re-raise the error to halt execution in case of a critical failure

if __name__ == "__main__":
    # Entry point of the application
    try:
        root = tk.Tk()  # Create the main Tkinter window
        app = App(root)  # Instantiate the App class
        root.mainloop()  # Start the Tkinter main loop
    except Exception as e:
        logger.critical(f"Unhandled exception in the main application: {e}")
