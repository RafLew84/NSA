# -*- coding: utf-8 -*-
"""
Main application module.

This module defines the main application class and the entry point of the application.

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

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
        self.root = root
        self.root.title("NanoSurface Analyzer")