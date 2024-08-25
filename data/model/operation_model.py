# -*- coding: utf-8 -*-
"""
Data model for STM files data

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

class OperationModel:
    def __init__(self, process_name, image):
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