# -*- coding: utf-8 -*-
"""
Stores default values for preprocess tab.

This script defines default parameter values for various image preprocessing methods,
which can be used in a GUI or an application for image processing.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os
import sys

# Modify the Python path to include the parent directory of the script, allowing for module imports.
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

# Dictionary storing default parameters for different preprocessing techniques.
# Each key represents a preprocessing method, and its corresponding value is a dictionary
# containing the relevant parameters and their default values.
preprocess_params = {
    "Gaussian Blur": {"sigmaX": 5, "sigmaY": 5},  # Gaussian blur with specified sigma values for X and Y axes.
    
    "Non-local Mean Denoising": {
        "h": 3,  # Filter strength for noise removal.
        "searchWindowSize": 21,  # Size of the search window.
        "templateWindowSize": 7  # Size of the template patch.
    },
    
    "GaussianFilter": {"sigma": 4},  # Gaussian filter with specified sigma.
    
    "Erosion": {
        "kernel_type": "re",  # Type of kernel (rectangular).
        "kernel_size": 5,     # Size of the kernel.
        "iterations": 1       # Number of iterations for erosion.
    },
    
    "Binary Greyscale Erosion": {
        "kernel_type": "re",  # Type of kernel (rectangular).
        "kernel_size": 3      # Size of the kernel for binary greyscale erosion.
    },

    "Binary Greyscale Dilation": {
        "kernel_type": "re",  # Type of kernel (rectangular).
        "kernel_size": 3      # Size of the kernel for binary greyscale dilation.
    },

    "Binary Greyscale Opening": {
        "kernel_type": "re",  # Type of kernel (rectangular).
        "kernel_size": 3      # Size of the kernel for binary greyscale opening.
    },
    
    # Gaussian Greyscale Opening parameters can be added as needed.
    # "Gaussian Greyscale Opening": {"mask_size": 3, "sigma": 1.0},

    "Binary Greyscale Closing": {
        "kernel_type": "re",  # Type of kernel (rectangular).
        "kernel_size": 3      # Size of the kernel for binary greyscale closing.
    },

    "Gamma Adjustment": {"gamma": 3.5},  # Gamma correction with specified gamma value.
    
    "Contrast Stretching": {
        "min": 2,  # Minimum percentile for contrast stretching.
        "max": 98  # Maximum percentile for contrast stretching.
    },
    
    "Adaptive Equalization": {"limit": 0.03},  # Limit for contrast clipping in adaptive equalization.
    
    "Region Leveling": {},  # No parameters defined, uses default settings.
    
    "Three Point Leveling": {},  # No parameters defined, uses default settings.
    
    "Gaussian Sharpening": {
        "radius": 1.0,  # Radius for Gaussian sharpening.
        "amount": 1.0   # Amount of sharpening to apply.
    },
    
    "Propagation": {
        "type": "dilation",     # Type of propagation (dilation).
        "marker_value": 0.3     # Marker value used in the propagation process.
    },
    
    "Polynomial Leveling": {"order": 3},  # Polynomial leveling with specified order.
    
    "Adaptive Leveling": {"disk_size": 5},  # Disk size for adaptive leveling.
    
    "Local Median Filter": {"size": 5},  # Size of the filter for local median filtering.
    
    "White Top Hat": {
        "selem_type": "disk",  # Type of structuring element (disk).
        "selem_size": 12       # Size of the structuring element for white top-hat transformation.
    },
    
    "Black Top Hat": {
        "selem_type": "disk",  # Type of structuring element (disk).
        "selem_size": 12       # Size of the structuring element for black top-hat transformation.
    }
}