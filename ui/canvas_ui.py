import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk


def create_canvas_ui(
        root,
        canvas,
        header_info_label
        ):
    # Create a frame for the data UI section
    canvas_ui_section = ttk.Frame(root, padding="5")
    canvas_ui_section.grid(row=0, column=2, padx=5, pady=2, sticky="nsew")

    header_info_label = tk.Label(canvas_ui_section, text="", justify="left", anchor="w")
    header_info_label.grid(row=0, column=0, padx=5, pady=5, sticky="nwe")

    canvas = tk.Canvas(canvas_ui_section, bg="white")
    canvas.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    vertical_scrollbar_canvas = tk.Scrollbar(
        canvas_ui_section, 
        orient=tk.VERTICAL, 
        command=canvas.yview
        )
    vertical_scrollbar_canvas.grid(row=1, column=1, sticky="ns")
    canvas.configure(yscrollcommand=vertical_scrollbar_canvas.set)
    horizontal_scrollbar_canvas = tk.Scrollbar(
        canvas_ui_section, 
        orient=tk.HORIZONTAL, 
        command=canvas.xview
        )
    horizontal_scrollbar_canvas.grid(row=2, column=0, sticky="ew")
    canvas.configure(xscrollcommand=horizontal_scrollbar_canvas.set)
    
    # Bind event for canvas resizing
    # canvas.bind("<Configure>", resize_canvas_detection_scrollregion)

    # Configure grid row and column weights to allow Listbox to expand
    canvas_ui_section.grid_rowconfigure(1, weight=1)  
    canvas_ui_section.grid_columnconfigure(0, weight=1)

    return canvas_ui_section, canvas, header_info_label
