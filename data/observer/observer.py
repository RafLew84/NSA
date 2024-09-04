# -*- coding: utf-8 -*-
"""
Observer pattern for the app

@author
Author: Rafał Lewandków (rafal.lewandkow2@uwr.edu.pl)
"""
import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Abstract base class for observers in the observer design pattern.

    This class should be subclassed, and the `update` method should be implemented
    by any class that wants to act as an observer.
    """
    @abstractmethod
    def update(self, observable, *args, **kwargs):
        """
        Method that will be called by the Observable when notifying observers.

        Args:
            observable (Observable): The Observable instance that triggered the notification.
            *args: Variable length argument list to pass to the observer.
            **kwargs: Arbitrary keyword arguments to pass to the observer.
        """
        pass