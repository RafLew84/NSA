import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

def create_data_ui(root, selected_measured_image, data_listbox, remove_button):
    # Create a frame for the data UI section
    data_ui_section = ttk.Frame(root, padding="5")
    data_ui_section.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")

    measured_image_options = ["Selected", "Original", "Labeled", "Contours", "WContours"]

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

    # Configure grid row and column weights to allow Listbox to expand
    data_ui_section.grid_rowconfigure(1, weight=1)  
    # data_ui_section.grid_columnconfigure(0, weight=1)

    return data_ui_section, data_listbox, remove_button
