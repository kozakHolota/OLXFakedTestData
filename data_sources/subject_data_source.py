import os
import random

from data_sources.abstract_data_source import AbstractDataSource
from utils.readers import read_json


class SubjectDataSource(AbstractDataSource):
    @read_json(os.path.join("sample_data", "quotes.json"))
    def read(self):
        pass

    def random_choice(self):
        return random.choices([k for k in self.array["quote"] if len(k.split(" ")) <= 10], k=1)[0]