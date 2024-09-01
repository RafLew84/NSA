import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

def create_show_result_ui(
    root,
    checkbox,
    checkbox_color_var,
    result_treeview,
    delete_button,
    save_button        
):
    result_ui_section = ttk.Frame(root, padding="5")
    result_ui_section.grid(row=0, column=3, rowspan=3, padx=5, pady=2, sticky="nsew")

    result_treeview = ttk.Treeview(result_ui_section)
    result_treeview.grid(row=0, column=0, columnspan=2, sticky="ns")

    treeview_scrollbar = tk.Scrollbar(
        result_ui_section, 
        orient=tk.VERTICAL
        # command=self.measurement_results_treeview.yview
        )
    treeview_scrollbar.grid(row=0, column=2, sticky="ns")

    # result_treeview.bind("<<TreeviewSelect>>", self.treeview_onSelect)

    # Define columns
    result_treeview["columns"] = ("label", "area", "distance", "neighbor")
    result_treeview.column("#0", width=60, minwidth=25)
    result_treeview.column("label", width=40, minwidth=25)
    result_treeview.column("area", width=60, minwidth=25)
    result_treeview.column("distance", width=60, minwidth=25)
    result_treeview.column("neighbor", width=40, minwidth=25)

    # Define headings
    result_treeview.heading("#0", text="Frame", anchor=tk.W)
    result_treeview.heading("label", text="Label", anchor=tk.W)
    result_treeview.heading("area", text="Area", anchor=tk.W)
    result_treeview.heading("distance", text="Distance", anchor=tk.W)
    result_treeview.heading("neighbor", text="Neighbor", anchor=tk.W)

    # self.checkbox_color_var = tk.IntVar()

    # Create a checkbox and associate it with the IntVar
    checkbox = tk.Checkbutton(result_ui_section, text="Change Color", variable=checkbox_color_var, onvalue=255, offvalue=0)
    checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    font_settings = ("Helvetica", 12, "bold")
    save_button = tk.Button(result_ui_section, text="SAVE", font=font_settings)
    save_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="we")

    delete_button = tk.Button(result_ui_section, text="Delete")
    delete_button.grid(row=1, column=1, padx=5, pady=5, sticky="we")

    result_ui_section.grid_rowconfigure(0, weight=1)  

    return result_ui_section, checkbox_color_var, checkbox, result_treeview, delete_button, save_button