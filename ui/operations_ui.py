import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk
from ui.custom_dropdown import CustomDropdownMenu

from data.preprocessing.preprocess_params_default import preprocess_params
from data.processing.process_params_default import threshold_params, process_params
from data.options_config import options_config
from data.options_config import preprocess_operations, process_operations

from data.selected_item_manager import SelectedItemManager
from data.model.operation_model import OperationModel

def create_operations_ui(
        root,
        selected_operation
):
    selected_item_manager = SelectedItemManager()
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

    selected_option_var = tk.StringVar()

    def choose_process_options_dropdownOnChange(selected_option):
        selected_operation.set(selected_option)
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
            selected_option_var.set(config["radio_buttons"][0][1])  # Set default value
            
            for text, value in config["radio_buttons"]:
                radio = tk.Radiobutton(operations_ui_section, text=text, variable=selected_option_var, value=value, command=process_and_display_image)
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
                    slider = tk.Scale(operations_ui_section, from_=slider_config.get("from_", 0), to=slider_config.get("to", 100), resolution=slider_config.get("resolution", 1), orient=tk.HORIZONTAL, command=update_sliders_onChange, length=150)
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
            
            slider = tk.Scale(operations_ui_section, from_=config["slider_config"].get("from_", 0), to=config["slider_config"].get("to", 100), resolution=config["slider_config"].get("resolution", 1), orient=tk.HORIZONTAL, command=update_sliders_onChange, length=150)
            slider.set(default_value)
            slider.grid(row=row + 1, column=0, padx=5, pady=2, sticky="w")
            parameter_process_sliders.append(slider)
            
            row += 2

        # Apply button
        apply_button = tk.Button(operations_ui_section, text="Apply", command=apply_preprocessing_onClick)
        apply_button.grid(row=row + 2, column=0, padx=5, pady=5)
        parameter_process_buttons.append(apply_button)

    def update_sliders_onChange(event=None):
        process_and_display_image() 

    def process_and_display_image():
        params = {}

        img = selected_item_manager.selected_item.image_for_processing
        get_values_from_preprocess_menu_items(params)
        result_image, _ = apply_processing_operation(params, img)
        selected_item_manager.selected_item.currently_processing_image = result_image
    
    def apply_preprocessing_onClick():
        params = {}
        img = selected_item_manager.selected_item.image_for_processing

        result_image = None
        process_name = None

        get_values_from_preprocess_menu_items(params)
        # Apply preprocessing based on selected option and parameters
        result_image, process_name = apply_processing_operation(params, img)
        operation = OperationModel(process_name, result_image)

        selected_item_manager.selected_item.add_operation(operation)
        selected_item_manager.selected_item.image_for_processing = result_image
        selected_item_manager.selected_item.currently_processing_image = None
    
    def apply_processing_operation(params, img):

        if selected_operation.get() in preprocess_operations:
            process_function = preprocess_operations[selected_operation.get()]
            process_name, result_image = process_function(params, img)
        elif selected_operation.get() in process_operations:
            process_function = process_operations[selected_operation.get()]
            process_name, result_image = process_function(params, img)
        else:
            msg = f"Invalid preprocessing option: {selected_operation}"
            # logger.error(msg)
            raise ValueError(msg)
            
        return result_image, process_name
    
    def get_values_from_preprocess_menu_items(params):
        option = selected_operation.get()

        def add_odd_value(slider):
            value = slider.get()
            return value + 1 if value % 2 == 0 else value


        preprocess_map = {
            "GaussianFilter": lambda: params.update({'sigma': parameter_process_sliders[0].get()}),
            "Gamma Adjustment": lambda: params.update({'gamma': parameter_process_sliders[0].get()}),
            "Adaptive Equalization": lambda: params.update({'limit': parameter_process_sliders[0].get()}),
            "Contrast Stretching": lambda: params.update({
                'min': parameter_process_sliders[0].get(),
                'max': parameter_process_sliders[1].get()
            }),
            "Gaussian Blur": lambda: params.update({
                'sigmaY': add_odd_value(parameter_process_sliders[0]),
                'sigmaX': add_odd_value(parameter_process_sliders[1])
            }),
            "Non-local Mean Denoising": lambda: params.update({
                'h': parameter_process_sliders[0].get(),
                'templateWindowSize': parameter_process_sliders[1].get(),
                'searchWindowSize': add_odd_value(parameter_process_sliders[2])
            }),
            "Erosion": lambda: params.update({
                'kernel_type': selected_option_var.get(),
                'iterations': parameter_process_sliders[1].get(),
                'kernel_size': add_odd_value(parameter_process_sliders[0])
            }),
            "Propagation": lambda: params.update({
                'type': selected_option_var.get(),
                'marker_value': parameter_process_sliders[0].get(),
            }),
            "Polynomial Leveling": lambda: params.update({
                'order': parameter_process_sliders[0].get(),
            }),
            "Adaptive Leveling": lambda: params.update({
                'disk_size': parameter_process_sliders[0].get(),
            }),
            "Local Median Filter": lambda: params.update({
                'size': parameter_process_sliders[0].get(),
            }),
            "Binary Greyscale Erosion": lambda: params.update({
                'kernel_type': selected_option_var.get(),
                'kernel_size': add_odd_value(parameter_process_sliders[0])
            }),
            "Gaussian Greyscale Erosion": lambda: params.update({
                'mask_size': add_odd_value(parameter_process_sliders[0]),
                'sigma': parameter_process_sliders[1].get()
            }),
            "Binary Greyscale Dilation": lambda: params.update({
                'kernel_type': selected_option_var.get(),
                'kernel_size': add_odd_value(parameter_process_sliders[0])
            }),
            "Gaussian Greyscale Dilation": lambda: params.update({
                'mask_size': add_odd_value(parameter_process_sliders[0]),
                'sigma': parameter_process_sliders[1].get()
            }),
            "Binary Greyscale Opening": lambda: params.update({
                'kernel_type': selected_option_var.get(),
                'kernel_size': add_odd_value(parameter_process_sliders[0])
            }),
            "Gaussian Greyscale Opening": lambda: params.update({
                'mask_size': add_odd_value(parameter_process_sliders[0]),
                'sigma': parameter_process_sliders[1].get()
            }),
            "Binary Greyscale Closing": lambda: params.update({
                'kernel_type': selected_option_var.get(),
                'kernel_size': add_odd_value(parameter_process_sliders[0])
            }),
            "White Top Hat": lambda: params.update({
                'selem_type': selected_option_var.get(),
                'selem_size': parameter_process_sliders[0].get()
            }),
            "Black Top Hat": lambda: params.update({
                'selem_type': selected_option_var.get(),
                'selem_size': parameter_process_sliders[0].get()
            }),
            "Gaussian Greyscale Closing": lambda: params.update({
                'mask_size': add_odd_value(parameter_process_sliders[0]),
                'sigma': parameter_process_sliders[1].get()
            }),
            "Gaussian Sharpening": lambda: params.update({
                'radius': parameter_process_sliders[0].get(),
                'amount': parameter_process_sliders[1].get()
            }),
            "Local Threshold": lambda: params.update({
                'method': selected_option_var.get(),
                'block_size': parameter_process_sliders[0].get(),
                'offset': parameter_process_sliders[1].get()
            }),
            "Niblack Threshold": lambda: params.update({
                'window_size': parameter_process_sliders[0].get(),
                'k': parameter_process_sliders[1].get()
            }),
            "Sauvola Threshold": lambda: params.update({
                'window_size': parameter_process_sliders[0].get(),
                'k': parameter_process_sliders[1].get(),
                'r': parameter_process_sliders[2].get()
            }),
            "Binary Erosion": lambda: params.update({
                'footprint_type': selected_option_var.get(),
                'footprint_size': parameter_process_sliders[0].get()
            }),
            "Binary Dilation": lambda: params.update({
                'footprint_type': selected_option_var.get(),
                'footprint_size': parameter_process_sliders[0].get()
            }),
            "Binary Opening": lambda: params.update({
                'footprint_type': selected_option_var.get(),
                'footprint_size': parameter_process_sliders[0].get()
            }),
            "Binary Closing": lambda: params.update({
                'footprint_type': selected_option_var.get(),
                'footprint_size': parameter_process_sliders[0].get()
            }),
            "Remove Small Holes": lambda: params.update({
                'area_threshold': parameter_process_sliders[0].get(),
                'connectivity': parameter_process_sliders[1].get()
            }),
            "Remove Small Objects": lambda: params.update({
                'min_size': parameter_process_sliders[0].get(),
                'connectivity': parameter_process_sliders[1].get()
            }),
            "Binary Threshold": lambda: params.update({
                'threshold': parameter_process_sliders[0].get()
            }),
        }

        # Apply the corresponding function based on the selected preprocess option
        if option in preprocess_map:
            preprocess_map[option]()

        # Handle any additional parameters from preprocess menu items
        for param_name, entry in parameter_process_entries.items():
            try:
                params[param_name] = int(entry.get())
            except ValueError:
                params[param_name] = entry.get()

    # Instantiate CustomDropdownMenu with the update_selected_operation command
    dropdown = CustomDropdownMenu(operations_ui_section, categories, command=choose_process_options_dropdownOnChange)
    dropdown.grid(row=0, column=0, columnspan=2, padx=5, pady=1, sticky="n")

    return operations_ui_section, selected_operation

