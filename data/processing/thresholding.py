# -*- coding: utf-8 -*-
"""
Functions for image processing

This module provides various image thresholding techniques using OpenCV and scikit-image.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import cv2

from skimage.filters import (
    threshold_otsu,
    threshold_local,
    threshold_multiotsu,
    threshold_niblack, 
    threshold_sauvola,
    threshold_yen,
    threshold_isodata
)

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def OtsuThreshold(img):
    """
    Applies Otsu's thresholding method to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.

    Returns:
        numpy.ndarray: Binary image after applying Otsu's threshold.
    """
    try:
        thresh = threshold_otsu(img)
        threshold_image = img > thresh

        return threshold_image
    
    except Exception as e:
        logger.error(f"OtsuThreshold error: {e}")
        raise

def LocalThreshold(img, method, block_size, offset):
    """
    Applies local (adaptive) thresholding to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.
        method (str): Method for calculating local threshold (e.g., 'gaussian').
        block_size (int): Size of the block used to calculate the threshold.
        offset (float): Constant subtracted from the mean or weighted mean.

    Returns:
        numpy.ndarray: Binary image after applying local threshold.
    """
    try:
        threshold_image = img < threshold_local(
            image=img, 
            method=method, 
            block_size=block_size, 
            offset=offset
            )

        return threshold_image
    
    except Exception as e:
        logger.error(f"LocalThreshold error: {e}")
        raise

def NiblackThreshold(img, window_size, k):
    """
    Applies Niblack's thresholding method to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.
        window_size (int): Size of the window used to calculate the local mean.
        k (float): Tuning parameter to adjust the threshold.

    Returns:
        numpy.ndarray: Binary image after applying Niblack's threshold.
    """
    try:
        threshold_image = img > threshold_niblack(img, window_size=window_size, k=k)

        return threshold_image
    
    except Exception as e:
        logger.error(f"NiblackThreshold error: {e}")
        raise

def SauvolaThreshold(img, window_size, k, r):
    """
    Applies Sauvola's thresholding method to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.
        window_size (int): Size of the window used to calculate the local mean.
        k (float): Tuning parameter to adjust the threshold.
        r (float): Dynamic range of standard deviation.

    Returns:
        numpy.ndarray: Binary image after applying Sauvola's threshold.
    """
    try:
        threshold_image = img < threshold_sauvola(img, window_size=window_size, k=k, r=r)

        return threshold_image
    
    except Exception as e:
        logger.error(f"SauvolaThreshold error: {e}")
        raise

def YenThreshold(img):
    """
    Applies Yen's thresholding method to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.

    Returns:
        numpy.ndarray: Binary image after applying Yen's threshold.
    """
    try:
        thresh = threshold_yen(img)
        threshold_image = img > thresh

        return threshold_image
    
    except Exception as e:
        logger.error(f"YenThreshold error: {e}")
        raise

def IsodataThreshold(img):
    """
    Applies ISODATA thresholding method to the input image.

    Args:
        img (numpy.ndarray): Grayscale input image.

    Returns:
        numpy.ndarray: Binary image after applying ISODATA threshold.
    """
    try:
        thresh = threshold_isodata(img)
        threshold_image = img > thresh

        return threshold_image
    
    except Exception as e:
        logger.error(f"IsodataThreshold error: {e}")
        raise

def BinaryThreshold(img, threshold):
    """
    Applies binary thresholding using a fixed threshold value.

    Args:
        img (numpy.ndarray): Grayscale input image.
        threshold (int): Threshold value to binarize the image.

    Returns:
        numpy.ndarray: Binary image after applying the fixed threshold.
    """
    try:
        _, binary_image = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
        return binary_image
    
    except Exception as e:
        logger.error(f"BinaryThreshold error: {e}")
        raise
