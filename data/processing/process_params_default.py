# -*- coding: utf-8 -*-
"""
Stores default values for preprocess tab.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

# Dictionary storing default parameters for different processing techniques.
# Each key represents a preprocessing method, and its corresponding value is a dictionary
# containing the relevant parameters and their default values.
process_params = {
    "Binary Erosion": {
        "footprint_type": "disk",  # Type of the footprint (e.g., disk) used for erosion.
        "footprint_size": 2        # Size of the footprint used for erosion.
    },
    
    "Binary Dilation": {
        "footprint_type": "disk",  # Type of the footprint (e.g., disk) used for dilation.
        "footprint_size": 2        # Size of the footprint used for dilation.
    },
    
    "Binary Opening": {
        "footprint_type": "disk",  # Type of the footprint (e.g., disk) used for opening (erosion followed by dilation).
        "footprint_size": 2        # Size of the footprint used for opening.
    },
    
    "Binary Closing": {
        "footprint_type": "disk",  # Type of the footprint (e.g., disk) used for closing (dilation followed by erosion).
        "footprint_size": 2        # Size of the footprint used for closing.
    },
    
    "Remove Small Holes": {
        "area_threshold": 64,      # Minimum area of small holes to be removed.
        "connectivity": 1          # Connectivity defining the neighborhood (e.g., 4 or 8 connectivity).
    },
    
    "Remove Small Objects": {
        "min_size": 64,            # Minimum size of small objects to be removed.
        "connectivity": 1          # Connectivity defining the neighborhood (e.g., 4 or 8 connectivity).
    },
    
    "Manual Erase": {
        # No specific parameters required for manual erase operations.
    }
}

# Parameters for thresholding methods
threshold_params = {
    "Otsu Threshold": {
        # No specific parameters required, uses Otsu's method for automatic thresholding.
    },
    
    "Local Threshold": {
        "method": "gaussian",  # Method for local thresholding (e.g., Gaussian).
        "block_size": 3,       # Size of the neighborhood used for threshold calculation.
        "offset": 10           # Constant subtracted from the mean or weighted mean.
    },
    
    "Niblack Threshold": {
        "window_size": 5,      # Size of the window used for calculating the local threshold.
        "k": 0.8               # Tuning parameter that controls the threshold level.
    },
    
    "Sauvola Threshold": {
        "window_size": 5,      # Size of the window used for calculating the local threshold.
        "k": 0.8,              # Tuning parameter that controls the threshold level.
        "r": 128               # Dynamic range of standard deviation used in the Sauvola method.
    },
    
    "Yen Threshold": {
        # No specific parameters required, uses Yen's method for thresholding.
    },
    
    "ISODATA Threshold": {
        # No specific parameters required, uses ISODATA method for thresholding.
    },
    
    "Binary Threshold": {
        "threshold": 127       # Threshold value for binary thresholding.
    }
}