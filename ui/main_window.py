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

from tkinterweb import HtmlFrame 
import markdown

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

        # File menu with submenus
        file_menu = tk.Menu(menu_bar, tearoff=0)

        # Submenu for Select Folder
        select_folder_menu = tk.Menu(file_menu, tearoff=0)
        select_folder_menu.add_command(label="mpp", command=lambda: self.select_folder('mpp'))
        select_folder_menu.add_command(label="stp", command=lambda: self.select_folder('stp'))
        select_folder_menu.add_command(label="s94", command=lambda: self.select_folder('s94'))
        file_menu.add_cascade(label="Select Folder", menu=select_folder_menu)

        # Submenu for Open File
        open_file_menu = tk.Menu(file_menu, tearoff=0)
        open_file_menu.add_command(label="mpp", command=lambda: self.open_file('mpp'))
        open_file_menu.add_command(label="stp", command=lambda: self.open_file('stp'))
        open_file_menu.add_command(label="s94", command=lambda: self.open_file('s94'))
        file_menu.add_cascade(label="Open File", menu=open_file_menu)

        # Close option
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # About menu
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        about_menu.add_command(label="Show Docs", command=self.show_docs)
        menu_bar.add_cascade(label="Info", menu=about_menu)

        # Configure the menu bar
        self.root.config(menu=menu_bar)

    def select_folder(self, filetype):
        """
        Handle the 'Select Folder' action for different file types.
        """
        pass
        # folder_selected = filedialog.askdirectory(title=f"Select Folder for {filetype} files")
        # if folder_selected:
        #     print(f"Selected folder for {filetype} files: {folder_selected}")

    def open_file(self, filetype):
        """
        Handle the 'Open File' action for different file types.
        """
        pass
        # file_types = [(f"{filetype.upper()} Files", f"*.{filetype}"), ("All Files", "*.*")]
        # file_selected = filedialog.askopenfilename(title=f"Open {filetype.upper()} File", filetypes=file_types)
        # if file_selected:
        #     print(f"Selected {filetype.upper()} file: {file_selected}")

    def show_about(self):
        """
        Show information about the application.
        """
        pass
        # messagebox.showinfo("About NanoSurface Analyzer", "NanoSurface Analyzer v1.0\nDeveloped by Your Name")

    def show_docs(self):
        """
        Display Markdown documentation in a new window.
        """
        # Create a new window for the documentation
        docs_window = tk.Toplevel(self.root)
        docs_window.title("Documentation")

        # Create an HtmlFrame widget to display the HTML content
        html_frame = HtmlFrame(docs_window)
        html_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        with open("NSA/docs/docs.md", "r") as file:
            md_content = file.read()

        html_content = markdown.markdown(md_content)

        # Load the HTML content into the HtmlFrame
        html_frame.load_html(html_content)