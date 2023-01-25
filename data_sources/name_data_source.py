import os
import random

from data_sources.abstract_data_source import AbstractDataSource
from utils.readers import read_csv


class NameDataSource(AbstractDataSource):

    @read_csv(os.path.join("sample_data", "baby-names.csv"))
    def read(self):
        pass

    def random_choice(self):
        return random.choices(self.array["name"], k=1)[0]