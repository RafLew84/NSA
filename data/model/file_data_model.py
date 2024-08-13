# -*- coding: utf-8 -*-
"""
Data model for STM files data

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

class FileDataModel:
    def __init__(self):
        self._data_name = None
        self._file_name = None
        self._header_info = None
        self._frame_number = None
        self._data = None
        self._greyscale_image = None
        self._operations = []

    # Getters
    @property
    def data_name(self):
        return self._data_name

    @property
    def file_name(self):
        return self._file_name

    @property
    def header_info(self):
        return self._header_info

    @property
    def frame_number(self):
        return self._frame_number

    @property
    def data(self):
        return self._data

    @property
    def greyscale_image(self):
        return self._greyscale_image

    @property
    def operations(self):
        return self._operations

    # Setters
    @data_name.setter
    def data_name(self, value):
        self._data_name = value

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @header_info.setter
    def header_info(self, value):
        self._header_info = value

    @frame_number.setter
    def frame_number(self, value):
        self._frame_number = value

    @data.setter
    def data(self, value):
        self._data = value

    @greyscale_image.setter
    def greyscale_image(self, value):
        self._greyscale_image = value

    # Operations methods
    def clear_operations(self):
        self._operations.clear()

    def add_operation(self, operation):
        self._operations.append(operation)

    def get_operation(self, index):
        if 0 <= index < len(self._operations):
            return self._operations[index]
        else:
            raise IndexError("Index out of range")

    def get_all_operations(self):
        return self._operations[:]