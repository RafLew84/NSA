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
from ui.scaling_ui import create_scaling_ui
from ui.navigation_ui import create_navigation_ui
from ui.show_result_ui import create_show_result_ui

from PIL import Image, ImageTk

import logging

logger = logging.getLogger(__name__)

class MainWindow(Observer):
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root

        self.setup_observers()
        create_menu(self.root)
        self.setup_ui_elements()
        self.create_ui()
        self.bind_callbacks()
        self.configure_main_window()

    def configure_main_window(self):
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

    def bind_callbacks(self):
        self.data_listbox.bind("<<ListboxSelect>>", self.show_data_onDataListboxSelect)
        self.operations_listbox.bind("<<ListboxSelect>>", self.show_data_onOperationsListboxSelect)
        self.remove_button.config(command=self.on_remove_button_click)
        self.scale_factor_slider.bind("<ButtonRelease-1>", self.update_image_on_rescale_slider_change)
        self.navigation_slider.bind("<B1-Motion>", self.update_image_from_navigation_slider_onChange)
        self.save_button.config(command=self.save_button_onClick)
        self.move_for_analisys_button.config(command=self.move_for_analisys_button_onClick)

        self.selected_measured_image.trace_add('write', self.image_selection_dropdown_onSelect)
    
    def move_for_analisys_button_onClick(self):
        current_item = self.selected_item_manager.selected_item
        current_item.image_for_analisys = current_item.image_for_processing
    
    def image_selection_dropdown_onSelect(self, *args):
        img = self.display_image()
        self.handle_displaying_image_on_canvas(img)
        # print(self.selected_measured_image.get())
    
    def display_image(self):
        item = self.selected_item_manager.selected_item
        if self.selected_item_manager.selected_item.currently_processing_image:
            img = self.selected_item_manager.selected_item.currently_processing_image
        elif self.selected_measured_image.get() == "Selected":
            img = item.image_for_analisys
        elif self.selected_measured_image.get() == "Original":
            img = item.original_image
        elif self.selected_measured_image.get() == "Contours":
            img = item.labeled_overlays
        elif self.selected_measured_image.get() == "WContours":
            img = item.labeled_overlays_white
        return img
    
    def save_button_onClick(self):
        print(self.selected_operation.get())

    def setup_observers(self):
        self.data_manager = DataManager()
        self.data_manager.add_observer(self)

        self.selected_item_manager = SelectedItemManager()
        self.selected_item_manager.add_observer(self)

    def create_ui(self):
        self.data_ui_section, self.data_listbox, self.remove_button, self.operations_listbox, self.move_for_analisys_button, self.find_button, self.image_selection_dropdown = create_data_ui(
            self.root, 
            self.selected_measured_image, 
            self.data_listbox, 
            self.remove_button,
            self.operations_listbox,
            self.move_for_analisys_button,
            self.find_button,
            self.image_selection_dropdown
        )

        self.operations_section, self.selected_operation = create_operations_ui(
            self.root, 
            self.selected_operation
        )

        self.canvas_ui_section, self.canvas, self.header_info_label = create_canvas_ui(
            self.root,
            self.header_info_label,
            self.canvas
        )

        self.scaling_ui_section, self.scaling_factor_var, self.scale_factor_slider = create_scaling_ui(
            self.root,
            self.scaling_factor_var,
            self.scale_factor_slider
        )

        # self.navigation_ui_section, self.navigation_slider, self.prev_button, self.next_button = create_navigation_ui(
        self.navigation_ui_section, self.navigation_slider = create_navigation_ui(
            self.root,
            self.navigation_slider
        )
        
        self.result_ui_section, self.checkbox_color_var, self.result_treeview, self.delete_button, self.save_button = create_show_result_ui(
            self.root,
            self.checkbox_color_var,
            self.result_treeview,
            self.delete_button,
            self.save_button
        )

    def setup_ui_elements(self):
        self.setup_data_ui_elements()
        self.setup_operations_ui_elements()
        self.setup_canvas_ui_elements()
        self.setup_results_ui_elements()
        self.setup_navigation_ui_elements()
        self.setup_scaling_ui_elements()

    def setup_results_ui_elements(self):
        self.checkbox_color_var = tk.IntVar()
        self.result_treeview = None
        self.delete_button = None
        self.save_button = None

    def setup_navigation_ui_elements(self):
        self.navigation_slider = None

    def setup_scaling_ui_elements(self):
        self.scaling_factor_var = tk.DoubleVar()
        self.scale_factor_slider = None

    def setup_canvas_ui_elements(self):
        self.header_info_label = None
        self.canvas = None

    def setup_operations_ui_elements(self):
        self.selected_operation = tk.StringVar()

    def setup_data_ui_elements(self):
        self.selected_measured_image = tk.StringVar()
        self.data_listbox = None
        self.remove_button = None
        self.operations_listbox = None
        self.move_for_analisys_button = None
        self.find_button = None
        self.image_selection_dropdown = None
    
    def on_remove_button_click(self):
        self.data_manager.remove_item(self.selected_item_manager.selected_item)
        
    
    def show_data_onDataListboxSelect(self, event=None):
        selection = self.data_listbox.curselection()
        if selection:
            index = selection[0] 
            data_model = self.data_manager.data_for_analisys[index]  
            
            # Update the selected item in SelectedItemManager
            self.selected_item_manager.insert_data(data_model)
            self.navigation_slider.set(index + 1)
            self.selected_item_manager.selected_item.currently_processing_image = None
            self.selected_item_manager.selected_item.image_for_processing = self.selected_item_manager.selected_item.original_image
    
    def show_data_onOperationsListboxSelect(self, event=None):
        selection = self.operations_listbox.curselection()
        if selection:
            index = selection[0]
            self.selected_item_manager.selected_item.currently_processing_image = None
            img = self.selected_item_manager.selected_item.operations[index].image
            self.selected_item_manager.selected_item.image_for_processing = img
            self.handle_displaying_image_on_canvas(img)
            self.operations_listbox.selection_clear(0, tk.END)
            self.operations_listbox.selection_set(index)
            self.operations_listbox.activate(index)
    
    def update_image_on_rescale_slider_change(self, event=None):
        if self.selected_item_manager.selected_item.currently_processing_image == None:
            img = self.selected_item_manager.selected_item.image_for_processing
        else:
            img = self.selected_item_manager.selected_item.currently_processing_image
        self.handle_displaying_image_on_canvas(img)

    def update_image_from_navigation_slider_onChange(self, event):
        idx = int(self.navigation_slider.get()-1)
        self.selected_item_manager.insert_data(self.data_manager.data_for_analisys[idx])
        self.data_listbox.selection_clear(0, tk.END)
        self.data_listbox.selection_set(idx)

    def handle_displaying_image_on_canvas(self, img, text=None):
        self.canvas.delete("all")
        # Retrieve the scale factor
        scale_factor = self.scaling_factor_var.get()
        # Resize the image
        img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)), Image.LANCZOS)

        # Convert the PIL image to a Tkinter PhotoImage
        image_width, image_height = img.size
        photo = ImageTk.PhotoImage(img)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=photo)
        if text:
            self.data_canvas_processing.create_text(
                20, 
                image_height + 10, 
                text=text, 
                anchor=tk.NW, 
                font=("Arial", 16), 
                fill="black"
            )

        # Save a reference to the PhotoImage to prevent garbage collection
        self.canvas.image = photo

    def refresh_data_in_operations_listbox(self):
        self.operations_listbox.delete(0, tk.END)
        operations = [item.process_name for item in self.selected_item_manager.selected_item.operations]
        self.operations_listbox.insert(tk.END, *operations)

    def update_navigation_slider_range(self):
        num_items = len(self.data_manager.data_for_analisys)
        self.navigation_slider.config(from_=1, to=num_items)

    def update(self, observable, *args, **kwargs):
        """Update the UI components based on changes in data."""
        if observable is self.data_manager:
            self.update_listbox()
        elif observable is self.selected_item_manager:
            self.update_selected_item_ui()
        elif observable is self.selected_item_manager.selected_item:
            self.update_selected_item_ui()

    def update_listbox(self):
        """Populate the Listbox with data names from data_for_analisys."""
        self.data_listbox.delete(0, tk.END)
        for data_model in self.data_manager.data_for_analisys:
            self.data_listbox.insert(tk.END, data_model.data_name)
            self.update_navigation_slider_range()
    
    def update_selected_item_ui(self):
        """Update the UI based on the selected item."""
        selected_item = self.selected_item_manager.selected_item
        if selected_item:
            self.header_info_label.config(text=selected_item.get_header_string())
            self.refresh_data_in_operations_listbox()
            # if self.selected_item_manager.selected_item.currently_processing_image == None:
            #     img = self.selected_item_manager.selected_item.image_for_processing
            # else:
            #     img = self.selected_item_manager.selected_item.currently_processing_image
            img = self.display_image()
            self.handle_displaying_image_on_canvas(img)
            # You can add more UI updates here based on the selected item

