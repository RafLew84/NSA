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

from data.observer.observer import Observer
from data.data_manager import DataManager

from ui.menu import create_menu
from ui.data_ui import create_data_ui

class MainWindow(Observer):
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root

        self.data_manager = DataManager()  # Assuming this is your data manager
        self.data_manager.add_observer(self)

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

    def update(self):
        """Update the UI components based on changes in data."""
        self.update_listbox()

    def update_listbox(self):
        """Populate the Listbox with data names from data_for_analisys."""
        self.data_listbox.delete(0, tk.END)
        for data_model in self.data_manager.data_for_analisys:
            self.data_listbox.insert(tk.END, data_model.data_name)

