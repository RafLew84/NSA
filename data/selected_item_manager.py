import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.observer.observable import Observable
from data.model.file_data_model import FileDataModel

from PIL import Image

import logging

logger = logging.getLogger(__name__)

class SelectedItemManager(Observable):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SelectedItemManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.selected_item = None
            self.initialized = True
    
    def insert_data(self, item):
        self.selected_item = item
        self.notify_observers()