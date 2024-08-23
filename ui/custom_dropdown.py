import tkinter as tk
from tkinter import font

class CustomDropdownMenu(tk.Frame):
    def __init__(self, parent, categories, **kwargs):
        super().__init__(parent, **kwargs)

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
        for category, options in categories.items():
            # Add category label in uppercase, bold, and black
            self.menu.add_command(
                label=category.upper(),
                state=tk.DISABLED,
                font=self.category_font,
                foreground="black"
            )
            for option in options:
                # Add regular options
                self.menu.add_command(label=option)
            self.menu.add_separator()  # Add a separator between categories