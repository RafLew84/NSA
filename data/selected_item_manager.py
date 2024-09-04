# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from data.observer.observable import Observable

import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class SelectedItemManager(Observable):
    """
    Singleton class that manages the currently selected item and notifies observers of changes.
    
    Inherits:
        Observable: Base class for implementing the observer pattern.
    
    Attributes:
        selected_item (FileDataModel or None): The currently selected item, or None if no item is selected.
    
    Methods:
        __new__(cls, *args, **kwargs): Ensures only one instance of the class is created.
        __init__(self): Initializes the manager, setting the selected item to None.
        insert_data(self, item): Sets a new item as the selected item and updates observers.
        update(self, observable, *args, **kwargs): Notifies observers if the selected item changes.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Ensures that only one instance of the class is created (Singleton pattern).

        Returns:
            SelectedItemManager: The single instance of the class.
        """
        if cls._instance is None:
            cls._instance = super(SelectedItemManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """
        Initializes the SelectedItemManager instance. Sets the initial selected item to None.
        """
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.selected_item = None
            self.initialized = True
    
    def insert_data(self, item):
        """
        Updates the selected item and notifies observers.

        Args:
            item (FileDataModel): The new item to be set as the selected item.

        Raises:
            TypeError: If the item is not an instance of FileDataModel.
        """
        if self.selected_item:
            self.selected_item.remove_observer(self)  # Remove self as an observer of the old item
        self.selected_item = item
        self.selected_item.image_for_processing = item.original_image
        if self.selected_item:
            self.selected_item.add_observer(self)  # Add self as an observer of the new item
        self.notify_observers()  # Notify observers of the selection change

    def update(self, observable, *args, **kwargs):
        """
        Called when an observable updates. Notifies observers if the selected item has changed.

        Args:
            observable (Observable): The observable that has been updated.
            *args: Additional arguments passed by the observable.
            **kwargs: Additional keyword arguments passed by the observable.
        """
        if observable is self.selected_item:
            self.notify_observers()  # Notify observers if the selected item has changed