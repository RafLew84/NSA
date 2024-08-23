import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk
from ui.custom_dropdown import CustomDropdownMenu

from data.preprocessing.preprocess_params_default import preprocess_params
from data.processing.process_params_default import threshold_params, process_params

def create_operations_ui(
        root,
        selected_operation
):
    # Create a frame for the data UI section
    operations_ui_section = ttk.Frame(root, padding="5")
    operations_ui_section.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")

    preprocessing_options = list(preprocess_params.keys())
    threshold_options = list(threshold_params.keys())
    processing_options = list(process_params.keys())

    categories = {
        "Preprocessing": preprocessing_options,
        "Thresholding": threshold_options,
        "Binary Process": processing_options
    }

    # self.parameter_preprocess_entries = {}
    # self.parameter_preprocess_labels = {}
    # self.parameter_preprocess_buttons = []
    # self.parameter_preprocess_sliders = []
    # self.parameter_preprocess_radio = []
    # self.parameter_preprocess_dropdown = []

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

# def display_preprocess_options_menu(section, preprocessing_options):
#     try:
#         # Preprocess Dropdown menu options
#         # preprocessing_options = list(preprocess_params.keys())

#         # Create and place dropdown menu
#         choose_preprocess_option_dropdown_var = tk.StringVar()
#         choose_preprocess_option_dropdown_var.set("")  # Set default option
#         choose_preprocess_option_dropdown = tk.OptionMenu(
#             section, 
#             choose_preprocess_option_dropdown_var, 
#             *preprocessing_options, 
#             command=self.choose_preprocess_options_dropdownOnChange
#             )
#         choose_preprocess_option_dropdown.config(width=20)
#         choose_preprocess_option_dropdown.grid(row=1, column=0, padx=5, pady=1, sticky="n")

#         # Labels for function parameters
#         self.parameter_preprocess_entries = {}
#         self.parameter_preprocess_labels = {}
#         self.parameter_preprocess_buttons = []
#         self.parameter_preprocess_sliders = []
#         self.parameter_preprocess_radio = []
#         self.parameter_preprocess_dropdown = []
#     except Exception as e:
#         error_msg = f"Error displaying preprocess options menu: {e}"
#         logger.error(error_msg)
#         raise ValueError(error_msg)

