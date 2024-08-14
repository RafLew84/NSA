# -*- coding: utf-8 -*-
"""
Data model for STM files data

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from PIL import Image

from data.model.file_data_model import FileDataModel

import logging

logger = logging.getLogger(__name__)


# data_for_analisys = []

# def clear_data():
#     data_for_analisys.clear()

# def insert_data(file_ext, item):
#     if file_ext.lower() == "stp" or file_ext.lower() == "s94":
#         filename_only = os.path.basename(item['file_name'])
#         data_model = FileDataModel()
#         data_model.data_name = filename_only
#         data_model.file_name = item['file_name']
#         data_model.header_info = item['header_info']
#         data_model.data = item['data']
#         data_model.greyscale_image = convert_data_to_greyscale_image(item['data'])
#         data_for_analisys.append(data_model)
#     elif file_ext.lower() == "mpp":
#         filename_only = os.path.basename(item['file_name'])
#         for i, frame in enumerate(item['data'], start=1):
#             frame_name = f"frame {i}"
#             data_model = FileDataModel()
#             data_model.data_name = frame_name
#             data_model.file_name = item['file_name']
#             data_model.frame_number = i
#             data_model.header_info = item['header_info']
#             data_model.data = frame
#             data_model.greyscale_image = convert_data_to_greyscale_image(frame)
#             data_for_analisys.append(data_model)

# def convert_data_to_greyscale_image(points):
#     """
#     Create a grayscale image from input data.

#     Parameters:
#         points (list): List of lists containing the data points.

#     Returns:
#         PIL.Image.Image: The created grayscale image.

#     Raises:
#         ValueError: If points is not a list of lists.
#     """
#     try:
#         # Input validation
#         # if not isinstance(points, list) or not all(isinstance(row, list) for row in points):
#         #     raise ValueError("Input points must be a list of lists.")

#         # Create a new grayscale image
#         img = Image.new('L', (len(points[0]), len(points)))

#         # Normalize the values in data to the range [0, 255]
#         max_z = max(map(max, points))
#         min_z = min(map(min, points))
#         if max_z == min_z:
#             max_z += 1
#         for i in range(len(points)):
#             for j in range(len(points[i])):
#                 val = int(255 * (points[i][j] - min_z) / (max_z - min_z))
#                 img.putpixel((j, i), val)

#         return img
#     except ValueError as ve:
#         msg = f"ValueError in create_greyscale_image: {ve}"
#         logger.error(msg)
#         raise ValueError(msg)
#     except Exception as e:
#         logger.error(f"Error in create_greyscale_image: {e}")
#         raise