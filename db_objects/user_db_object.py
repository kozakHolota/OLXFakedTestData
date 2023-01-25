import random
import string

from data_sources.name_data_source import NameDataSource
from data_sources.surname_data_source import SurnameDataSource
from db_models.db_models import ContactPerson, Requisites, User
from db_objects.abstract_db_object import AbstractDbObject
from utils.db_utils import insert_contact_person, insert_requisites
from utils.mssql_connector import MSSQLConnector


class UserDbObject(AbstractDbObject):
    def __init__(self, db_object: MSSQLConnector):
        super().__init__(db_object)
        self.name_ds = NameDataSource()
        self.surname_ds = SurnameDataSource()

    @insert_contact_person
    @insert_requisites
    def insert_data(self, count: int):
        contact_persons = self.db_object.session.query(ContactPerson.ContactPersonId).all()
        requisites = self.db_object.session.query(Requisites.RequisitesId).all()
        for i in range(count):
            self.db_object.session.add(
                User(
                    UserName=f"{self.name_ds.random_choice()} {self.surname_ds.random_choice()}",
                    Password="".join(random.choices([string.printable], k=20)),
                    Email="".join(random.choices([*string.ascii_letters, *string.digits], k=10)) + "@gmail.com",
                    ContactPersonId=contact_persons[i][0],
                    RequisitesId=requisites[i][0]
                )
            )
        self.commit()
