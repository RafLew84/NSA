# -*- coding: utf-8 -*-
"""
Functions for preprocessing

This module provides functions to apply various preprocessing techniques to images,
such as Gaussian blur, denoising, morphological operations, intensity adjustments, 
and more.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import cv2
import numpy as np
from PIL import Image

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

from data.preprocessing.smoothing import (
    GaussianBlur,
    GaussianFilter,
    LocalMedianFilter
)

from data.preprocessing.noise_reduction import (
    NlMeansDenois
)

from data.preprocessing.sharpening import (
    GaussianSharpening
)

from data.preprocessing.morphology import (
    Erosion,
    BinaryGreyscaleErosion,
    GaussianGreyscaleErosion,
    BinaryGreyscaleDilation,
    GaussianGreyscaleDilation,
    BinaryGreyscaleOpening,
    GaussianGreyscaleOpening,
    BinaryGreyscaleClosing,
    GaussianGreyscaleClosing,
    Propagation,
    BlackTopHatTransformation,
    WhiteTopHatTransformation
)

from data.preprocessing.intensity import (
    GammaAdjustment,
    ContrastStretching,
    AdaptiveEqualization
)

from data.preprocessing.leveling import (
    RegionLeveling,
    ThreePointLeveling,
    PolynomialLeveling,
    AdaptiveLeveling
)

def perform_gaussian_blur(params, img):
    """
    Apply Gaussian blur to an image.

    Args:
        params (dict): Parameters for Gaussian blur, should include 'sigmaX' and 'sigmaY'.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "GaussianBlur"
        result_image = GaussianBlur(
                img=np.array(img), 
                sigmaX=params['sigmaX'],
                sigmaY=params['sigmaY']
                )
        
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_non_local_denoising(params, img):
    """
    Apply Non-local Means denoising to an image.

    Args:
        params (dict): Parameters for Non-local Means denoising, should include 'h', 'searchWindowSize', and 'templateWindowSize'.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Non-local Mean Denoising"
        result_image = NlMeansDenois(
                img=np.array(img),
                h=params['h'],
                searchWinwowSize=params['searchWindowSize'],
                templateWindowSize=params['templateWindowSize']
                )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_gaussian_filter(params, img):
    """
    Apply a Gaussian filter to an image.

    Args:
        params (dict): Parameters for the Gaussian filter, should include 'sigma'.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "GaussianFilter"
        result_image = GaussianFilter(
                img=np.array(img),
                sigma=params['sigma']
            )
        
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_erosion(params, img):
    """
    Apply a Erosion to an image.

    Args:
        params (dict): Parameters for the Erosion.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Erosion"
        result_image = Erosion(
                img=np.array(img),
                kernel_type=params['kernel_type'],
                kernel_size=params['kernel_size'],
                iterations=params['iterations']
            )
        
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_greyscale_erosion(params, img):
    """
    Apply binary greyscale erosion to an image.

    Args:
        params (dict): Parameters for the binary greyscale erosion.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Greyscale Erosion"
        result_image = BinaryGreyscaleErosion(
            img=np.array(img),
            kernel_type=params['kernel_type'],
            kernel_size=params['kernel_size']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_gaussian_greyscale_erosion(params, img):
    """
    Apply Gaussian greyscale erosion to an image.

    Args:
        params (dict): Parameters for the Gaussian greyscale erosion.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gaussian Greyscale Erosion"
        result_image = GaussianGreyscaleErosion(
            img=np.array(img),
            mask_size=params['mask_size'],
            sigma=params['sigma']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_greyscale_dilation(params, img):
    """
    Apply binary greyscale dilation to an image.

    Args:
        params (dict): Parameters for the binary greyscale dilation.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Greyscale Dilation"
        result_image = BinaryGreyscaleDilation(
            img=np.array(img),
            kernel_type=params['kernel_type'],
            kernel_size=params['kernel_size']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_gaussian_greyscale_dilation(params, img):
    """
    Apply Gaussian greyscale dilation to an image.

    Args:
        params (dict): Parameters for the Gaussian greyscale dilation.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gaussian Greyscale Dilation"
        result_image = GaussianGreyscaleDilation(
            img=np.array(img),
            mask_size=params['mask_size'],
            sigma=params['sigma']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_binary_greyscale_opening(params, img):
    """
    Apply Binary greyscale opening to an image.

    Args:
        params (dict): Parameters for the Binary greyscale opening.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Greyscale Opening"
        result_image = BinaryGreyscaleOpening(
            img=np.array(img),
            kernel_type=params['kernel_type'],
            kernel_size=params['kernel_size']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img

def perform_gaussian_greyscale_opening(params, img):
    """
    Apply Gaussian greyscale openig to an image.

    Args:
        params (dict): Parameters for the Gaussian greyscale opening.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gaussian Greyscale Opening"
        result_image = GaussianGreyscaleOpening(
            img=np.array(img),
            mask_size=params['mask_size'],
            sigma=params['sigma']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
def perform_binary_greyscale_closing(params, img):
    """
    Apply Binary greyscale closing to an image.

    Args:
        params (dict): Parameters for the Binary greyscale closing.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Binary Greyscale Closing"
        result_image = BinaryGreyscaleClosing(
            img=np.array(img),
            kernel_type=params['kernel_type'],
            kernel_size=params['kernel_size']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img    

def perform_gaussian_greyscale_closing(params, img):
    """
    Apply Gaussian greyscale closing to an image.

    Args:
        params (dict): Parameters for the Gaussian greyscale closing.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gaussian Greyscale Closing"
        result_image = GaussianGreyscaleClosing(
            img=np.array(img),
            mask_size=params['mask_size'],
            sigma=params['sigma']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_gamma_adjustment(params, img):
    """
    Apply Gamma adjustment to an image.

    Args:
        params (dict): Parameters for the gamma adjustment.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gamma Adjustment"
        result_image = GammaAdjustment(
            img=np.array(img),
            gamma=params['gamma']
        )

        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_contrast_stretching(params, img):
    """
    Apply constrast stretching to an image.

    Args:
        params (dict): Parameters for the contrast stretching.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Contrast Stretching"
        result_image = ContrastStretching(
            img=np.array(img),
            min=params['min'],
            max=params['max']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_adaptive_equalization(params, img):
    """
    Apply Adaptive equalization to an image.

    Args:
        params (dict): Parameters for the adaptive equalization.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Adaptive Equalization"
        result_image = AdaptiveEqualization(
            img=np.array(img),
            limit=params['limit']
        )
        image_uint8 = (result_image * 255).astype(np.uint8)
        return process_name, Image.fromarray(image_uint8)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_region_leveling(params, img):
    """
    Apply Region leveling to an image.

    Args:
        params (dict): Parameters for the region leveling.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Region Leveling"
        result_image = RegionLeveling(img)
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_three_point_leveling(params, img):
    """
    Apply three point leveling dilation to an image.

    Args:
        params (dict): Parameters for the three point leveling.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Three Point Leveling"
        result_image = ThreePointLeveling(img)
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_gaussian_sharpening(params, img):
    """
    Apply Gaussian sharpening to an image.

    Args:
        params (dict): Parameters for the Gaussian sharpening.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Gaussian Sharpening"
        result_image = GaussianSharpening(
            img=np.array(img),
            radius=params['radius'],
            amount=params['amount']
        )
        image_uint8 = (result_image * 255).astype(np.uint8)
        return process_name, Image.fromarray(image_uint8)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_propagation(params, img):
    """
    Apply propagation to an image.

    Args:
        params (dict): Parameters for the propagation.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Propagation"
        result_image = Propagation(
            img=np.array(img),
            type=params['type'],
            marker_value=params['marker_value']
        )
        image_uint8 = (result_image * 255).astype(np.uint8)
        return process_name, Image.fromarray(image_uint8)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_polynomial_leveling(params, img):
    """
    Apply polynomial leveling to an image.

    Args:
        params (dict): Parameters for the polynomial leveling.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Polynomial Leveling"
        result_image = PolynomialLeveling(
            img=np.array(img),
            order=params['order']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_adaptive_leveling(params, img):
    """
    Apply adaptive leveling to an image.

    Args:
        params (dict): Parameters for the adaptive lavaling.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Adaptive Leveling"
        result_image = AdaptiveLeveling(
            img=np.array(img),
            disk_size=params['disk_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_local_median_filter(params, img):
    """
    Apply local median filter to an image.

    Args:
        params (dict): Parameters for the local median filter.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Local Median Filter"
        result_image = LocalMedianFilter(
            image=np.array(img),
            size=params['size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_white_top_hat(params, img):
    """
    Apply white top hat to an image.

    Args:
        params (dict): Parameters for the white top hat.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "White Top Hat"
        result_image = WhiteTopHatTransformation(
            img=np.array(img),
            selem_type=params['selem_type'],
            selem_size=params['selem_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img
    
def perform_black_top_hat(params, img):
    """
    Apply black top hat to an image.

    Args:
        params (dict): Parameters for the black top hat.
        img (PIL.Image.Image): The input image.

    Returns:
        tuple: Process name and the resulting image.
    """
    try:
        process_name = "Black Top Hat"
        result_image = BlackTopHatTransformation(
            img=np.array(img),
            selem_type=params['selem_type'],
            selem_size=params['selem_size']
        )
        return process_name, Image.fromarray(result_image)
    
    except Exception as e:
        logger.error(f"Error in {process_name}: {e}")
        return process_name, img