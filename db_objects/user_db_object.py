from data_sources.addresses_data_source import AddressesDataSource
from data_sources.cities_data_source import CitiesDataSource
from data_sources.name_data_source import NameDataSource
from data_sources.surname_data_source import SurnameDataSource
from db_objects.abstract_db_object import AbstractDbObject
from utils.api_utils import create_users
from utils.mssql_connector import MSSQLConnector


class UserDbObject(AbstractDbObject):
    def __init__(self, db_object: MSSQLConnector, default_user_password: str):
        super().__init__(db_object)
        self.default_user_password = default_user_password
        self.name_ds = NameDataSource()
        self.surname_ds = SurnameDataSource()
        self.address_ds = AddressesDataSource()
        self.city_ds = CitiesDataSource()

    @create_users
    def insert_data(self, count: int):
        return getattr(self, "user_ids")
