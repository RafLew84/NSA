import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

def create_scaling_ui(
        root,
        scale_factor_var,
        scale_factor_slider
):
    scaling_ui_section = ttk.Frame(root, padding="5")
    scaling_ui_section.grid(row=1, column=2, padx=5, pady=2, sticky="nsew")

    # Scale factor label and slider
    scale_factor_label = tk.Label(scaling_ui_section, text="Scale Factor:")
    scale_factor_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    scale_factor_var.set(1.0)  # Default scale factor
    scale_factor_slider = tk.Scale(
        scaling_ui_section, 
        from_=0.1, 
        to=10.0, 
        resolution=0.1, 
        orient=tk.HORIZONTAL, 
        variable=scale_factor_var, 
        length=200
        )
    scale_factor_slider.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    
    # Bind event for slider changes
    # self.scale_factor_slider.bind("<ButtonRelease-1>", self.update_image_on_rescale_slider_change)

    scaling_ui_section.grid_columnconfigure(1, weight=1)  

    return scaling_ui_section, scale_factor_var, scale_factor_slider