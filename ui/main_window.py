# -*- coding: utf-8 -*-
"""
Main application module.

This module defines the main application class and the entry point of the application.

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import tkinter as tk

from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        """
        Initialize the main window.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root

        self.create_menu()

        # self.data = []

        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)



        # self.load_data_tab = LoadDataTab(self.notebook, self)
        # self.preprocessing_tab = PreprocessingTab(self.notebook, self)
        # self.processing_tab = ProcessingTab(self.notebook, self)
        # self.measurement_tab = SpotsMeasurementTab(self.notebook, self)
        # self.spots_detection_tab = SpotsDetectionTab(self.notebook, self)
        # self.noise_analisys_tab = NoiseAnalysisTab(self.notebook, self)

        # Configure grid row and column weights for rescaling
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_menu(self):
        """
        Create the top menu with File and About options.
        """
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Select Folder", command=self.select_folder)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # About menu
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="About", menu=about_menu)

        # Configure the menu bar
        self.root.config(menu=menu_bar)

    def select_folder(self):
        """
        Handle the 'Select Folder' action.
        """
        pass
        # folder_selected = filedialog.askdirectory(title="Select Folder")
        # if folder_selected:
        #     print(f"Selected folder: {folder_selected}")

    def open_file(self):
        """
        Handle the 'Open File' action.
        """
        pass
        # file_selected = filedialog.askopenfilename(title="Open File", filetypes=(("All Files", "*.*"),))
        # if file_selected:
        #     print(f"Selected file: {file_selected}")

    def show_about(self):
        """
        Show information about the application.
        """
        pass
        # messagebox.showinfo("About NanoSurface Analyzer", "NanoSurface Analyzer v1.0\nDeveloped by Your Name")