import logging
from abc import ABC, abstractmethod

from utils.mssql_connector import MSSQLConnector


class AbstractDbObject(ABC):
    def __init__(self, db_object: MSSQLConnector):
        logging.basicConfig(format='%(asctime)s %(message)s')

        self.db_object: MSSQLConnector = db_object
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

    @abstractmethod
    def insert_data(self, count: int):
        raise NotImplemented("Not implemented")

    def commit(self):
        self.db_object.session.commit()

    def flush(self):
        self.db_object.session.flush()

    def query(self, *args, **kwargs):
        qr = self.db_object.session.query(*args, **kwargs)
        self.logger.info(f"Executing SQL Query: {qr}")

        return qr

