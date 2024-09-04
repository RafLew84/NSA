# -*- coding: utf-8 -*-
"""
This module defines a custom dropdown

Author:
- Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""
import tkinter as tk
from tkinter import font

class CustomDropdownMenu(tk.Frame):
    """
    A custom dropdown menu widget that displays categories and their corresponding options.
    This class inherits from `tk.Frame` and provides a dropdown menu with categories
    shown in bold, and options listed under each category.

    Args:
        parent (tk.Widget): The parent widget (typically a Tkinter window or frame).
        categories (dict): A dictionary where keys are category names and values are lists of options.
        command (function, optional): A function to be called when an option is selected. 
                                      The selected option will be passed as an argument to this function.
        **kwargs: Additional keyword arguments to configure the Frame widget.

    Attributes:
        button (tk.Menubutton): The button that triggers the dropdown menu.
        menu (tk.Menu): The menu that contains categories and options.
        category_font (tk.Font): The font used to display category labels.

    Methods:
        create_menu(categories): Populates the dropdown menu with categories and options.
        on_select(option): Updates the button text with the selected option and calls the provided command.
    """
    def __init__(self, parent, categories, command=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.command = command  # Store the command passed during initialization

        # Create a Menubutton that triggers the dropdown menu
        self.button = tk.Menubutton(self, text="Select an option", relief=tk.RAISED)
        self.button.grid(padx=20, pady=20)

        # Create the Menu
        self.menu = tk.Menu(self.button, tearoff=False)
        self.button["menu"] = self.menu

        # Define font for categories
        self.category_font = font.Font(weight="bold", size=10)  # Bold font for categories

        # Populate the menu with categories and options
        self.create_menu(categories)

    def create_menu(self, categories):
        """
        Populates the dropdown menu with categories and their corresponding options.

        Args:
            categories (dict): A dictionary where keys are category names and values are lists of options.

        Raises:
            TypeError: If categories is not a dictionary.
        """
        for category, options in categories.items():
            # Add category label in uppercase, bold, and black
            self.menu.add_command(
                label=category.upper(),
                state=tk.DISABLED,
                font=self.category_font,
                foreground="black"
            )
            for option in options:
                # Add regular options with a command to update selected_operation
                self.menu.add_command(label=option, command=lambda opt=option: self.on_select(opt))
            self.menu.add_separator()  # Add a separator between categories

    def on_select(self, option):
        """
        Handles the selection of an option from the dropdown menu.

        Args:
            option (str): The selected option.

        This method updates the Menubutton text to show the selected option.
        If a command was provided during initialization, it will be executed with the selected option.
        """
        # Update the Menubutton text to show the selected option
        self.button.config(text=option)
        # If a command is provided, execute it with the selected option
        if self.command:
            self.command(option)