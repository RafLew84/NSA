# -*- coding: utf-8 -*-
"""
Main application module.

This module defines the main application class and the entry point of the application.

It sets up a Tkinter-based GUI for managing and analyzing image data, including
displaying images, performing operations, and saving results.

Author:
- Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk
from tkinter import filedialog, messagebox

import numpy as np

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
from data.detection.spots_measurement import (
    analyze_images,
    overlay_labels_on_original,
    overlay_selected_label
)
from data.save_data import save_measured_data

from PIL import Image, ImageTk

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class MainWindow(Observer):
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        try:
            self.root = root

            self.setup_observers()
            create_menu(self.root)
            self.setup_ui_elements()
            self.create_ui()
            self.bind_callbacks()
            self.configure_main_window()
        except Exception as e:
            logger.error(f"Error initializing the main window: {e}")

    def configure_main_window(self):
        """Configures the grid layout for the main window."""
        try:
            self.root.grid_rowconfigure(0, weight=1)
            self.root.grid_columnconfigure(2, weight=1)
        except Exception as e:
            logger.error(f"Error configuring the main window: {e}")

    def bind_callbacks(self):
        """Binds the GUI elements to their respective callback functions."""
        try:
            self.data_listbox.bind("<<ListboxSelect>>", self.show_data_onDataListboxSelect)
            self.operations_listbox.bind("<<ListboxSelect>>", self.show_data_onOperationsListboxSelect)
            self.remove_button.config(command=self.on_remove_button_click)
            self.scale_factor_slider.bind("<ButtonRelease-1>", self.update_image_on_rescale_slider_change)
            self.navigation_slider.bind("<B1-Motion>", self.update_image_from_navigation_slider_onChange)
            self.save_button.config(command=self.save_button_onClick)
            self.move_for_analisys_button.config(command=self.move_for_analisys_button_onClick)
            self.canvas.bind("<Configure>", self.resize_canvas_detection_scrollregion)
            self.selected_measured_image.trace_add('write', self.image_selection_dropdown_onSelect)
            self.find_button.config(command=self.find_button_onClick)
            self.result_treeview.bind("<<TreeviewSelect>>", self.treeview_onSelect)

        except Exception as e:
            logger.error(f"Error binding callbacks: {e}")

    def find_button_onClick(self):
        """Callback for the 'Find' button, triggers the analysis of images."""
        try:
            images = []
            for item in self.data_manager.data_for_analisys:
                images.append(item.image_for_analisys)
            
            all_centrodids, all_areas, all_labels_names, nearest_neighbor_distances_list, nearest_neighbor_names, labeled_images, all_labels_num = analyze_images(images)
            original_images = []
            labeled = []
            labels_names = []
            centroids = []
            for i, item in enumerate(self.data_manager.data_for_analisys):
                original_images.append(item.original_image)
                labels_names.append(all_labels_names[i])
                labeled.append(labeled_images[i])
                centroids.append(all_centrodids[i])
                item.labeled_image = labeled_images[i]
                item.areas = all_areas[i] * item.area_px_nm_coefficient
                item.centroids = all_centrodids[i]
                item.labels_names = all_labels_names[i]
                item.nearest_neighbor_distances = nearest_neighbor_distances_list[i] * item.x_px_nm_coefficient # zmienić
                item.nearest_neighbor_name = nearest_neighbor_names[i]
            
            labeled_overlays = overlay_labels_on_original(original_images, labeled, labels_names, centroids)
            labeled_overlays_white = overlay_labels_on_original(original_images, labeled, labels_names, centroids, 'white')

            for i, item in enumerate(self.data_manager.data_for_analisys):
                item.labeled_overlays = Image.fromarray(labeled_overlays[i])
                item.labeled_overlays_white = Image.fromarray(labeled_overlays_white[i])
            
            self.load_data_to_treeview()

        except Exception as e:
            logger.error(f"Error during image analysis: {e}")
    
    def load_data_to_treeview(self):
        """Loads the analyzed data into the Treeview widget."""
        try:
            # Clear the Treeview widget
            for item in self.result_treeview.get_children():
                self.result_treeview.delete(item)
            # Insert data into the Treeview widget
            for i, frame in enumerate(self.data_manager.data_for_analisys):
                frame_id = self.result_treeview.insert("", "end", text=frame.data_name, open=True)
                for name, area, distance, nname in zip(frame.labels_names, frame.areas, frame.nearest_neighbor_distances, frame.nearest_neighbor_name):
                    formatted_area = f"{area:.3f}"
                    formatted_distance = f"{distance:.3f}"
                    self.result_treeview.insert(frame_id, "end", values=(name, formatted_area, formatted_distance, nname))
        except Exception as e:
            logger.error(f"Error loading data to Treeview: {e}")
    
    def treeview_onSelect(self, event=None):
        """Callback for Treeview item selection."""
        try:
            # Callback function for when an item is selected
            selected_item = self.result_treeview.selection()[0]
            item = self.result_treeview.item(selected_item)
            
            # Navigate up to get the parent frame if a child item is selected
            parent_item = self.result_treeview.parent(selected_item)
            if parent_item:
                frame_name = self.result_treeview.item(parent_item)['text']
            else:
                frame_name = item['text']

            selected_data = []
            
            for data in self.data_manager.data_for_analisys:
                if data.data_name == frame_name:
                    selected_data = data
            
            if item['values']:
                index = item['values'][0] - 1
                original_image = selected_data.original_image
                labeled_image = selected_data.labeled_image
                lebels_names = selected_data.labels_names
                centroids = selected_data.centroids

                image_data = overlay_selected_label(
                    original_image=np.array(original_image),
                    labeled_image=labeled_image,
                    label_names=lebels_names,
                    centroids=centroids,
                    index=index,
                    label_colors=self.checkbox_color_var.get()
                )

                img = Image.fromarray(image_data)
                self.handle_displaying_image_on_canvas(img)

        except Exception as e:
            logger.error(f"Error selecting Treeview item")

    def resize_canvas_detection_scrollregion(self, event=None):
        """Resize the canvas scroll region based on its contents."""
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
    
    def move_for_analisys_button_onClick(self):
        """Handle the move for analysis button click event."""
        try:
            current_item = self.selected_item_manager.selected_item
            current_item.image_for_analisys = current_item.image_for_processing
        except Exception as e:
            logger.error(f"An error occurred while processing analysis button click: {e}")
    
    def image_selection_dropdown_onSelect(self, *args):
        """Update the displayed image based on the selection in the dropdown."""
        try:
            img = self.display_image()
            self.handle_displaying_image_on_canvas(img)
        except Exception as e:
            logger.error(f"An error occurred while selecting image: {e}")
    
    def display_image(self):
        """Retrieve and return the current image based on user selection."""
        try:
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
        except Exception as e:
            logger.error(f"An error occurred while displaying image: {e}")
    
    def save_button_onClick(self):
        """Handle the save button click event to save measured data."""
        try:
            folder_selected = filedialog.askdirectory()
            if folder_selected:
                save_measured_data(folder_selected)
        except Exception as e:
            logger.error(f"An error occurred while saving data: {e}")

    def setup_observers(self):
        """Initializes and sets up observers for data management."""
        try:
            self.data_manager = DataManager()
            self.data_manager.add_observer(self)

            self.selected_item_manager = SelectedItemManager()
            self.selected_item_manager.add_observer(self)
        except Exception as e:
            logger.error(f"Error setting up observers: {e}")

    def create_ui(self):
        """Create and arrange UI components."""
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

        self.navigation_ui_section, self.navigation_slider = create_navigation_ui(
            self.root,
            self.navigation_slider
        )
        
        self.result_ui_section, self.checkbox_color_var, self.checkbox, self.result_treeview, self.delete_button, self.save_button = create_show_result_ui(
            self.root,
            self.checkbox,
            self.checkbox_color_var,
            self.result_treeview,
            self.delete_button,
            self.save_button
        )

    def setup_ui_elements(self):
        """Initialize UI elements."""
        self.setup_data_ui_elements()
        self.setup_operations_ui_elements()
        self.setup_canvas_ui_elements()
        self.setup_results_ui_elements()
        self.setup_navigation_ui_elements()
        self.setup_scaling_ui_elements()

    def setup_results_ui_elements(self):
        """Initialize UI elements for results section."""
        self.checkbox_color_var = tk.IntVar()
        self.checkbox = None
        self.result_treeview = None
        self.delete_button = None
        self.save_button = None

    def setup_navigation_ui_elements(self):
        """Initialize UI elements for navigation section."""
        self.navigation_slider = None

    def setup_scaling_ui_elements(self):
        """Initialize UI elements for scaling section."""
        self.scaling_factor_var = tk.DoubleVar()
        self.scale_factor_slider = None

    def setup_canvas_ui_elements(self):
        """Initialize UI elements for canvas section."""
        self.header_info_label = None
        self.canvas = None

    def setup_operations_ui_elements(self):
        """Initialize UI elements for operations section."""
        self.selected_operation = tk.StringVar()

    def setup_data_ui_elements(self):
        """Initialize UI elements for data section."""
        self.selected_measured_image = tk.StringVar()
        self.data_listbox = None
        self.remove_button = None
        self.operations_listbox = None
        self.move_for_analisys_button = None
        self.find_button = None
        self.image_selection_dropdown = None
    
    def on_remove_button_click(self):
        """Handle the remove button click event to remove the selected item."""
        try:
            self.data_manager.remove_item(self.selected_item_manager.selected_item)
        except Exception as e:
            logger.error(f"An error occurred while removing item: {e}")
        
    
    def show_data_onDataListboxSelect(self, event=None):
        """Handle selection in the data listbox."""
        try:
            selection = self.data_listbox.curselection()
            if selection:
                index = selection[0] 
                data_model = self.data_manager.data_for_analisys[index]  
                
                # Update the selected item in SelectedItemManager
                self.selected_item_manager.insert_data(data_model)
                self.navigation_slider.set(index + 1)
                self.selected_item_manager.selected_item.currently_processing_image = None
                self.selected_item_manager.selected_item.image_for_processing = self.selected_item_manager.selected_item.original_image
        except Exception as e:
            logger.error(f"An error occurred while selecting data in listbox: {e}")

    def show_data_onOperationsListboxSelect(self, event=None):
        """Handle selection in the operations listbox."""
        try:
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
        except Exception as e:
            logger.error(f"An error occurred while selecting operation in listbox: {e}")
    
    def update_image_on_rescale_slider_change(self, event=None):
        """Update the displayed image based on changes in the rescale slider."""
        try:
            if self.selected_item_manager.selected_item.currently_processing_image == None:
                img = self.selected_item_manager.selected_item.image_for_processing
            else:
                img = self.selected_item_manager.selected_item.currently_processing_image
            self.handle_displaying_image_on_canvas(img)
            self.resize_canvas_detection_scrollregion()
        except Exception as e:
            logger.error(f"An error occurred while updating image on rescale slider change: {e}")


    def update_image_from_navigation_slider_onChange(self, event):
        """Update the displayed image based on changes in the navigation slider."""
        try:
            idx = int(self.navigation_slider.get()-1)
            self.selected_item_manager.insert_data(self.data_manager.data_for_analisys[idx])
            self.data_listbox.selection_clear(0, tk.END)
            self.data_listbox.selection_set(idx)
        except Exception as e:
            logger.error(f"An error occurred while updating image from navigation slider: {e}")


    def handle_displaying_image_on_canvas(self, img):
        """Display the provided image on the canvas."""
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

        # Save a reference to the PhotoImage to prevent garbage collection
        self.canvas.image = photo

    def refresh_data_in_operations_listbox(self):
        """Refresh the operations listbox with updated operations."""
        try:
            self.operations_listbox.delete(0, tk.END)
            operations = [item.process_name for item in self.selected_item_manager.selected_item.operations]
            self.operations_listbox.insert(tk.END, *operations)
        except Exception as e:
            logger.error(f"An error occurred while refreshing operations listbox: {e}")


    def update_navigation_slider_range(self):
        """Update the range of the navigation slider based on the number of items."""
        try:
            num_items = len(self.data_manager.data_for_analisys)
            self.navigation_slider.config(from_=1, to=num_items)
        except Exception as e:
            logger.error(f"An error occurred while updating navigation slider range: {e}")


    def update(self, observable, *args, **kwargs):
        """Update the UI components based on changes in data."""
        try:
            if observable is self.data_manager:
                self.update_listbox()
            elif observable is self.selected_item_manager:
                self.update_selected_item_ui()
            elif observable is self.selected_item_manager.selected_item:
                self.update_selected_item_ui()
        except Exception as e:
            logger.error(f"An error occurred during UI update: {e}")

    def update_listbox(self):
        """Populate the Listbox with data names from data_for_analisys."""
        try:
            self.data_listbox.delete(0, tk.END)
            for data_model in self.data_manager.data_for_analisys:
                self.data_listbox.insert(tk.END, data_model.data_name)
                self.update_navigation_slider_range()
        except Exception as e:
            logger.error(f"An error occurred while updating listbox: {e}")
    
    def update_selected_item_ui(self):
        """Update the UI based on the selected item."""
        try:
            selected_item = self.selected_item_manager.selected_item
            if selected_item:
                self.header_info_label.config(text=selected_item.get_header_string())
                self.refresh_data_in_operations_listbox()
                img = self.display_image()
                self.handle_displaying_image_on_canvas(img)
        except Exception as e:
            logger.error(f"An error occurred while updating the selected item UI: {e}")

def main():
    """
    Main entry point for the application.

    Initializes the Tkinter root window and starts the application.
    """
    try:
        root = tk.Tk()
        root.title("Image Analysis Application")
        MainWindow(root)
        root.mainloop()
    except Exception as e:
        logger.error(f"An error occurred while running the application: {e}")
        messagebox.showerror("Error", "An error occurred while starting the application. Please check the logs for more details.")

if __name__ == "__main__":
    main()


