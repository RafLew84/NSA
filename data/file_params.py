import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import logging

logger = logging.getLogger(__name__)

import re

def calculate_pixel_to_nm_coefficients(header_info, file_ext):
    if not isinstance(header_info, dict):
        error_msg = "calculate_pixel_to_nm_coefficient: Header information must be provided as a dictionary."
        logger.error(error_msg)
        raise TypeError(error_msg)
    
    x_nm = None
    y_nm = None

    x_px = None
    y_px = None
    
    try:
        x_nm, y_nm, x_px, y_px = get_image_sizes(header_info, file_ext)
        
        nm_per_pixel_x = x_nm / x_px
        nm_per_pixel_y = y_nm / y_px
            
        return nm_per_pixel_x, nm_per_pixel_y
    except KeyError as e:
        error_msg = f"Header information for file extension '{file_ext}' is missing: {e}"
        logger.error(error_msg)
        raise e
    
def calculate_pixels_from_nm(nm, coeff):
    pixels = nm / coeff
    return int(pixels)


def get_image_sizes(header_info, file_ext):
    if file_ext.lower() == "s94":
        x_nm = header_info['x_size']
        y_nm = header_info['y_size']

        x_px = header_info['x_points']
        y_px = header_info['y_points']

    elif file_ext.lower() == "stp":
        x_nm = extract_number_from_string(header_info['X Amplitude'])
        y_nm = extract_number_from_string(header_info['Y Amplitude'])

        x_px = float(header_info['Number of columns'])
        y_px = float(header_info['Number of rows'])

    elif file_ext.lower() == "mpp":
        x_nm = extract_number_from_string(header_info.get('Control', {}).get('X Amplitude', ''))
        y_nm = extract_number_from_string(header_info.get('Control', {}).get('Y Amplitude', ''))

        x_px = float(header_info.get('General Info', {}).get('Number of columns', ''))
        y_px = float(header_info.get('General Info', {}).get('Number of rows', ''))
    return x_nm,y_nm,x_px,y_px
    
def calculate_avg_nm_per_px(header_info, file_ext):
    #x_nm, y_nm, x_px, y_px = get_image_sizes(header_info, file_ext)
    x_coeff, y_coeff = calculate_pixel_to_nm_coefficients(header_info, file_ext)
    avg_nm_per_pixel = x_coeff * y_coeff

    return avg_nm_per_pixel

def extract_number_from_string(string):
    # Use regular expression to match numerical part
    match = re.search(r'(\d+\.?\d*)', string)
    if match:
        return float(match.group())  # Convert matched string to float
    else:
        return None  # Return None if no match found