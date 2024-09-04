# -*- coding: utf-8 -*-
"""
Data model for STM files data.

This module defines the `OperationModel` class, which holds data for STM file processing.

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

class OperationModel:
    """
    Represents a data model for STM files.

    Attributes:
        process_name (str): The name of the process associated with the STM data.
        image (numpy.ndarray): The image data associated with the STM data.
    """
    def __init__(self, process_name, image):
        """
        Initialize the OperationModel instance.

        Args:
            process_name (str): The name of the process.
            image (numpy.ndarray): The image data.
        """
        self._process_name = process_name
        self._image = image

    @property
    def process_name(self):
        return self._process_name

    @process_name.setter
    def process_name(self, value):
        self._process_name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value