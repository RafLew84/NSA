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
from data.selected_item_manager import SelectedItemManager

from ui.menu import create_menu
from ui.data_ui import create_data_ui
from ui.operations_ui import create_operations_ui
from ui.canvas_ui import create_canvas_ui

class MainWindow(Observer):
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root

        self.data_manager = DataManager()
        self.data_manager.add_observer(self)

        self.selected_item_manager = SelectedItemManager()
        self.selected_item_manager.add_observer(self)

        create_menu(self.root)

        self.selected_measured_image = tk.StringVar()
        self.data_listbox = None
        self.remove_button = None
        self.operations_listbox = None
        self.move_for_analisys_button = None
        self.find_button = None

        self.data_ui_section, self.data_listbox, self.remove_button, self.operations_listbox, self.move_for_analisys_button, self.find_button = create_data_ui(
            self.root, 
            self.selected_measured_image, 
            self.data_listbox, 
            self.remove_button,
            self.operations_listbox,
            self.move_for_analisys_button,
            self.find_button
        )

        self.selected_operation = tk.StringVar()

        self.selected_operation = create_operations_ui(self.root, self.selected_operation)

        self.header_info_label = None
        self.canvas = None

        self.canvas_ui_section, self.canvas, self.header_info_label = create_canvas_ui(
            self.root,
            self.header_info_label,
            self.canvas
        )

        # self.create_scaling_ui()
        # self.create_navigation_ui()
        # self.create_show_result_ui()

        # self.data = []

        self.data_listbox.bind("<<ListboxSelect>>", self.show_data_onDataListboxSelect)

        # Ensure the root window also allows the frame to expand
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
    
    def show_data_onDataListboxSelect(self, event=None):
        selection = self.data_listbox.curselection()
        if selection:
            index = selection[0] 
            data_model = self.data_manager.data_for_analisys[index]  
            
            # Update the selected item in SelectedItemManager
            self.selected_item_manager.insert_data(data_model)

    def update(self, observable, *args, **kwargs):
        """Update the UI components based on changes in data."""
        if observable is self.data_manager:
            self.update_listbox()
        elif observable is self.selected_item_manager:
            self.update_selected_item_ui()

    def update_listbox(self):
        """Populate the Listbox with data names from data_for_analisys."""
        self.data_listbox.delete(0, tk.END)
        for data_model in self.data_manager.data_for_analisys:
            self.data_listbox.insert(tk.END, data_model.data_name)
    
    def update_selected_item_ui(self):
        """Update the UI based on the selected item."""
        selected_item = self.selected_item_manager.selected_item
        if selected_item:
            self.header_info_label.config(text=selected_item.get_header_string())

