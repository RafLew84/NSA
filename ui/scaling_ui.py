# -*- coding: utf-8 -*-
"""
This module creates scaling UI section.

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

def create_scaling_ui(
        root,
        scale_factor_var,
        scale_factor_slider
):
    """
    Create the scaling UI section with a slider to adjust the scale factor of images.

    Args:
        root (tk.Tk): The root Tkinter window.
        scale_factor_var (tk.DoubleVar): The variable holding the scale factor value.
        scale_factor_slider (tk.Scale): The slider for adjusting the scale factor.

    Returns:
        tuple: A tuple containing the scaling UI section, the scale factor variable, and the scale factor slider.
    """
    try:
        scaling_ui_section = ttk.Frame(root, padding="5")
        scaling_ui_section.grid(row=1, column=2, padx=5, pady=2, sticky="nsew")

        # Scale factor label and slider
        scale_factor_label = tk.Label(scaling_ui_section, text="Scale Factor:")
        scale_factor_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        scale_factor_var.set(1.0)  # Default scale factor
        scale_factor_slider = tk.Scale(
            scaling_ui_section, 
            from_=0.1, 
            to=10.0, 
            resolution=0.1, 
            orient=tk.HORIZONTAL, 
            variable=scale_factor_var, 
            length=200
            )
        scale_factor_slider.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        scaling_ui_section.grid_columnconfigure(1, weight=1)  

        return scaling_ui_section, scale_factor_var, scale_factor_slider
    
    except Exception as e:
        logger.error(f"Error creating scaling UI: {e}")