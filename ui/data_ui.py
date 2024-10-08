# -*- coding: utf-8 -*-
"""
This module creates the UI for managing data and operations within the application.

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

def create_data_ui(
        root, 
        selected_measured_image, 
        data_listbox, 
        remove_button, 
        operations_listbox, 
        move_for_analisys_button,
        find_button,
        image_selection_dropdown
    ):
    """
    Creates the UI for managing data and operations within the application.

    Args:
        root (tk.Tk): The root window or parent widget.
        selected_measured_image (tk.StringVar): Tkinter StringVar to hold the selected image option.
        data_listbox (tk.Listbox): The listbox widget that will display data items.
        remove_button (tk.Button): The button to remove selected data items.
        operations_listbox (tk.Listbox): The listbox widget that will display operations.
        move_for_analisys_button (tk.Button): The button to move selected data items for analysis.
        find_button (tk.Button): The button to trigger the "find" operation.
        image_selection_dropdown (tk.OptionMenu): The dropdown menu for selecting image types.

    Returns:
        tuple: Contains references to the created UI components:
               (data_ui_section, data_listbox, remove_button, operations_listbox, 
                move_for_analisys_button, find_button, image_selection_dropdown)
    """
    try:
        # Create a frame for the data UI section
        data_ui_section = ttk.Frame(root, padding="5")
        data_ui_section.grid(row=0, column=0, rowspan=3, padx=5, pady=2, sticky="nsew")

        measured_image_options = ["Selected", "Original", "Contours", "WContours"]

        selected_measured_image.set(measured_image_options[1])

        # Dropdown menu for image selection
        image_selection_dropdown = tk.OptionMenu(
            data_ui_section, 
            selected_measured_image, 
            *measured_image_options
        )
        image_selection_dropdown.grid(row=0, column=0, padx=5, pady=1, sticky="n")

        # Create a Listbox
        data_listbox = tk.Listbox(
            data_ui_section, 
            width=20, 
            height=10, 
            selectmode=tk.SINGLE
        )
        data_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

        # Scrollbar for the Listbox
        data_listbox_scrollbar = tk.Scrollbar(
            data_ui_section, 
            orient=tk.VERTICAL, 
            command=data_listbox.yview
        )
        data_listbox_scrollbar.grid(row=1, column=1, sticky="ns")
        data_listbox.config(yscrollcommand=data_listbox_scrollbar.set)

        # Remove button
        remove_button = tk.Button(data_ui_section, text="Remove")
        remove_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

        # Name label
        operations_label = tk.Label(data_ui_section, text="Operations:")
        operations_label.grid(row=0, column=2, padx=5, pady=5, sticky="n")

        # Create a Operations Listbox
        operations_listbox = tk.Listbox(
            data_ui_section, 
            width=20, 
            height=10, 
            selectmode=tk.SINGLE
        )
        operations_listbox.grid(row=1, column=2, padx=5, pady=5, sticky="ns")

        # Scrollbar for the Listbox
        operations_listbox_scrollbar = tk.Scrollbar(
            data_ui_section, 
            orient=tk.VERTICAL, 
            command=operations_listbox.yview
        )
        operations_listbox_scrollbar.grid(row=1, column=3, sticky="ns")
        operations_listbox.config(yscrollcommand=operations_listbox_scrollbar.set)

        # analisys button
        move_for_analisys_button = tk.Button(data_ui_section, text="Move for analisys")
        move_for_analisys_button.grid(row=2, column=2, padx=5, pady=5, sticky="n")

        # find button
        font_settings = ("Helvetica", 12, "bold")
        find_button = tk.Button(data_ui_section, text="FIND", font=font_settings)
        find_button.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="nwe")


        # Configure grid row and column weights to allow Listbox to expand
        data_ui_section.grid_rowconfigure(1, weight=1)  
        # data_ui_section.grid_columnconfigure(0, weight=1)

        return data_ui_section, data_listbox, remove_button, operations_listbox, move_for_analisys_button, find_button, image_selection_dropdown
    except Exception as e:
        logger.error(f"Error creating data UI: {e}")
        raise