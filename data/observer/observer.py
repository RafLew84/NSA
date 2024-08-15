import os, sys

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, observable, *args, **kwargs):
        pass