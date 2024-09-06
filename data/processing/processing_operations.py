# -*- coding: utf-8 -*-
"""
Functions for preprocessing

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import numpy as np
from PIL import Image

from data.processing.thresholding import (
    OtsuThreshold,
    LocalThreshold,
    NiblackThreshold,
    SauvolaThreshold,
    YenThreshold,
    IsodataThreshold,
    BinaryThreshold
)

from data.processing.morphology import (
    BinaryErosion,
    BinaryDilation,
    BinaryClosing,
    BinaryOpening,
    RemoveSmallHoles,
    RemoveSmallObjects
)

from data.processing.image_edit import (
    ImageEditRemoveWhite
)

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def perform_otsu_threshold(params, img):
    """
    Apply Otsu Threshold to an image.

    Args:
        params (dict): Parameters for Otsu threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Otsu Threshold"
        result_image = OtsuThreshold(
                img=np.array(img)
        )
        
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_local_threshold(params, img):
    """
    Apply local threshold to an image.

    Args:
        params (dict): Parameters for local threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Local Threshold"
        result_image = LocalThreshold(
            img=np.array(img),
            method=params['method'],
            block_size=params['block_size'],
            offset=params['offset']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_niblack_threshold(params, img):
    """
    Apply Niblack threshold to an image.

    Args:
        params (dict): Parameters for Niblack threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Niblack Threshold"
        result_image = NiblackThreshold(
            img=np.array(img),
            window_size=params['window_size'],
            k=params['k']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_sauvola_threshold(params, img):
    """
    Apply Sauvola threshold to an image.

    Args:
        params (dict): Parameters for Sauvola threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Sauvola Threshold"
        result_image = SauvolaThreshold(
            img=np.array(img),
            window_size=params['window_size'],
            k=params['k'],
            r=params['r']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_yen_threshold(params, img):
    """
    Apply Yen threshold to an image.

    Args:
        params (dict): Parameters for Yen threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Yen Threshold"
        result_image = YenThreshold(
            img=np.array(img)
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_isodata_threshold(params, img):
    """
    Apply ISODATA threshold to an image.

    Args:
        params (dict): Parameters for ISODATA threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "ISODATA Threshold"
        result_image = IsodataThreshold(
            img=np.array(img)
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_erosion(params, img):
    """
    Apply binary threshold to an image.

    Args:
        params (dict): Parameters for binary threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Erosion"
        result_image = BinaryErosion(
            img=np.array(img),
            footprint_type=params['footprint_type'],
            footprint_size=params['footprint_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_dilation(params, img):
    """
    Apply binary dilation to an image.

    Args:
        params (dict): Parameters for binary dilation.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Dilation"
        result_image = BinaryDilation(
            img=np.array(img),
            footprint_type=params['footprint_type'],
            footprint_size=params['footprint_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_opening(params, img):
    """
    Apply binary opening to an image.

    Args:
        params (dict): Parameters for binary opening.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Opening"
        result_image = BinaryOpening(
            img=np.array(img),
            footprint_type=params['footprint_type'],
            footprint_size=params['footprint_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_closing(params, img):
    """
    Apply binary closing to an image.

    Args:
        params (dict): Parameters for binary closing.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Closing"
        result_image = BinaryClosing(
            img=np.array(img),
            footprint_type=params['footprint_type'],
            footprint_size=params['footprint_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_removing_small_holes(params, img):
    """
    Apply remove small holes to an image.

    Args:
        params (dict): Parameters for remove small holes.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Remove Small Holes"
        result_image = RemoveSmallHoles(
            img=np.array(img),
            area_threshold=params['area_threshold'],
            connectivity=params['connectivity']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_removing_small_objects(params, img):
    """
    Apply remove small objects to an image.

    Args:
        params (dict): Parameters for remove small objects.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Remove Small Objects"
        result_image = RemoveSmallObjects(
            img=np.array(img),
            min_size=params['min_size'],
            connectivity=params['connectivity']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_manual_white_remove(params, img):
    """
    Apply manual remove white areas to an image.

    Args:
        params (dict): Parameters for remove white areas.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Manual Edit"
        result_image = ImageEditRemoveWhite(np.array(img))
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_threshold(params, img):
    """
    Apply binary threshold areas to an image.

    Args:
        params (dict): Parameters for binary threshold.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Threshold"
        result_image = BinaryThreshold(
            img=np.array(img),
            threshold=params['threshold']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img