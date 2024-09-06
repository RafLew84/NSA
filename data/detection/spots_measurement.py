# -*- coding: utf-8 -*-
"""
Module for spots detection in the NanoSurface Analyzer application.

This module provides functions for detecting and analyzing spots in images. 
It includes labeling, calculating regions, computing nearest neighbors, 
tracking spots, and overlaying labels on original images.

Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import numpy as np
import cv2
from skimage import measure, morphology
from scipy.spatial import KDTree
from skimage import feature
from PIL import Image, ImageTk

import logging

logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.DEBUG,  # Set default logging level to DEBUG
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def label_image(img):
    """
    Label connected regions in the input binary image.

    Args:
        img (numpy.ndarray): Binary image to be labeled.

    Returns:
        labeled_image (numpy.ndarray): Labeled image where each connected region has a unique label.
        regions_num (int): Number of distinct regions detected in the image.
        names (list): List of region labels as strings.

    Raises:
        ValueError: If the input image is not valid.
    """
    try:
        img = np.array(img)
        labeled_image = morphology.label(img)
        regions_num = np.max(labeled_image)  # The number of distinct regions (excluding the background)
        names = ["{:03}".format(i) for i in range(1, regions_num + 1)]  # Creating label names for regions
        return labeled_image, regions_num, names
    
    except Exception as e:
        logger.error(f"Error in label_image: {e}")
        raise ValueError(f"Failed to label the image: {e}")

def calculate_regions(labeled_image):
    """
    Calculate properties of labeled regions in an image.

    Args:
        labeled_image (numpy.ndarray): Labeled image where each region has a unique label.

    Returns:
        regions (list): List of region properties (e.g., area, centroid) calculated by skimage.measure.regionprops.
    
    Raises:
        ValueError: If region calculation fails.
    """
    try:
        regions = measure.regionprops(labeled_image)
        return regions
    
    except Exception as e:
        logger.error(f"Error in calculate_regions: {e}")
        raise ValueError(f"Failed to calculate regions: {e}")

def compute_nearest_neighbor_distances(centroids, names):
    """
    Compute the nearest neighbor distances and corresponding region names.

    Args:
        centroids (numpy.ndarray): Array of region centroids.
        names (list): List of region names.

    Returns:
        nearest_neighbor_distances (numpy.ndarray): Distances to the nearest neighbor for each region.
        nearest_neighbor_names (list): Names of the nearest neighbors for each region.
    
    Raises:
        ValueError: If computation of nearest neighbor distances fails.
    """
    try:
        tree = KDTree(centroids)
        distances, indices = tree.query(centroids, k=2)  # k=2 because the first neighbor is the point itself
        nearest_neighbor_distances = distances[:, 1]  # The second column contains the nearest neighbor distances
        nearest_neighbor_names = [names[idx[1]] for idx in indices]  # Retrieve names of the nearest neighbors
        return nearest_neighbor_distances, nearest_neighbor_names
    
    except Exception as e:
        logger.error(f"Error in compute_nearest_neighbor_distances: {e}")
        raise ValueError(f"Failed to compute nearest neighbor distances: {e}")

def track_spots(previous_centroids, current_centroids, threshold=5):
    """
    Track spots between consecutive frames based on nearest centroid matching.

    Args:
        previous_centroids (numpy.ndarray): Centroids of spots in the previous frame.
        current_centroids (numpy.ndarray): Centroids of spots in the current frame.
        threshold (float): Distance threshold for considering a match.

    Returns:
        matched_indices (list): List of tuples indicating matched spots (index in current_centroids, index in previous_centroids).
        new_spots (list): List of indices of new spots that do not match any spot in the previous frame.
    
    Raises:
        ValueError: If spot tracking fails.
    """
    try:
        tree = KDTree(previous_centroids)
        distances, indices = tree.query(current_centroids)
        matched_indices = []
        new_spots = []
        
        for i, (dist, idx) in enumerate(zip(distances, indices)):
            if dist < threshold:
                matched_indices.append((i, idx))
            else:
                new_spots.append(i)
        
        return matched_indices, new_spots
    
    except Exception as e:
        logger.error(f"Error in track_spots: {e}")
        raise ValueError(f"Failed to track spots: {e}")

def analyze_images(images, threshold=5):
    """
    Analyze a list of images, labeling regions, calculating centroids, areas, and nearest neighbor distances.

    Args:
        images (list): List of binary images to be analyzed.
        threshold (float): Distance threshold for spot tracking (not used in this function but provided for consistency).

    Returns:
        tuple: Containing all centroids, areas, labels names, nearest neighbor distances, and other analysis data.
    
    Raises:
        ValueError: If image analysis fails.
    """
    try:
        all_regions = []
        all_centroids = []
        all_areas = []
        all_labels_num = []
        all_labels_names = []
        nearest_neighbor_distances_list = []
        nearest_neighbor_names = []
        # spot_tracks = defaultdict(list)
        labeled_images = []
        
        for frame_index, img in enumerate(images):
            labeled_image, labels_num, labels_names = label_image(img)
            regions = calculate_regions(labeled_image)
            labeled_images.append(labeled_image)
            all_labels_num.append(labels_num)
            all_labels_names.append(labels_names)

            all_regions.append(regions)
            
            centroids = np.array([region.centroid for region in regions])
            areas = np.array([region.area for region in regions])
            
            all_centroids.append(centroids)
            all_areas.append(areas)
            
            nearest_neighbor_distances, nearest_neighbor_name = compute_nearest_neighbor_distances(centroids, labels_names)
            nearest_neighbor_distances_list.append(nearest_neighbor_distances)
            nearest_neighbor_names.append(nearest_neighbor_name)

        return all_centroids, all_areas, all_labels_names, nearest_neighbor_distances_list, nearest_neighbor_names, labeled_images, all_labels_num
    except Exception as e:
        logger.error(f"Error in analyze_images: {e}")
        raise ValueError(f"Failed to analyze images: {e}")

def overlay_labels_on_original(original_images, labeled_images, label_names, centroids, color='black'):
    """
    Overlay labels and contours on original images.

    Args:
        original_images (list): List of original images.
        labeled_images (list): List of labeled images.
        label_names (list): List of label names.
        centroids (list): List of centroids for each label.
        color (str): Color for the overlay (default is black).

    Returns:
        labeled_overlays (list): List of images with labels and contours overlaid.
    
    Raises:
        ValueError: If overlay fails.
    """
    try:
        labeled_overlays = []
        for original_image, labeled_image, label_name, centroid in zip(original_images, labeled_images, label_names, centroids):
            overlay = original_image.copy()
            
            # Perform Canny edge detection on the labeled image
            edges = feature.canny(labeled_image > 0.5)  # Canny edge detector expects a binary image

            edges_color = 0
            text_color = (0,0,0)

            if color == 'white':
                edges_color = 255
                text_color = (255,255,255)
            # Overlay edges on the original image
            overlay = np.array(overlay)
            overlay[edges] = edges_color
            
            for label, center in zip(label_name, centroid):
                overlay = cv2.putText(overlay, label, (int(center[1]), int(center[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.3, text_color, 1)
            
            labeled_overlays.append(overlay)
        return labeled_overlays
    
    except Exception as e:
        logger.error(f"Error in overlay_labels_on_original: {e}")
        raise ValueError(f"Failed to overlay labels on original images: {e}")

def overlay_selected_label(
        original_image, 
        labeled_image, 
        label_names, 
        centroids,
        index,
        label_colors=255
    ):
    """
    Overlay a selected label on the original image, highlighting it with the specified color.

    Args:
        original_image (numpy.ndarray): The original image.
        labeled_image (numpy.ndarray): The labeled image.
        label_names (list): List of label names.
        centroids (list): List of centroids for each label.
        index (int): Index of the label to highlight.
        label_colors (int): Color value for the label and edges (default is 255 for white).

    Returns:
        overlay (numpy.ndarray): Image with the selected label highlighted.
    
    Raises:
        ValueError: If overlay fails.
    """
    try:
        overlay = original_image.copy()
        selected_label = label_names[index]
        
        edges = feature.canny(labeled_image > 0.5)

        text_color = (label_colors,label_colors,label_colors)
        edges_color = label_colors

        overlay[edges] = edges_color

        for label, center in zip(label_names, centroids):
            if label == selected_label:
                if label_colors == 255:
                        text_color = (0,0,0)
                elif label_colors == 0:
                        text_color = (255,255,255)
            else:
                if label_colors == 255:
                    text_color = (255,255,255)
                elif label_colors == 0:
                    text_color = (0,0,0)
            overlay = cv2.putText(overlay, label, (int(center[1]), int(center[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.3, text_color, 1)
        return overlay
    except Exception as e:
        logger.error(f"Error in overlay_selected_label: {e}")
        raise ValueError(f"Failed to overlay selected label: {e}")
    

def convert_to_tk_image(image):
    """
    Convert a NumPy array image to a Tkinter-compatible image.

    Args:
        image (numpy.ndarray): The image to convert.

    Returns:
        tk_image (PIL.ImageTk.PhotoImage): Tkinter-compatible image.
    
    Raises:
        ValueError: If conversion fails.
    """
    try:
        image = Image.fromarray(image)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        logger.error(f"Error in convert_to_tk_image: {e}")
        raise ValueError(f"Failed to convert image to Tkinter format: {e}")