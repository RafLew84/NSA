import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

def create_navigation_ui(
        root,
        # prev_button,
        # next_button,
        navigation_slider
):
    navigation_ui_section = ttk.Frame(root, padding="5")
    navigation_ui_section.grid(row=2, column=2, padx=5, pady=2, sticky="nsew")
    # Slider for navigation
    navigation_slider = tk.Scale(
        navigation_ui_section, 
        from_=1, 
        to=1, 
        orient=tk.HORIZONTAL
        # command=self.update_image_from_navigation_slider_onChange
        )
    navigation_slider.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

    # Navigation buttons
    # prev_button = tk.Button(navigation_ui_section, text="Prev")
    # prev_button.grid(row=0, column=0, padx=5, pady=5)
    # next_button = tk.Button(navigation_ui_section, text="Next")
    # next_button.grid(row=0, column=2, padx=5, pady=5)

    navigation_ui_section.grid_columnconfigure(1, weight=1)

    # return navigation_ui_section, navigation_slider, prev_button, next_button
    return navigation_ui_section, navigation_slider