# -*- coding: utf-8 -*-
"""
This module defines a function to create a UI canvas with scrollbars in a Tkinter application. 
The canvas is placed within a frame, alongside a label for displaying header information.

The function is designed to be flexible and can be integrated into various Tkinter GUI applications.

Author:
- Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def create_canvas_ui(
        root,
        canvas,
        header_info_label
        ):
    """
    Creates a UI section with a canvas, scrollbars, and a header label.

    Args:
        root (tk.Tk or tk.Frame): The parent widget (typically the main Tkinter window or a frame).
        canvas (tk.Canvas): The canvas widget to be created and configured.
        header_info_label (tk.Label): A label widget to display header information.

    Returns:
        tuple: Contains the following Tkinter widgets:
            canvas_ui_section (ttk.Frame): The frame containing the canvas and scrollbars.
            canvas (tk.Canvas): The configured canvas widget with scrollbars.
            header_info_label (tk.Label): The label for displaying header information.

    Raises:
        ValueError: If the root parameter is None.
        TypeError: If the root, canvas, or header_info_label parameters are not Tkinter widgets.
    """
    # Error handling for invalid parameters
    if root is None:
        logger.error("The root parameter cannot be None.")
        raise ValueError("The root parameter cannot be None.")
    if not isinstance(root, (tk.Tk, tk.Frame)):
        logger.error("The root parameter must be a Tkinter Tk or Frame widget.")
        raise TypeError("The root parameter must be a Tkinter Tk or Frame widget.")
    if not isinstance(canvas, tk.Canvas) and canvas is not None:
        logger.error("The canvas parameter must be a Tkinter Canvas widget or None.")
        raise TypeError("The canvas parameter must be a Tkinter Canvas widget or None.")
    if not isinstance(header_info_label, tk.Label) and header_info_label is not None:
        logger.error("The header_info_label parameter must be a Tkinter Label widget or None.")
        raise TypeError("The header_info_label parameter must be a Tkinter Label widget or None.")

    # Create a frame for the data UI section
    canvas_ui_section = ttk.Frame(root, padding="5")
    canvas_ui_section.grid(row=0, column=2, padx=5, pady=2, sticky="nsew")

    header_info_label = tk.Label(canvas_ui_section, text="", justify="left", anchor="w")
    header_info_label.grid(row=0, column=0, padx=5, pady=5, sticky="nwe")

    canvas = tk.Canvas(canvas_ui_section, bg="white")
    canvas.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    vertical_scrollbar_canvas = tk.Scrollbar(
        canvas_ui_section, 
        orient=tk.VERTICAL, 
        command=canvas.yview
        )
    vertical_scrollbar_canvas.grid(row=1, column=1, sticky="ns")
    canvas.configure(yscrollcommand=vertical_scrollbar_canvas.set)
    horizontal_scrollbar_canvas = tk.Scrollbar(
        canvas_ui_section, 
        orient=tk.HORIZONTAL, 
        command=canvas.xview
        )
    horizontal_scrollbar_canvas.grid(row=2, column=0, sticky="ew")
    canvas.configure(xscrollcommand=horizontal_scrollbar_canvas.set)

    # Configure grid row and column weights to allow Listbox to expand
    canvas_ui_section.grid_rowconfigure(1, weight=1)  
    canvas_ui_section.grid_columnconfigure(0, weight=1)

    return canvas_ui_section, canvas, header_info_label
