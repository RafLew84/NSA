import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk
from ui.custom_dropdown import CustomDropdownMenu

def create_operations_ui(
        root,
        selected_operation
):
    # Create a frame for the data UI section
    operations_ui_section = ttk.Frame(root, padding="5")
    operations_ui_section.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")

    categories = {
        "Category 1": ["Option 1.1", "Option 1.2"],
        "Category 2": ["Option 2.1", "Option 2.2"]
    }

    # selected_operation.set(operations[0])

    # Dropdown menu for image selection
    # opedrations_selection_dropdown = tk.OptionMenu(
    #     operations_ui_section, 
    #     selected_operation, 
    #     *operations
    # )
    # opedrations_selection_dropdown.grid(row=0, column=0, columnspan=2, padx=5, pady=1, sticky="n")
    dropdown = CustomDropdownMenu(operations_ui_section, categories)
    dropdown.grid(row=0, column=0, columnspan=2, padx=5, pady=1, sticky="n")

    return operations_ui_section, selected_operation

