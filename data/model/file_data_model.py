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
        self._original_image = None
        self._operations = []
        self._image_for_analisys = None
        self._labeled_image = None
        self._labeled_overlays = None
        self._labeled_overlays_white = None
        self._areas = None
        self._labels_names = None
        self._nearest_neighbor_distance = None
        self._nearest_neighbor_name = None

    # Getters
    @property
    def image_for_analisys(self):
        return self._image_for_analisys
    
    @property
    def labeled_image(self):
        return self._labeled_image
    
    @property
    def labeled_overlays(self):
        return self._labeled_overlays
    
    @property
    def labeled_overlays_white(self):
        return self._labeled_overlays_white
    
    @property
    def areas(self):
        return self._areas
    
    @property
    def labels_names(self):
        return self._labels_names
    
    @property
    def nearest_neighbor_distance(self):
        return self._nearest_neighbor_distance
    
    @property
    def nearest_neighbor_name(self):
        return self._nearest_neighbor_name

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
    def original_image(self):
        return self._original_image

    @property
    def operations(self):
        return self._operations

    # Setters
    @image_for_analisys.setter
    def image_for_analisys(self, value):
        self._image_for_analisys = value
    
    @labeled_image.setter
    def labeled_image(self, value):
        self._labeled_image = value

    @labeled_overlays.setter
    def labeled_overlays(self, value):
        self._labeled_overlays = value
    
    @labeled_overlays_white.setter
    def labeled_overlays_white(self, value):
        self._labeled_overlays_white = value
    
    @areas.setter
    def areas(self, value):
        self._areas = value
    
    @labels_names.setter
    def labeld_names(self, value):
        self._labels_names = value
    
    @nearest_neighbor_distance.setter
    def nearest_neighbor_distance(self, value):
        self._nearest_neighbor_distance = value

    @nearest_neighbor_name.setter
    def nearest_neighbor_name(self, value):
        self._nearest_neighbor_name = value

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

    @original_image.setter
    def original_image(self, value):
        self._original_image = value

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