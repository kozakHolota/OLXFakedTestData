from functools import wraps

import pandas


class read_csv:
    def __init__(self, fname: str, separator=","):
        self.separator = separator
        self.fname = fname

    def __call__(self, func):
        @wraps(func)
        def wrapper(_self):
            if not hasattr(_self, "array") or not getattr(_self, "array"):
                _self.array = pandas.read_csv(self.fname, sep=self.separator, header=0)

        return wrapper


class read_json:
    def __init__(self, fname):
        self.fname = fname

    def __call__(self, func):
        @wraps(func)
        def wrapper(_self):
            if not hasattr(_self, "array") or not getattr(_self, "array"):
                _self.array = pandas.read_json(self.fname)

        return wrapper


