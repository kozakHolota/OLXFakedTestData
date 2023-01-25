from abc import ABC, abstractmethod

from pandas import DataFrame


class AbstractDataSource(ABC):
    def __init__(self):
        self.array = None
        self.read()

    @abstractmethod
    def read(self):
        raise NotImplemented("Not implemented")

    @abstractmethod
    def random_choice(self):
        raise NotImplemented("Not implemented")