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
from tkinter import filedialog, messagebox

from tkinterweb import HtmlFrame 
import markdown

from data.files.read_mpp import read_mpp_file
from data.files.read_s94 import read_s94_file
from data.files.read_stp import read_stp_file

from data.data_for_analisys import (
    data_for_analisys,
    insert_data,
    clear_data
)

from ui.menu import create_menu
from ui.data_ui import create_data_ui

class MainWindow:
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root

        create_menu(self.root)
        self.selected_measured_image = tk.StringVar()
        self.data_listbox = None
        self.remove_button = None

        self.data_ui_section, self.data_listbox, self.remove_button = create_data_ui(
            self.root, 
            self.selected_measured_image, 
            self.data_listbox, 
            self.remove_button
        )
        # self.create_canvas_ui()
        # self.create_scaling_ui()
        # self.create_navigation_ui()
        # self.create_show_result_ui()

        # self.data = []

        # Ensure the root window also allows the frame to expand
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
    
    # def create_data_ui(self, root):
    #     # Create a frame for the data UI section
    #     self.data_ui_section = ttk.Frame(root, padding="5")
    #     self.data_ui_section.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")

    #     measured_image_options = ["Selected", "Original", "Labeled", "Contours", "WContours"]

    #     self.selected_measured_image = tk.StringVar()
    #     self.selected_measured_image.set(measured_image_options[1])

    #     # Dropdown menu for image selection
    #     image_selection_dropdown = tk.OptionMenu(
    #         self.data_ui_section, 
    #         self.selected_measured_image, 
    #         *measured_image_options
    #     )
    #     image_selection_dropdown.grid(row=0, column=0, padx=5, pady=1, sticky="n")

    #     # Create a Listbox
    #     self.data_listbox = tk.Listbox(
    #         self.data_ui_section, 
    #         width=20, 
    #         height=10, 
    #         selectmode=tk.SINGLE
    #     )
    #     self.data_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

    #     # Scrollbar for the Listbox
    #     self.data_listbox_scrollbar = tk.Scrollbar(
    #         self.data_ui_section, 
    #         orient=tk.VERTICAL, 
    #         command=self.data_listbox.yview
    #     )
    #     self.data_listbox_scrollbar.grid(row=1, column=1, sticky="ns")
    #     self.data_listbox.config(yscrollcommand=self.data_listbox_scrollbar.set)

    #     # Remove button
    #     self.remove_button = tk.Button(self.data_ui_section, text="Remove")
    #     self.remove_button.grid(row=2, column=0, padx=5, pady=5, sticky="n")

    #     # Configure grid row and column weights to allow Listbox to expand
    #     self.data_ui_section.grid_rowconfigure(1, weight=1)  # Row 1 (Listbox row) can expand
    #     # self.data_ui_section.grid_columnconfigure(0, weight=1)  # Column 0 can expand

