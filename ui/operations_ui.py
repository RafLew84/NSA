import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk
from ui.custom_dropdown import CustomDropdownMenu

from data.preprocessing.preprocess_params_default import preprocess_params
from data.processing.process_params_default import threshold_params, process_params
from data.options_config import options_config

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

    parameter_process_entries = {}
    parameter_process_labels = {}
    parameter_process_buttons = []
    parameter_process_sliders = []
    parameter_process_radio = []
    parameter_process_dropdown = []

    def choose_process_options_dropdownOnChange(selected_option):
        for widget in [*parameter_process_entries.values(),
                    *parameter_process_labels.values(),
                    *parameter_process_buttons,
                    *parameter_process_sliders,
                    *parameter_process_radio,
                    *parameter_process_dropdown]:
            widget.destroy()

        # Clear the collections
        parameter_process_entries.clear()
        parameter_process_labels.clear()
        parameter_process_buttons.clear()
        parameter_process_sliders.clear()
        parameter_process_radio.clear()
        parameter_process_dropdown.clear()

        # options_config

        config = options_config.get(selected_option, {})
        row = 1 # Initialize row for layout

        # Handle radio buttons
        if "radio_buttons" in config:
            selected_option_var = tk.StringVar()
            selected_option_var.set(config["radio_buttons"][0][1])  # Set default value
            
            for text, value in config["radio_buttons"]:
                # radio = tk.Radiobutton(operations_ui_section, text=text, variable=selected_option_var, value=value, command=self.process_and_display_image)
                radio = tk.Radiobutton(operations_ui_section, text=text, variable=selected_option_var, value=value)
                radio.grid(row=row, column=0, padx=5, pady=1, sticky="w")
                parameter_process_radio.append(radio)
                row += 1

        # Handle labels and sliders
        if "labels" in config:
            for label_text, default_value in config["labels"]:
                label = tk.Label(operations_ui_section, text=label_text, width=20)
                label.grid(row=row, column=0, padx=5, pady=1, sticky="w")
                parameter_process_labels[label_text] = label
                
                slider_config = next((item for item in config.get("sliders", []) if item.get("value") == default_value), {})
                if slider_config:
                    # slider = tk.Scale(operations_ui_section, from_=slider_config.get("from_", 0), to=slider_config.get("to", 100), resolution=slider_config.get("resolution", 1), orient=tk.HORIZONTAL, command=self.update_sliders_onChange, length=150)
                    slider = tk.Scale(operations_ui_section, from_=slider_config.get("from_", 0), to=slider_config.get("to", 100), resolution=slider_config.get("resolution", 1), orient=tk.HORIZONTAL, length=150)
                    slider.set(default_value)
                    slider.grid(row=row + 1, column=0, padx=5, pady=2, sticky="w")
                    parameter_process_sliders.append(slider)
                
                row += 2

        # Handle single slider configurations
        if "slider_config" in config:
            label_text = config["label_text"]
            default_value = config["slider_config"].get("value")
            label = tk.Label(operations_ui_section, text=label_text, width=20)
            label.grid(row=row, column=0, padx=5, pady=1, sticky="w")
            parameter_process_labels[label_text] = label
            
            # slider = tk.Scale(operations_ui_section, from_=config["slider_config"].get("from_", 0), to=config["slider_config"].get("to", 100), resolution=config["slider_config"].get("resolution", 1), orient=tk.HORIZONTAL, command=self.update_sliders_onChange, length=150)
            slider = tk.Scale(operations_ui_section, from_=config["slider_config"].get("from_", 0), to=config["slider_config"].get("to", 100), resolution=config["slider_config"].get("resolution", 1), orient=tk.HORIZONTAL, length=150)
            slider.set(default_value)
            slider.grid(row=row + 1, column=0, padx=5, pady=2, sticky="w")
            parameter_process_sliders.append(slider)
            
            row += 2

        # Apply button
        # apply_button = tk.Button(operations_ui_section, text="Apply", command=self.apply_preprocessing_onClick)
        apply_button = tk.Button(operations_ui_section, text="Apply")
        apply_button.grid(row=row + 2, column=0, padx=5, pady=5)
        parameter_process_buttons.append(apply_button)

    # Instantiate CustomDropdownMenu with the update_selected_operation command
    dropdown = CustomDropdownMenu(operations_ui_section, categories, command=choose_process_options_dropdownOnChange)
    dropdown.grid(row=0, column=0, columnspan=2, padx=5, pady=1, sticky="n")

    return operations_ui_section, selected_operation

