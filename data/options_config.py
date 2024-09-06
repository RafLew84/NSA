# -*- coding: utf-8 -*-
"""
Configuration options for preprocessing and processing image data.

This module contains configuration settings for various preprocessing and processing
operations applied to image data. It includes default parameter values, options for
UI elements (like sliders and radio buttons), and mappings of operations to their
respective functions.

Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.preprocessing.preprocess_params_default import preprocess_params
from data.processing.process_params_default import process_params, threshold_params

from data.preprocessing.preprocessing_operations import (
    perform_gaussian_blur,
    perform_gaussian_filter,
    perform_non_local_denoising,
    perform_erosion,
    perform_binary_greyscale_erosion,
    perform_binary_greyscale_dilation,
    perform_binary_greyscale_opening,
    perform_binary_greyscale_closing,
    perform_gamma_adjustment,
    perform_contrast_stretching,
    perform_adaptive_equalization,
    perform_region_leveling,
    perform_three_point_leveling,
    perform_gaussian_sharpening,
    perform_propagation,
    perform_polynomial_leveling,
    perform_adaptive_leveling,
    perform_local_median_filter,
    perform_black_top_hat,
    perform_white_top_hat
)

from data.processing.processing_operations import (
    perform_otsu_threshold,
    perform_local_threshold,
    perform_niblack_threshold,
    perform_sauvola_threshold,
    perform_yen_threshold,
    perform_isodata_threshold,
    perform_binary_erosion,
    perform_binary_dilation,
    perform_binary_opening,
    perform_binary_closing,
    perform_removing_small_holes,
    perform_removing_small_objects,
    perform_manual_white_remove,
    perform_binary_threshold
)

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

options_config = {
    "GaussianFilter": {
        "label_text": "sigma",
        "slider_config": {"from_": 0.1, "to": 4.0, "resolution": 0.05, "value": preprocess_params["GaussianFilter"]["sigma"]}
    },
    "Gamma Adjustment": {
        "label_text": "gamma",
        "slider_config": {"from_": 0.1, "to": 10.0, "resolution": 0.05, "value": preprocess_params["Gamma Adjustment"]["gamma"]}
    },
    "Adaptive Equalization": {
        "label_text": "limit",
        "slider_config": {"from_": 0.01, "to": 0.20, "resolution": 0.005, "value": preprocess_params["Adaptive Equalization"]["limit"]}
    },
    "Contrast Stretching": {
        "labels": [("min", preprocess_params["Contrast Stretching"]["min"]), ("max", preprocess_params["Contrast Stretching"]["max"])],
        "sliders": [
            {"from_": 1, "to": 99, "resolution": 1, "value": preprocess_params["Contrast Stretching"]["min"]},
            {"from_": 1, "to": 99, "resolution": 1, "value": preprocess_params["Contrast Stretching"]["max"]}
        ]
    },
    "Gaussian Blur": {
        "labels": [("sigmaY", preprocess_params["Gaussian Blur"]["sigmaY"]), ("sigmaX", preprocess_params["Gaussian Blur"]["sigmaX"])],
        "sliders": [
            {"from_": 3, "to": 21, "resolution": 2, "value": preprocess_params["Gaussian Blur"]["sigmaY"]},
            {"from_": 3, "to": 21, "resolution": 2, "value": preprocess_params["Gaussian Blur"]["sigmaX"]}
        ]
    },
    "Non-local Mean Denoising": {
        "labels": [
            ("h", preprocess_params["Non-local Mean Denoising"]["h"]),
            ("Template Window Size", preprocess_params["Non-local Mean Denoising"]["templateWindowSize"]),
            ("Search Window Size", preprocess_params["Non-local Mean Denoising"]["searchWindowSize"])
        ],
        "sliders": [
            {"from_": 0.1, "to": 10.0, "resolution": 0.1, "value": preprocess_params["Non-local Mean Denoising"]["h"]},
            {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Non-local Mean Denoising"]["templateWindowSize"]},
            {"from_": 3, "to": 51, "resolution": 1, "value": preprocess_params["Non-local Mean Denoising"]["searchWindowSize"]}
        ]
    },
    "Erosion": {
        "radio_buttons": [("Rectangle", "re"), ("Ellipse", "el"), ("Cross", "cr")],
        "labels": [("Kernel Size", preprocess_params["Erosion"]["kernel_size"]), ("Iterations", preprocess_params["Erosion"]["iterations"])],
        "sliders": [
            {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Erosion"]["kernel_size"]},
            {"from_": 1, "to": 5, "resolution": 1, "value": preprocess_params["Erosion"]["iterations"]}
        ]
    },
    "Propagation": {
        "radio_buttons": [("Dilation", "dilation"), ("Erosion", "erosion")],
        "labels": [("Margker value", preprocess_params["Propagation"]["marker_value"])],
        "sliders": [
            {"from_": 0.05, "to": 0.95, "resolution": 0.05, "value": preprocess_params["Propagation"]["marker_value"]}
        ]
    },
    "Polynomial Leveling": {
        "labels": [("Order", preprocess_params["Polynomial Leveling"]["order"])],
        "sliders": [
            {"from_": 2, "to": 20, "resolution": 1, "value": preprocess_params["Polynomial Leveling"]["order"]}
        ]
    },
    "Adaptive Leveling": {
        "labels": [("Disk size", preprocess_params["Adaptive Leveling"]["disk_size"])],
        "sliders": [
            {"from_": 2, "to": 50, "resolution": 1, "value": preprocess_params["Adaptive Leveling"]["disk_size"]}
        ]
    },
    "Local Median Filter": {
        "labels": [("Size", preprocess_params["Local Median Filter"]["size"])],
        "sliders": [
            {"from_": 2, "to": 20, "resolution": 1, "value": preprocess_params["Local Median Filter"]["size"]}
        ]
    },
    "Binary Greyscale Erosion": {
        "radio_buttons": [("Rectangle", "re"), ("Ellipse", "el"), ("Cross", "cr")],
        "label_text": "Kernel Size",
        "slider_config": {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Binary Greyscale Erosion"]["kernel_size"]}
    },
    "Binary Greyscale Dilation": {
        "radio_buttons": [("Rectangle", "re"), ("Ellipse", "el"), ("Cross", "cr")],
        "label_text": "Kernel Size",
        "slider_config": {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Binary Greyscale Dilation"]["kernel_size"]}
    },
    "Binary Greyscale Opening": {
        "radio_buttons": [("Rectangle", "re"), ("Ellipse", "el"), ("Cross", "cr")],
        "label_text": "Kernel Size",
        "slider_config": {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Binary Greyscale Opening"]["kernel_size"]}
    },
    "Binary Greyscale Closing": {
        "radio_buttons": [("Rectangle", "re"), ("Ellipse", "el"), ("Cross", "cr")],
        "label_text": "Kernel Size",
        "slider_config": {"from_": 3, "to": 21, "resolution": 1, "value": preprocess_params["Binary Greyscale Closing"]["kernel_size"]}
    },
    "White Top Hat": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Diamond", "diamond"), ("Star", "star")],
        "label_text": "Selem Size",
        "slider_config": {"from_": 2, "to": 30, "resolution": 1, "value": preprocess_params["White Top Hat"]["selem_size"]}
    },
    "Black Top Hat": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Diamond", "diamond"), ("Star", "star")],
        "label_text": "Selem Size",
        "slider_config": {"from_": 2, "to": 30, "resolution": 1, "value": preprocess_params["Black Top Hat"]["selem_size"]}
    },
    "Gaussian Sharpening": {
        "labels": [("Radius", preprocess_params["Gaussian Sharpening"]["radius"]), ("Amount", preprocess_params["Gaussian Sharpening"]["amount"])],
        "sliders": [
            {"from_": 0.1, "to": 10.0, "resolution": 0.05, "value": preprocess_params["Gaussian Sharpening"]["radius"]},
            {"from_": 0.1, "to": 10.0, "resolution": 0.05, "value": preprocess_params["Gaussian Sharpening"]["amount"]}
        ]
    },
    "Binary Threshold": {
        "labels": [("Threshold", threshold_params["Binary Threshold"]["threshold"])],
        "sliders": [
            {"from_": 1, "to": 254, "resolution": 1, "value": threshold_params["Binary Threshold"]["threshold"]}
        ]
    },
    "Local Threshold": {
        "radio_buttons": [("Gaussian", "gaussian"), ("Mean", "mean"), ("Median", "median")],
        "labels": [("Block Size", threshold_params["Local Threshold"]["block_size"]), ("Offset", threshold_params["Local Threshold"]["offset"])],
        "sliders": [
            {"from_": 3, "to": 21, "resolution": 2, "value": threshold_params["Local Threshold"]["block_size"]},
            {"from_": 1, "to": 30, "resolution": 1, "value": threshold_params["Local Threshold"]["offset"]}
        ]
    },
    "Niblack Threshold": {
        "labels": [("Window size", threshold_params["Niblack Threshold"]["window_size"]), ("k", threshold_params["Niblack Threshold"]["k"])],
        "sliders": [
            {"from_": 3, "to": 51, "resolution": 2, "value": threshold_params["Niblack Threshold"]["window_size"]},
            {"from_": -5.0, "to": 5.0, "resolution": 0.05, "value": threshold_params["Niblack Threshold"]["k"]}
        ]
    },
    "Sauvola Threshold": {
        "labels": [("Window size", threshold_params["Sauvola Threshold"]["window_size"]), ("k", threshold_params["Sauvola Threshold"]["k"]), ("r", threshold_params["Sauvola Threshold"]["r"])],
        "sliders": [
            {"from_": 3, "to": 51, "resolution": 2, "value": threshold_params["Sauvola Threshold"]["window_size"]},
            {"from_": -5.0, "to": 5.0, "resolution": 0.05, "value": threshold_params["Sauvola Threshold"]["k"]},
            {"from_": 32, "to": 512, "resolution": 32, "value": threshold_params["Sauvola Threshold"]["r"]}
        ]
    },
    "Binary Erosion": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Star", "star"), ("Diamond", "diamond")],
        "labels": [("Footprint Size", process_params["Binary Erosion"]["footprint_size"])],
        "sliders": [
            {"from_": 1, "to": 50, "resolution": 1, "value": process_params["Binary Erosion"]["footprint_size"]}
        ]
    },
    "Binary Dilation": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Star", "star"), ("Diamond", "diamond")],
        "labels": [("Footprint Size", process_params["Binary Dilation"]["footprint_size"])],
        "sliders": [
            {"from_": 1, "to": 50, "resolution": 1, "value": process_params["Binary Dilation"]["footprint_size"]}
        ]
    },
    "Binary Opening": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Star", "star"), ("Diamond", "diamond")],
        "labels": [("Footprint Size", process_params["Binary Opening"]["footprint_size"])],
        "sliders": [
            {"from_": 1, "to": 50, "resolution": 1, "value": process_params["Binary Opening"]["footprint_size"]}
        ]
    },
    "Binary Closing": {
        "radio_buttons": [("Disk", "disk"), ("Square", "square"), ("Star", "star"), ("Diamond", "diamond")],
        "labels": [("Footprint Size", process_params["Binary Closing"]["footprint_size"])],
        "sliders": [
            {"from_": 1, "to": 50, "resolution": 1, "value": process_params["Binary Closing"]["footprint_size"]}
        ]
    },
    "Remove Small Holes": {
        "labels": [("Area threshold", process_params["Remove Small Holes"]["area_threshold"]), ("Connectivity", process_params["Remove Small Holes"]["connectivity"])],
        "sliders": [
            {"from_": 1, "to": 256, "resolution": 1, "value": process_params["Remove Small Holes"]["area_threshold"]},
            {"from_": 1, "to": 256, "resolution": 1, "value": process_params["Remove Small Holes"]["connectivity"]},
        ]
    },
    "Remove Small Objects": {
        "labels": [("Min size", process_params["Remove Small Objects"]["min_size"]), ("Connectivity", process_params["Remove Small Objects"]["connectivity"])],
        "sliders": [
            {"from_": 1, "to": 256, "resolution": 1, "value": process_params["Remove Small Objects"]["min_size"]},
            {"from_": 1, "to": 256, "resolution": 1, "value": process_params["Remove Small Objects"]["connectivity"]},
        ]
    },
}

preprocess_operations = {
    "Gaussian Blur": perform_gaussian_blur,
    "Non-local Mean Denoising": perform_non_local_denoising,
    "GaussianFilter": perform_gaussian_filter,
    "Erosion": perform_erosion,
    "Binary Greyscale Erosion": perform_binary_greyscale_erosion,
    "Binary Greyscale Dilation": perform_binary_greyscale_dilation,
    "Binary Greyscale Opening": perform_binary_greyscale_opening,
    "Binary Greyscale Closing": perform_binary_greyscale_closing,
    "Gamma Adjustment": perform_gamma_adjustment,
    "Contrast Stretching": perform_contrast_stretching,
    "Adaptive Equalization": perform_adaptive_equalization,
    "Region Leveling": perform_region_leveling,
    "Three Point Leveling": perform_three_point_leveling,
    "Gaussian Sharpening": perform_gaussian_sharpening,
    "Propagation": perform_propagation,
    "Polynomial Leveling": perform_polynomial_leveling,
    "Adaptive Leveling": perform_adaptive_leveling,
    "Local Median Filter": perform_local_median_filter,
    "White Top Hat": perform_white_top_hat,
    "Black Top Hat": perform_black_top_hat,
}

process_operations = {
    "Otsu Threshold": perform_otsu_threshold,
    "Local Threshold": perform_local_threshold,
    "Niblack Threshold": perform_niblack_threshold,
    "Sauvola Threshold": perform_sauvola_threshold,
    "Yen Threshold": perform_yen_threshold,
    "ISODATA Threshold": perform_isodata_threshold,
    "Binary Erosion": perform_binary_erosion,
    "Binary Dilation": perform_binary_dilation,
    "Binary Opening": perform_binary_opening,
    "Binary Closing": perform_binary_closing,
    "Remove Small Holes": perform_removing_small_holes,
    "Remove Small Objects": perform_removing_small_objects,
    "Manual Erase": perform_manual_white_remove,
    "Binary Threshold": perform_binary_threshold
}