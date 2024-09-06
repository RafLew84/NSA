# -*- coding: utf-8 -*-
"""
Morphology functions for binary images.

This module provides binary morphological operations such as erosion, dilation, opening, closing, and functions for removing small holes and objects.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from skimage.morphology import (disk, binary_erosion, binary_closing, binary_dilation, binary_opening,
                                square, diamond, star, remove_small_holes, remove_small_objects)

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def BinaryErosion(img, footprint_type, footprint_size):
    """
    Apply binary erosion to an image.

    Args:
        img (numpy.ndarray): Input binary image.
        footprint_type (str): Type of the structural element ('disk', 'square', 'diamond', 'star').
        footprint_size (int): Size of the structural element.

    Returns:
        numpy.ndarray: Eroded binary image.
    """
    try:
        footprint = binary_selem(footprint_type, footprint_size)
        eroded_image = binary_erosion(img, footprint=footprint)

        return eroded_image
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def BinaryDilation(img, footprint_type, footprint_size):
    """
    Apply binary dilation to an image.

    Args:
        img (numpy.ndarray): Input binary image.
        footprint_type (str): Type of the structural element ('disk', 'square', 'diamond', 'star').
        footprint_size (int): Size of the structural element.

    Returns:
        numpy.ndarray: Dilated binary image.
    """
    try:
        footprint = binary_selem(footprint_type, footprint_size)
        dilated_image = binary_dilation(img, footprint=footprint)

        return dilated_image
    
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def BinaryOpening(img, footprint_type, footprint_size):
    """
    Apply binary opening to an image.

    Args:
        img (numpy.ndarray): Input binary image.
        footprint_type (str): Type of the structural element ('disk', 'square', 'diamond', 'star').
        footprint_size (int): Size of the structural element.

    Returns:
        numpy.ndarray: Opened binary image.
    """
    try:
        footprint = binary_selem(footprint_type, footprint_size)
        opened_image = binary_opening(img, footprint=footprint)

        return opened_image

    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def BinaryClosing(img, footprint_type, footprint_size):
    """
    Apply binary closing to an image.

    Args:
        img (numpy.ndarray): Input binary image.
        footprint_type (str): Type of the structural element ('disk', 'square', 'diamond', 'star').
        footprint_size (int): Size of the structural element.

    Returns:
        numpy.ndarray: Closed binary image.
    """
    try:
        footprint = binary_selem(footprint_type, footprint_size)
        closed_image = binary_closing(img, footprint=footprint)

        return closed_image
    
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def RemoveSmallHoles(img, area_threshold,connectivity):
    """
    Remove small holes from a binary image.

    Args:
        img (numpy.ndarray): Input binary image.
        area_threshold (int): The maximum area of holes to remove.
        connectivity (int): The connectivity defining the neighborhood (e.g., 1 or 2).

    Returns:
        numpy.ndarray: Binary image with small holes removed.
    """
    try:
        result_image = remove_small_holes(img, area_threshold, connectivity)
        return result_image
    
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def RemoveSmallObjects(img, min_size,connectivity):
    """
    Remove small objects from a binary image.

    Args:
        img (numpy.ndarray): Input binary image.
        min_size (int): Minimum size of objects to keep.
        connectivity (int): The connectivity defining the neighborhood (e.g., 1 or 2).

    Returns:
        numpy.ndarray: Binary image with small objects removed.
    """
    try:
        result_image = remove_small_objects(img, min_size, connectivity)
        return result_image
    
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise


def binary_selem(selem_type, selem_size):
    """
    Generate a structural element (footprint) for binary morphological operations.

    Args:
        selem_type (str): The type of the structural element ('disk', 'square', 'diamond', 'star').
        selem_size (int): The size of the structural element.

    Returns:
        numpy.ndarray: The structural element for morphology operations.
    """
    try:
        selem = None
        if selem_type == "disk":
            selem = disk(selem_size)
        elif selem_type == "square":
            selem = square(selem_size)
        elif selem_type == "diamond":
            selem = diamond(selem_size)
        elif selem_type == "star":
            selem = star(selem_size)
        else:
            raise ValueError(f"Invalid selem_type: {selem_type}")
        
        return selem
    
    except Exception as e:
        logger.error(f"Error in binary_selem: {e}")
        raise