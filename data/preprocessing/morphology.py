# -*- coding: utf-8 -*-
"""
Morphology functions

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys
import numpy as np

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import cv2
from scipy import ndimage
from skimage.morphology import reconstruction
from skimage import img_as_float
from skimage.morphology import (disk, white_tophat, black_tophat, 
                                square, diamond, star)

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def Erosion(img, kernel_type="re", kernel_size=(5,5), iterations=1):
    """
    Perform binary erosion on an image using a specified kernel.

    Parameters:
    - img: Input image as a numpy array.
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Tuple specifying kernel size.
    - iterations: Number of erosion iterations.

    Returns:
    - eroded_image: Eroded image as a numpy array.
    """
    try:
        kernel = binary_kernel(kernel_type, kernel_size)
        eroded_image = cv2.erode(img, kernel, iterations)
        return eroded_image
    except Exception as e:
        logger.error(f"Error in Erosion: {e}")
        raise

def BinaryGreyscaleErosion(img, kernel_type="re", kernel_size=(3,3)):
    """
    Perform greyscale erosion on an image using a specified binary kernel.

    Parameters:
    - img: Input image as a numpy array.
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Tuple specifying kernel size.

    Returns:
    - eroded_image: Eroded image as a numpy array.
    """
    try:
        kernel = binary_kernel(kernel_type, kernel_size)
        eroded_image = ndimage.grey_erosion(img, footprint=kernel)
        return eroded_image
    except Exception as e:
        logger.error(f"Error in BinaryGreyscaleErosion: {e}")
        raise

def GaussianGreyscaleErosion(img, mask_size, sigma):
    """
    Perform greyscale erosion on an image using a Gaussian kernel.

    Parameters:
    - img: Input image as a numpy array.
    - mask_size: Size of the Gaussian mask.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - eroded_image_gaussian: Eroded image as a numpy array.
    """
    try:
        gm = gaussian_mask(mask_size, sigma)
        eroded_image_gaussian = ndimage.grey_erosion(img, structure=gm)
        return eroded_image_gaussian
    
    except Exception as e:
        logger.error(f"Error in GaussianGreyscaleErosion: {e}")
        raise

def BinaryGreyscaleDilation(img, kernel_type="re", kernel_size=(3,3)):
    """
    Perform greyscale dilation on an image using a specified binary kernel.

    Parameters:
    - img: Input image as a numpy array.
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Tuple specifying kernel size.

    Returns:
    - dilated_image: Dilated image as a numpy array.
    """
    try:
        kernel = binary_kernel(kernel_type, kernel_size)
        dilated_image = ndimage.grey_dilation(img, footprint=kernel)
        return dilated_image
    
    except Exception as e:
        logger.error(f"Error in BinaryGreyscaleDilation: {e}")
        raise

def GaussianGreyscaleDilation(img, mask_size, sigma):
    """
    Perform greyscale dilation on an image using a Gaussian kernel.

    Parameters:
    - img: Input image as a numpy array.
    - mask_size: Size of the Gaussian mask.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - dilated_image_gaussian: Dilated image as a numpy array.
    """
    try:
        gm = gaussian_mask(mask_size, sigma)
        dilated_image_gaussian = ndimage.grey_dilation(img, structure=gm)
        return dilated_image_gaussian
    
    except Exception as e:
        logger.error(f"Error in GaussianGreyscaleDilation: {e}")
        raise

def BinaryGreyscaleOpening(img, kernel_type="re", kernel_size=(3,3)):
    """
    Perform greyscale opening on an image using a specified binary kernel.

    Parameters:
    - img: Input image as a numpy array.
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Tuple specifying kernel size.

    Returns:
    - opened_image: Opened image as a numpy array.
    """
    try:
        kernel = binary_kernel(kernel_type, kernel_size)
        opened_image = ndimage.grey_opening(img, footprint=kernel)
        return opened_image
    
    except Exception as e:
        logger.error(f"Error in BinaryGreyscaleOpening: {e}")
        raise

def GaussianGreyscaleOpening(img, mask_size, sigma):
    """
    Perform greyscale opening on an image using a Gaussian kernel.

    Parameters:
    - img: Input image as a numpy array.
    - mask_size: Size of the Gaussian mask.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - opened_image_gaussian: Opened image as a numpy array.
    """
    try:
        gm = gaussian_mask(mask_size, sigma)
        opened_image_gaussian = ndimage.grey_opening(img, structure=gm)
        return opened_image_gaussian
    
    except Exception as e:
        logger.error(f"Error in GaussianGreyscaleOpening: {e}")
        raise

def BinaryGreyscaleClosing(img, kernel_type="re", kernel_size=(3,3)):
    """
    Perform greyscale closing on an image using a specified binary kernel.

    Parameters:
    - img: Input image as a numpy array.
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Tuple specifying kernel size.

    Returns:
    - closed_image: Closed image as a numpy array.
    """
    try:
        kernel = binary_kernel(kernel_type, kernel_size)
        closed_image = ndimage.grey_closing(img, footprint=kernel)
        return closed_image
    
    except Exception as e:
        logger.error(f"Error in BinaryGreyscaleClosing: {e}")
        raise

def GaussianGreyscaleClosing(img, mask_size, sigma):
    """
    Perform greyscale closing on an image using a Gaussian kernel.

    Parameters:
    - img: Input image as a numpy array.
    - mask_size: Size of the Gaussian mask.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - closed_image_gaussian: Closed image as a numpy array.
    """
    try:
        gm = gaussian_mask(mask_size, sigma)
        closed_image_gaussian = ndimage.grey_closing(img, structure=gm)
        return closed_image_gaussian
    
    except Exception as e:
        logger.error(f"Error in GaussianGreyscaleClosing: {e}")
        raise

def Propagation(img, type, marker_value):
    """
    Perform morphological propagation (dilation/erosion) on an image using reconstruction.

    Parameters:
    - img: Input image as a numpy array.
    - type: Type of propagation ("dilation" or "erosion").
    - marker_value: Value to use for the marker during propagation.

    Returns:
    - reconstructed_image: Image after morphological reconstruction.
    """
    try:
        marker = None
        img = img_as_float(img)
        if type == "dilation":
            marker = img - marker_value
            marker[marker < 0] = 0
        elif type == "erosion":
            marker = img + marker_value

        # Perform morphological reconstruction by dilation
        reconstructed_image = reconstruction(marker, img, method=type)

        return reconstructed_image
    
    except Exception as e:
        logger.error(f"Error in Propagation: {e}")
        raise

def WhiteTopHatTransformation(img, selem_type, selem_size):
    """
    Perform white top-hat transformation on an image.

    Parameters:
    - img: Input image as a numpy array.
    - selem_type: Type of structuring element ("disk", "square", "diamond", "star").
    - selem_size: Size of the structuring element.

    Returns:
    - leveled_image_normalized: Image after white top-hat transformation, normalized to 8-bit.
    """
    try:
        image = img_as_float(img) 
        selem = binary_selem(selem_type, selem_size)

        # Apply top-hat transformation
        tophat_image = white_tophat(image, selem)

        leveled_image_normalized = cv2.normalize(tophat_image, None, 0, 255, cv2.NORM_MINMAX)
        leveled_image_normalized = leveled_image_normalized.astype(np.uint8)

        return leveled_image_normalized
    
    except Exception as e:
        logger.error(f"Error in WhiteTopHatTransformation: {e}")
        raise

def BlackTopHatTransformation(img, selem_type, selem_size):
    """
    Perform black top-hat transformation on an image.

    Parameters:
    - img: Input image as a numpy array.
    - selem_type: Type of structuring element ("disk", "square", "diamond", "star").
    - selem_size: Size of the structuring element.

    Returns:
    - leveled_image_normalized: Image after black top-hat transformation, normalized to 8-bit.
    """
    try:
        image = img_as_float(img) 
        selem = binary_selem(selem_type, selem_size)

        # Apply top-hat transformation
        tophat_image = black_tophat(image, selem)

        leveled_image_normalized = cv2.normalize(tophat_image, None, 0, 255, cv2.NORM_MINMAX)
        leveled_image_normalized = leveled_image_normalized.astype(np.uint8)

        return leveled_image_normalized
    
    except Exception as e:
        logger.error(f"Error in BlackTopHatTransformation: {e}")
        raise

def binary_selem(selem_type, selem_size):
    """
    Create a binary structuring element for morphological operations.

    Parameters:
    - selem_type: Type of structuring element ("disk", "square", "diamond", "star").
    - selem_size: Size of the structuring element.

    Returns:
    - selem: Structuring element as a numpy array.
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

