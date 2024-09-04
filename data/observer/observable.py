# -*- coding: utf-8 -*-
"""
Observer pattern for the app

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

import logging
logger = logging.getLogger(__name__)

# Configure logging for the entire application (if not configured elsewhere)
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG level for detailed logging
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class Observable:
    """
    A class that implements the observer pattern.

    The Observable class maintains a list of observers (subscribers) and notifies
    them of changes by calling their update method.
    """
    def __init__(self):
        """
        Initialize the Observable object with an empty list of observers.
        """
        self._observers = []

    def add_observer(self, observer):
        """
        Add an observer to the list if it is not already present.

        Args:
            observer (object): An object that implements an update method to be notified of changes.
        """
        if observer not in self._observers:
            self._observers.append(observer)
        else:
            message = f"Observer {observer} is already registered."
            logger.warning(message)
            print(message)

    def remove_observer(self, observer):
        """
        Remove an observer from the list if it is present.

        Args:
            observer (object): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)
        else:
            message = f"Observer {observer} is not registered and cannot be removed."
            logger.warning(message)
            print(message)

    def notify_observers(self, *args, **kwargs):
        """
        Notify all observers of a change by calling their update method.

        Args:
            *args: Variable length argument list to pass to the observers.
            **kwargs: Arbitrary keyword arguments to pass to the observers.
        """
        for observer in self._observers:
            try:
                observer.update(self, *args, **kwargs)
            except AttributeError as e:
                message = f"Observer {observer} does not have an 'update' method. Error: {e}"
                logger.error(message)
                print(message)
            except Exception as e:
                message = f"Error notifying observer {observer}: {e}"
                logger.error(message)
                print(message)