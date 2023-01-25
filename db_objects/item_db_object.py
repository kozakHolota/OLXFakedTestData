import random

from data_sources.cities_data_source import CitiesDataSource
from data_sources.name_data_source import NameDataSource
from data_sources.quotes_data_source import QuotesDataSource
from data_sources.surname_data_source import SurnameDataSource
from db_models.db_models import ContactData, Item, User, UserItem, Category
from db_objects.abstract_db_object import AbstractDbObject
from utils.db_utils import insert_contact_data
from utils.mssql_connector import MSSQLConnector


class ItemDbObject(AbstractDbObject):
    def __init__(self, db_object: MSSQLConnector, users):
        super().__init__(db_object)
        self.users_count = users
        self.name_ds = NameDataSource()
        self.surname_ds = SurnameDataSource()
        self.city_ds = CitiesDataSource()
        self.quotes_ds = QuotesDataSource()

    @insert_contact_data
    def insert_data(self, count: int):
        contact_data = self.db_object.session.query(ContactData.ContactDataId).all()
        users = self.db_object.session.query(User.UserId).all()
        categories = self.db_object.session.query(Category.CategoryId).all()
        for i in range(self.users_count):
            items = list()
            for k in range(count):
                new_item = Item(
                        Name=f"{self.name_ds.random_choice()} {self.surname_ds.random_choice()}",
                        CategoryId=random.choices(categories, k=1)[0][0],
                        Description=self.quotes_ds.random_choice(),
                        AutoContinue=bool(random.randint(0, 2)),
                        ContactDataId=contact_data[k][0]
                    )

                self.db_object.session.add(
                    new_item
                )

                items.append(new_item)

            self.commit()

            for k in range(count):
                user_item = UserItem(
                        UserId=users[i][0],
                        ItemId=self.query(Item.ItemId).filter(
                            Item.Name == items[k].Name,
                            Item.CategoryId == items[k].CategoryId,
                            Item.Description == items[k].Description,
                            Item.AutoContinue == items[k].AutoContinue,
                            Item.ContactDataId == items[k].ContactDataId
                        ).scalar()
                    )

                self.db_object.session.add(
                    user_item
                )

            self.commit()
            items.clear()