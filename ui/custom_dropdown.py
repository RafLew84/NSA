import tkinter as tk

class CustomDropdownMenu(tk.Frame):
    def __init__(self, parent, categories, **kwargs):
        super().__init__(parent, **kwargs)

        # Create a Menubutton that triggers the dropdown menu
        self.button = tk.Menubutton(self, text="Select an option", relief=tk.RAISED)
        self.button.grid(padx=20, pady=20)

        # Create the Menu
        self.menu = tk.Menu(self.button, tearoff=False)
        self.button["menu"] = self.menu

        # Populate the menu with categories and options
        self.create_menu(categories)

    def create_menu(self, categories):
        for category, options in categories.items():
            self.menu.add_command(label=category, state=tk.DISABLED)  # Add category as a disabled label
            for option in options:
                self.menu.add_command(label=option, command=lambda opt=option: self.on_select(opt))
            self.menu.add_separator()  # Add a separator between categories

    def on_select(self, option):
        print(f"Selected: {option}")