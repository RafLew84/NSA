# -*- coding: utf-8 -*-
"""
Smoothing functions

This module provides functions to apply smoothing techniques to images,
such as Gaussian sharpening.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import cv2
from skimage.filters import unsharp_mask


import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def GaussianSharpening(img, radius=1.0, amount=1.0):
    """
    Apply Gaussian sharpening to an image using unsharp masking.

    Args:
        img (numpy.ndarray): The input image as a NumPy array.
        radius (float): The radius of the Gaussian blur used in the unsharp mask.
        amount (float): The amount by which the unsharp mask is applied.

    Returns:
        numpy.ndarray: The sharpened image.
    """
    try:
        # Apply unsharp masking
        sharpened_image = unsharp_mask(img, radius=radius, amount=amount)

        return sharpened_image
    
    except Exception as e:
        logger.error(f"Error in GaussianSharpening: {e}")
        return img  # Return the original image in case of an error