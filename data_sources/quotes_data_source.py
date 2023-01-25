import os
import random

from data_sources.abstract_data_source import AbstractDataSource
from utils.readers import read_json


class QuotesDataSource(AbstractDataSource):
    @read_json(os.path.join("sample_data", "quotes.json"))
    def read(self):
        pass

    def random_choice(self):
        return random.choices(self.array["quote"], k=1)[0]