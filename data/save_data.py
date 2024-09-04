# -*- coding: utf-8 -*-
"""
This script handles the saving of image data and associated measurements.
It performs the following tasks:
1. Converts and saves images from numpy arrays or PIL Image objects to specified file paths.
2. Organizes and saves measurement data into an Excel file, including associated images in designated folders.
3. Utilizes the `DataManager` class to retrieve data for analysis.

Functions:
- `save_image(image, path)`: Converts and saves an image to the specified file path.
- `save_measured_data(base_path)`: Saves measured data and associated images to the specified directory.

Author:
- Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import numpy as np
import pandas as pd
from PIL import Image
from datetime import datetime
from data.data_manager import DataManager

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def save_image(image, path):
    """
    Save an image to the specified path.

    Args:
        image (numpy.ndarray or PIL.Image.Image): The image to save. Can be a numpy array (grayscale or RGB/RGBA) or a PIL Image.
        path (str): The file path where the image should be saved.

    Raises:
        TypeError: If the image type is not supported.
        ValueError: If the image data is None or if the image shape is unsupported.
    """
    try:
        if image is not None:
            if isinstance(image, np.ndarray):
                # Convert dtype to uint8 if necessary
                if image.dtype == np.int64:
                    # Normalize and convert int64 to uint8
                    image = np.clip(image, 0, 255).astype(np.uint8)
                elif image.dtype == np.float32 or image.dtype == np.float64:
                    # Normalize float values to the range [0, 255]
                    image = (255 * np.clip(image, 0, 1)).astype(np.uint8)
                elif image.dtype != np.uint8:
                    raise TypeError(f"Unsupported dtype: {image.dtype}")

                # Handle grayscale and RGB images
                if image.ndim == 2:  # Grayscale image
                    image = Image.fromarray(image, mode='L')
                elif image.ndim == 3 and image.shape[2] in [3, 4]:  # RGB or RGBA image
                    image = Image.fromarray(image, mode='RGB' if image.shape[2] == 3 else 'RGBA')
                else:
                    raise ValueError(f"Unsupported image shape: {image.shape}")

            elif isinstance(image, Image.Image):
                pass  # Image is already a PIL Image
            else:
                raise TypeError(f"Unsupported image type: {type(image)}")

            # Save the image
            image.save(path)
        else:
            raise ValueError("Image is None.")
    except Exception as e:
        logging.error(f"Failed to save image at {path}: {e}")

def save_measured_data(base_path):
    """
    Save measured data and associated images to a specified directory.

    Args:
        base_path (str): The base directory where the data should be saved.

    Raises:
        Exception: If there is an issue with saving the data or images.
    """
    try:
        manager = DataManager()
        data = manager.data_for_analisys
        # Get the current date and time for the file name
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        folder_path = os.path.join(base_path, current_time)

        # Create directories to save images
        os.makedirs(os.path.join(folder_path, 'labeled_overlays'), exist_ok=True)
        os.makedirs(os.path.join(folder_path, 'labeled_overlays_white'), exist_ok=True)
        excel_file_path = os.path.join(folder_path, f"measured_data_{current_time}.xlsx")

        # Create a dictionary to hold DataFrames for each sheet
        sheet_data = {}

        # Organize data by name
        for item in data:
            name = item.data_name

            # Save images using the helper function
            save_image(item.labeled_overlays, os.path.join(folder_path, f'labeled_overlays/{name}_overlays.bmp'))
            save_image(item.labeled_overlays_white, os.path.join(folder_path, f'labeled_overlays_white/{name}_overlays_white.bmp'))
            
            # Prepare the row data using zip
            rows = []
            for label, area, distance, neighbor_name in zip(item.labels_names, item.areas, item.nearest_neighbor_distances, item.nearest_neighbor_name):
                row = {
                    'label': label,
                    'area': area,
                    'nearest_neighbor_distance': distance,
                    'nearest_neighbor_label': neighbor_name
                }
                rows.append(row)

            # Convert rows to DataFrame
            df = pd.DataFrame(rows)

            # Add DataFrame to the dictionary with the name as the key
            sheet_data[name] = df

        # Write all DataFrames to an Excel file with different sheets
        with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
            for sheet_name, df in sheet_data.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
    except Exception as e:
        logging.error(f"Failed to save measured data: {e}")