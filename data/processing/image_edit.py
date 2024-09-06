# -*- coding: utf-8 -*-
"""
Morphology functions for binary images.

This module provides tools for editing binary images, including removing white areas by selecting them interactively.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ImageEditor:
    """
    A class to allow interactive editing of a binary image using matplotlib's RectangleSelector.

    Attributes:
        original_image (numpy.ndarray): The original input image.
        modified_image (numpy.ndarray): The image after modifications.
        fig (matplotlib.figure.Figure): The matplotlib figure.
        ax (matplotlib.axes.Axes): The matplotlib axes.
        rect_selector (RectangleSelector): The interactive rectangle selector for editing the image.
    """
    def __init__(self, image):
        """
        Initialize the ImageEditor with the input image and set up the interactive plot.

        Args:
            image (numpy.ndarray): The input binary image to be edited.
        """
        try:
            self.original_image = image
            self.modified_image = image.copy()
            self.fig, self.ax = plt.subplots()
            self.rect_selector = RectangleSelector(self.ax, self.onselect,
                                                useblit=True,
                                                button=[1], minspanx=5, minspany=5,
                                                spancoords='pixels', interactive=True
                                                )
            self.ax.imshow(self.modified_image, cmap='gray')
            plt.connect('key_press_event', self.accept)
            plt.show()

        except Exception as e:
            msg = f"Error initializing ImageEditor: {e}"
            logger.error(msg)
            raise ValueError(msg)

    def onselect(self, eclick, erelease):
        """
        Callback function for the rectangle selector.

        Sets the selected region to black (removes white pixels).

        Args:
            eclick (matplotlib.backend_bases.MouseEvent): Mouse click event.
            erelease (matplotlib.backend_bases.MouseEvent): Mouse release event.
        """
        try:
            x1, y1 = int(eclick.xdata), int(eclick.ydata)
            x2, y2 = int(erelease.xdata), int(erelease.ydata)
            self.modified_image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)] = 0
            self.ax.imshow(self.modified_image, cmap='gray')
            plt.draw()

        except Exception as e:
            msg = f"Error during rectangle selection: {e}"
            logger.error(msg)
            raise ValueError(msg)

    def accept(self, event):
        """
        Callback function to accept changes when 'enter' key is pressed.

        Args:
            event (matplotlib.backend_bases.KeyEvent): Key press event.
        """
        try:
            if event.key == 'enter':
                plt.close(self.fig)

        except Exception as e:
            msg = f"Error during key press event: {e}"
            logger.error(msg)
            raise ValueError(msg)

    def get_modified_image(self):
        """
        Return the modified image after editing.

        Returns:
            numpy.ndarray: The modified image.
        """
        return self.modified_image

def ImageEditRemoveWhite(image):
    """
    Remove white areas from the binary image using interactive selection.

    Args:
        image (numpy.ndarray): The input binary image.

    Returns:
        numpy.ndarray: The modified image with selected white areas removed.
    """
    try:
        editor = ImageEditor(image)
        return editor.get_modified_image()
    
    except Exception as e:
        msg = f"Error in ImageEditRemoveWhite: {e}"
        logger.error(msg)
        raise ValueError(msg)
