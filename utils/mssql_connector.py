import sqlalchemy as sql
from sqlalchemy.orm import Session


class MSSQLConnector:
    def __init__(self, host, user, password, database):
        self.__connector = sql.create_engine(f"mssql+pymssql://{user}:{password}@{host}/{database}", future=True)
        self.__session = Session(self.__connector)

    @property
    def connection(self):
        return self.__connector

    @property
    def session(self):
        return self.__session