def binary_kernel(kernel_type, kernel_size):
    """
    Create a binary kernel for morphological operations.

    Parameters:
    - kernel_type: Type of kernel ("re", "el", "cr").
    - kernel_size: Size of the kernel.

    Returns:
    - kernel: Binary kernel as a numpy array.
    """
    try:
        kernel = None
        if kernel_type == "re":
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
        if kernel_type == "el":
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size,kernel_size))
        elif kernel_type == "cr":
            kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size,kernel_size))
        return kernel
    
    except Exception as e:
        logger.error(f"Error in binary_kernel: {e}")
        raise
    

def gaussian_kernel(size, sigma=1):
    """
    Generate a Gaussian kernel.

    Parameters:
    - size: Size of the kernel.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - kernel: Gaussian kernel as a numpy array.
    """
    try:
        ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
        xx, yy = np.meshgrid(ax, ax)
        kernel = np.exp(-0.5 * (np.square(xx) + np.square(yy)) / np.square(sigma))
        return kernel / np.sum(kernel)
    
    except Exception as e:
        logger.error(f"Error in gaussian_kernel: {e}")
        raise

def gaussian_mask(size, sigma):
    """
    Generate a Gaussian mask for morphological operations.

    Parameters:
    - size: Size of the mask.
    - sigma: Standard deviation of the Gaussian distribution.

    Returns:
    - gaussian_mask: Gaussian mask as a numpy array.
    """
    try:
        return gaussian_kernel(size, sigma)
    except Exception as e:
        logger.error(f"Error in gaussian_mask: {e}")
        raise