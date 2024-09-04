# -*- coding: utf-8 -*-
"""
Intensity functions

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys
import logging


sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

logger = logging.getLogger(__name__)
# Configure logging for the entire application (if not configured elsewhere)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

import numpy as np
from skimage import exposure

def GammaAdjustment(img, gamma):
    """
    Apply gamma correction to an image.

    Args:
        img (np.ndarray): Input image array.
        gamma (float): Gamma value for correction. Greater than 1 darkens the image, less than 1 lightens it.

    Returns:
        np.ndarray: Gamma-corrected image array.
    """
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("img must be a numpy ndarray")
        if not isinstance(gamma, (int, float)) or gamma <= 0:
            raise ValueError("gamma must be a positive number")

        return exposure.adjust_gamma(img, gamma)
    
    except (TypeError, ValueError) as e:
        logger.error(f"Error in gamma_adjustment: {e}")
        raise

def ContrastStretching(img, min, max):
    """
    Apply contrast stretching to an image.

    Args:
        img (np.ndarray): Input image array.
        min (float): Minimum percentile for contrast stretching.
        max (float): Maximum percentile for contrast stretching.

    Returns:
        np.ndarray: Contrast-stretched image array.
    """
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("img must be a numpy ndarray")
        if not (0 <= min < max <= 100):
            raise ValueError("min_percent and max_percent must be between 0 and 100 and min_percent < max_percent")

        p_min, p_max = np.percentile(img, (min, max))
        return exposure.rescale_intensity(img, in_range=(p_min, p_max))
    
    except (TypeError, ValueError) as e:
        logger.error(f"Error in contrast_stretching: {e}")
        raise

def AdaptiveEqualization(img, limit):
    """
    Apply adaptive histogram equalization to an image.

    Args:
        img (np.ndarray): Input image array.
        clip_limit (float, optional): Threshold for contrast limiting. Default is 0.01.

    Returns:
        np.ndarray: Adaptive histogram equalized image array.
    """
    try:
        if not isinstance(img, np.ndarray):
            raise TypeError("img must be a numpy ndarray")
        if not isinstance(limit, (int, float)) or limit <= 0:
            raise ValueError("clip_limit must be a positive number")

        return exposure.equalize_adapthist(img, clip_limit=limit)
    
    except (TypeError, ValueError) as e:
        logger.error(f"Error in adaptive_equalization: {e}")
        raise