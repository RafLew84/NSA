# -*- coding: utf-8 -*-
"""
This module creates ui for navigation in app

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

def create_navigation_ui(
        root,
        navigation_slider
):
    """
    Create the navigation UI section with a slider for navigating through images.

    Args:
        root (tk.Tk): The root Tkinter window.
        navigation_slider (tk.Scale): The navigation slider for image navigation.

    Returns:
        tuple: A tuple containing the navigation UI section frame and the navigation slider.
    """
    try:
        navigation_ui_section = ttk.Frame(root, padding="5")
        navigation_ui_section.grid(row=2, column=2, padx=5, pady=2, sticky="nsew")
        # Slider for navigation
        navigation_slider = tk.Scale(
            navigation_ui_section, 
            from_=1, 
            to=1, 
            orient=tk.HORIZONTAL
            )
        navigation_slider.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        navigation_ui_section.grid_columnconfigure(1, weight=1)

        return navigation_ui_section, navigation_slider
    
    except Exception as e:
        logger.error(f"Error creating navigation UI: {e}")
        tk.messagebox.showerror("Error", f"Failed to create navigation UI: {e}")