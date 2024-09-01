# -*- coding: utf-8 -*-
"""
Data model for STM files data

@author
rlewandkow
"""

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.observer.observable import Observable

class FileDataModel(Observable):
    def __init__(self):
        super().__init__()  # Call the Observable's constructor
        self._data_name = None
        self._file_name = None
        self._header_info = None
        self._frame_number = None
        self._data = None
        self._original_image = None
        self._image_for_processing = None
        self._operations = []
        self._image_for_analisys = None
        self._labeled_image = None
        self._labeled_overlays = None
        self._labeled_overlays_white = None
        self._areas = None
        self._labels_names = None
        self._nearest_neighbor_distance = None
        self._nearest_neighbor_name = None
        self._currently_processing_image = None
        self._area_px_nm_coefficient = None
        self._x_px_nm_coefficient = None
        self._y_px_nm_coefficient = None

    # Getters
    @property
    def area_px_nm_coefficient(self):
        return self._area_px_nm_coefficient
    
    @property
    def x_px_nm_coeffixient(self):
        return self._x_px_nm_coefficient
    
    @property
    def y_px_nm_coefficient(self):
        return self._y_px_nm_coefficient

    @property  
    def currently_processing_image(self):
        return self._currently_processing_image

    @property
    def image_for_processing(self):
        return self._image_for_processing
    
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

    # Property Setters with Notification
    @area_px_nm_coefficient.setter
    def area_px_nm_coefficient(self, value):
        self._area_px_nm_coefficient = value

    @x_px_nm_coeffixient.setter
    def x_px_nm_coefficient(self, value):
        self._x_px_nm_coefficient = value

    @y_px_nm_coefficient.setter
    def y_px_nm_coefficient(self, value):
        self._y_px_nm_coefficient = value

    @currently_processing_image.setter
    def currently_processing_image(self, value):
        self._currently_processing_image = value
        self.notify_observers()

    @image_for_processing.setter
    def image_for_processing(self, value):
        self._image_for_processing = value
        self.notify_observers()

    @image_for_analisys.setter
    def image_for_analisys(self, value):
        self._image_for_analisys = value
        self.notify_observers()

    @labeled_image.setter
    def labeled_image(self, value):
        self._labeled_image = value
        self.notify_observers()

    @labeled_overlays.setter
    def labeled_overlays(self, value):
        self._labeled_overlays = value
        self.notify_observers()

    @labeled_overlays_white.setter
    def labeled_overlays_white(self, value):
        self._labeled_overlays_white = value
        self.notify_observers()

    @areas.setter
    def areas(self, value):
        self._areas = value
        self.notify_observers()

    @labels_names.setter
    def labels_names(self, value):
        self._labels_names = value
        self.notify_observers()

    @nearest_neighbor_distance.setter
    def nearest_neighbor_distance(self, value):
        self._nearest_neighbor_distance = value
        self.notify_observers()

    @nearest_neighbor_name.setter
    def nearest_neighbor_name(self, value):
        self._nearest_neighbor_name = value
        self.notify_observers()

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
        self.notify_observers()

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
        self.notify_observers()

    @header_info.setter
    def header_info(self, value):
        self._header_info = value
        self.notify_observers()

    @frame_number.setter
    def frame_number(self, value):
        self._frame_number = value
        self.notify_observers()

    @data.setter
    def data(self, value):
        self._data = value
        self.notify_observers()

    @original_image.setter
    def original_image(self, value):
        self._original_image = value
        self.notify_observers()

    # Operations methods with Notification
    def clear_operations(self):
        self._operations.clear()
        self.notify_observers()

    def add_operation(self, operation):
        self._operations.append(operation)
        self.notify_observers()

    def get_operation(self, index):
        if 0 <= index < len(self._operations):
            return self._operations[index]
        else:
            raise IndexError("Index out of range")

    def get_all_operations(self):
        return self._operations[:]
    
    def get_header_string(self):
        header_labels_generator = {
            "s94": self.get_s94_labels,
            "stp": self.get_stp_labels,
            "mpp": self.get_mpp_labels
        }

        header_labels_func = header_labels_generator.get(self.file_name[-3:].lower())
        if header_labels_func:
            return header_labels_func()
    
    def get_s94_labels(self):
        header = [
            f"X Amplitude: {self.header_info.get('x_size', ''):.2f} nm",
            f"Y Amplitude: {self.header_info.get('y_size', ''):.2f} nm",
            f"Number of cols: {self.header_info.get('x_points', '')}",
            f"Number of rows: {self.header_info.get('y_points', '')}",
            f"X Offset: {self.header_info.get('x_offset', '')}",
            f"Y Offset: {self.header_info.get('y_offset', '')}",
            f"Z Gain: {self.header_info.get('z_gain', '')}"
        ]

        return f"Filename: {self.data_name}  {header[0]}  {header[1]}\n{header[2]}  {header[3]}"

    def get_mpp_labels(self):
        header = [
            f'X Amplitude: {float(self.header_info.get("Control", {}).get("X Amplitude", "")[:-3]):.2f} nm',
            f'Y Amplitude: {float(self.header_info.get("Control", {}).get("Y Amplitude", "")[:-3]):.2f} nm',
            f'Number of cols: {self.header_info.get("General Info", {}).get("Number of columns", "")}',
            f'Number of rows: {self.header_info.get("General Info", {}).get("Number of rows", "")}',
            f'X Offset: {self.header_info.get("Control", {}).get("X Offset", "")}',
            f'Y Offset: {self.header_info.get("Control", {}).get("Y Offset", "")}',
            f'Z Gain: {self.header_info.get("Control", {}).get("Z Gain", "")}'
        ]

        filename = os.path.basename(self.file_name)

        return f"Filename: {filename} Frame: {self.frame_number}  {header[0]}\n{header[1]}  {header[2]}  {header[3]}"

    def get_stp_labels(self):
        header = [
            f"X Amplitude: {float(self.header_info.get('X Amplitude', '')[:-3]):.2f} nm",
            f"Y Amplitude: {float(self.header_info.get('Y Amplitude', '')[:-3]):.2f} nm",
            f"Z Amplitude: {self.header_info.get('Z Amplitude', '')}",
            f"Number of cols: {self.header_info.get('Number of columns', '')}",
            f"Number of rows: {self.header_info.get('Number of rows', '')}",
            f"X Offset: {self.header_info.get('X Offset', '')}",
            f"Y Offset: {self.header_info.get('Y Offset', '')}",
            f"Z Gain: {self.header_info.get('Z Gain', '')}"
        ]

        return f"Filename: {self.data_name}  {header[0]}  {header[1]}\n{header[3]}  {header[4]}"