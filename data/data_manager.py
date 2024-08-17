import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.observer.observable import Observable
from data.model.file_data_model import FileDataModel

from PIL import Image

import logging

logger = logging.getLogger(__name__)

class DataManager(Observable):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.data_for_analisys = []
            self.initialized = True

    def clear_data(self):
        self.data_for_analisys.clear()
        self.notify_observers()

    def remove_item(self, item):
        self.data_for_analisys.remove(item)
        self.notify_observers()

    def insert_data(self, file_ext, item):
        # Existing logic for inserting data
        if file_ext.lower() == "stp" or file_ext.lower() == "s94":
            filename_only = os.path.basename(item['file_name'])
            data_model = FileDataModel()
            data_model.data_name = filename_only
            data_model.file_name = item['file_name']
            data_model.header_info = item['header_info']
            data_model.data = item['data']
            data_model.original_image = convert_data_to_greyscale_image(item['data'])
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
                self.data_for_analisys.append(data_model)
        self.notify_observers()

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
        # Input validation
        # if not isinstance(points, list) or not all(isinstance(row, list) for row in points):
        #     raise ValueError("Input points must be a list of lists.")

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