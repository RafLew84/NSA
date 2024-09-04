# -*- coding: utf-8 -*-
"""
DataManager class and utility functions for managing and processing image data.

This module defines the DataManager class, a singleton responsible for handling 
data related to image analysis. It also includes helper functions for converting 
raw data into grayscale images. The DataManager class integrates with the observer 
pattern, allowing it to notify observers when the data changes. Additionally, 
error handling and logging are implemented to ensure robust processing.

Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.observer.observable import Observable
from data.model.file_data_model import FileDataModel

from data.file_params import (
    calculate_avg_nm_per_px,
    calculate_pixel_to_nm_coefficients
)

from PIL import Image

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class DataManager(Observable):
    """
    Singleton class responsible for managing data for analysis.

    Inherits from Observable to notify observers when data changes.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Create a new instance if it doesn't exist, otherwise return the existing instance.
        """
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initialize the DataManager with an empty data list. Ensures initialization is only done once.
        """
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.data_for_analisys = []  # List to store data for analysis
            self.initialized = True  # Flag to prevent reinitialization

    def clear_data(self):
        """
        Clear all data from the data list and notify observers.
        """
        self.data_for_analisys.clear()
        self.notify_observers()
    
    def get_index(self, item):
        """
        Get the index of the specified item in the data list.

        Args:
            item: The item to find the index of.

        Returns:
            int: The index of the item in the data list.
        """
        return self.data_for_analisys.index(item)

    def remove_item(self, item):
        """
        Remove the specified item from the data list and notify observers.

        Args:
            item: The item to remove from the data list.
        """
        self.data_for_analisys.remove(item)
        self.notify_observers()

    def insert_data(self, file_ext, item):
        """
        Insert new data into the data list based on the file extension.

        Args:
            file_ext (str): The file extension (e.g., 'stp', 's94', 'mpp').
            item (dict): The item containing file data and header information.

        Raises:
            Exception: If there is an error during data insertion.
        """
        try:
            # Calculate conversion coefficients
            x_coeff, y_coeff = calculate_pixel_to_nm_coefficients(item['header_info'], file_ext.lower())
            area_coeff = calculate_avg_nm_per_px(item['header_info'], file_ext.lower())
            
            # Process files based on their extension
            if file_ext.lower() == "stp" or file_ext.lower() == "s94":
                filename_only = os.path.basename(item['file_name'])
                data_model = FileDataModel()
                data_model.data_name = filename_only
                data_model.file_name = item['file_name']
                data_model.header_info = item['header_info']
                data_model.data = item['data']
                data_model.original_image = convert_data_to_greyscale_image(item['data'])
                data_model.area_px_nm_coefficient = area_coeff
                data_model.x_px_nm_coefficient = x_coeff
                data_model.y_px_nm_coefficient = y_coeff
                self.data_for_analisys.append(data_model)
            elif file_ext.lower() == "mpp":
                filename_only = os.path.basename(item['file_name'])
                for i, frame in enumerate(item['data'], start=1):
                    frame_name = f"frame {i}"
                    data_model = FileDataModel()
                    data_model.data_name = frame_name
                    data_model.file_name = item['file_name']
                    data_model.frame_number = i
                    data_model.header_info = item['header_info']
                    data_model.data = frame
                    data_model.original_image = convert_data_to_greyscale_image(frame)
                    data_model.area_px_nm_coefficient = area_coeff
                    data_model.x_px_nm_coefficient = x_coeff
                    data_model.y_px_nm_coefficient = y_coeff
                    self.data_for_analisys.append(data_model)
            self.notify_observers()

        except Exception as e:
            logger.error(f"Error in insert_data: {e}")
            raise

def convert_data_to_greyscale_image(points):
    """
    Create a grayscale image from input data.

    Parameters:
        points (list): List of lists containing the data points.

    Returns:
        PIL.Image.Image: The created grayscale image.

    Raises:
        ValueError: If points is not a list of lists.
    """
    try:

        # Create a new grayscale image
        img = Image.new('L', (len(points[0]), len(points)))

        # Normalize the values in data to the range [0, 255]
        max_z = max(map(max, points))
        min_z = min(map(min, points))
        if max_z == min_z:
            max_z += 1
        for i in range(len(points)):
            for j in range(len(points[i])):
                val = int(255 * (points[i][j] - min_z) / (max_z - min_z))
                img.putpixel((j, i), val)

        return img
    except ValueError as ve:
        msg = f"ValueError in create_greyscale_image: {ve}"
        logger.error(msg)
        raise ValueError(msg)
    except Exception as e:
        logger.error(f"Error in create_greyscale_image: {e}")
        raise