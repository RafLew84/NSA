import tkinter as tk
from tkinter import filedialog, messagebox

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from tkinterweb import HtmlFrame 
import markdown

from data.files.read_mpp import read_mpp_file
from data.files.read_s94 import read_s94_file
from data.files.read_stp import read_stp_file

from data.data_manager import DataManager

def create_menu(root):
    """
    Create the top menu with File and About options.

    Args:
        root (tk.Tk): The root Tkinter window.
        select_folder_callback (func): Callback function for selecting folders.
        open_file_callback (func): Callback function for opening files.
        show_about_callback (func): Callback function to show about dialog.
        show_docs_callback (func): Callback function to show documentation.
    """
    menu_bar = tk.Menu(root)

    # File menu with submenus
    file_menu = tk.Menu(menu_bar, tearoff=0)

    # Submenu for Select Folder
    select_folder_menu = tk.Menu(file_menu, tearoff=0)
    select_folder_menu.add_command(label="mpp", command=lambda: select_folder('mpp'))
    select_folder_menu.add_command(label="stp", command=lambda: select_folder('stp'))
    select_folder_menu.add_command(label="s94", command=lambda: select_folder('s94'))
    file_menu.add_cascade(label="Select Folder", menu=select_folder_menu)

    # Submenu for Open File
    open_file_menu = tk.Menu(file_menu, tearoff=0)
    open_file_menu.add_command(label="mpp", command=lambda: open_file('mpp'))
    open_file_menu.add_command(label="stp", command=lambda: open_file('stp'))
    open_file_menu.add_command(label="s94", command=lambda: open_file('s94'))
    file_menu.add_cascade(label="Open Files", menu=open_file_menu)

    # Close option
    file_menu.add_separator()
    file_menu.add_command(label="Close", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # About menu
    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label="About", command=show_about)
    about_menu.add_command(label="Show Docs", command=lambda: show_docs(root))
    menu_bar.add_cascade(label="Info", menu=about_menu)

    # Configure the menu bar
    root.config(menu=menu_bar)

def select_folder(filetype):
    """
    Handle the 'Select Folder' action for different file types.
    """
    data_manager = DataManager()
    folder_selected = filedialog.askdirectory(title=f"Select Folder for {filetype} files")
    data_manager.clear_data()
    files = [os.path.join(folder_selected, f) for f in os.listdir(folder_selected) 
                if f.endswith(filetype.lower()) or f.endswith(filetype.upper())]
    for path in files:
        item = read_file(path, filetype)
        data_manager.insert_data(
            file_ext=filetype,
            item=item
        )

def open_file(filetype):
    data_manager = DataManager()
    file_types = [(f"{filetype.upper()} Files", f"*.{filetype}"), ("All Files", "*.*")]
    files_selected = filedialog.askopenfilenames(title=f"Open {filetype.upper()} File(s)", filetypes=file_types)
    data_manager.clear_data()
    for path in files_selected:
        item = read_file(path, filetype)
        data_manager.insert_data(
            file_ext=filetype,
            item=item
        )


def show_about():
    """
    Show information about the application.
    """
    messagebox.showinfo("About NanoSurface Analyzer", "NanoSurface Analyzer v1.0\nDeveloped by Your Name")

def show_docs(root):
    """
    Display Markdown documentation in a new window.
    """
    # Create a new window for the documentation
    docs_window = tk.Toplevel(root)
    docs_window.title("Documentation")

    # Create an HtmlFrame widget to display the HTML content
    html_frame = HtmlFrame(docs_window, messages_enabled = True)
    html_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    with open("NSA/docs/docs.html", "r") as file:
        md_content = file.read()

    html_content = markdown.markdown(md_content)

    # Load the HTML content into the HtmlFrame
    html_frame.load_html(html_content)

def read_file(file_path, file_type):
    """Read the file based on its type."""
    if file_type == "s94":
        return read_s94_file(file_path)
    elif file_type == "stp":
        return read_stp_file(file_path)
    elif file_type == "mpp":
        return read_mpp_file(file_path)
