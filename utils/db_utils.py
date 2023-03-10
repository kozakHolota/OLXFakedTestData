import logging
import random
import string

import sqlalchemy
from sqlalchemy.dialects import mssql

from data_sources.cities_data_source import CitiesDataSource
from data_sources.name_data_source import NameDataSource
from data_sources.surname_data_source import SurnameDataSource
from db_models.db_models import City, ContactData
from utils.mssql_connector import MSSQLConnector


def insert_contact_data(meth):
    def wrapper(self, count):
        sconnect: MSSQLConnector = self.db_object
        if not hasattr(self, "name_ds") or not getattr(self, "name_ds"):
            self.name_ds = NameDataSource()
        if not hasattr(self, "surname_ds") or not getattr(self, "surname_ds"):
            self.surname_ds = SurnameDataSource()
        if not hasattr(self, "city_ds") or not getattr(self, "city_ds"):
            self.city_ds = CitiesDataSource()

        for _ in range(int(count)):
            sconnect.session.add(
                ContactData(
                    Email=f"{self.name_ds.random_choice()}.{self.surname_ds.random_choice()}.{random.randint(100, 10000)}@gmail.com",
                    Phone=f"+380{random.randint(6, 10)}{random.randint(2, 8)}{''.join(random.choices(string.digits, k=7))}",
                    CityId=sconnect.session.query(City.CityId).filter(
                        City.Name == self.city_ds.random_choice()).first()[0]
                )
            )

        sconnect.session.commit()

        return meth(self, count)

    return wrapper


def delete_all(db_object: MSSQLConnector):
    logging.basicConfig(format='%(asctime)s %(message)s')
    logger = logging.getLogger("Garbage Collector")
    logger.setLevel(logging.DEBUG)

    from db_models import db_models as dbs
    clses = [dbs.UserItem, dbs.Item, dbs.AspNetUsers, dbs.ContactData, dbs.ContactPerson, dbs.Image, dbs.RefreshToken,
             dbs.Requisites, dbs.ContactPerson]

    with db_object.connection.begin() as con:

        for cls in clses:
            del_st = sqlalchemy.delete(cls)
            try:
                logger.info("Executing DELETE statement: " + str(del_st.compile(dialect=mssql.dialect())))
                con.execute(sqlalchemy.delete(cls))
            except Exception as e:
                logger.error(e)
