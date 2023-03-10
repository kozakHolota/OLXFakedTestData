import random

from data_sources.cities_data_source import CitiesDataSource
from data_sources.name_data_source import NameDataSource
from data_sources.quotes_data_source import QuotesDataSource
from data_sources.subject_data_source import SubjectDataSource
from data_sources.surname_data_source import SurnameDataSource
from db_models.db_models import ContactData, Item, UserItem, Category
from db_objects.abstract_db_object import AbstractDbObject
from utils.db_utils import insert_contact_data
from utils.mssql_connector import MSSQLConnector


class ItemDbObject(AbstractDbObject):
    def __init__(self, db_object: MSSQLConnector, user_ids: list):
        super().__init__(db_object)
        self.user_ids = user_ids
        self.name_ds = NameDataSource()
        self.surname_ds = SurnameDataSource()
        self.city_ds = CitiesDataSource()
        self.quotes_ds = QuotesDataSource()
        self.subject_ds = SubjectDataSource()

    @insert_contact_data
    def insert_data(self, count: int):
        contact_data = self.db_object.session.query(ContactData.ContactDataId).all()
        categories = self.db_object.session.query(Category.CategoryId).filter(Category.ParentCategoryId.isnot(None)).all()
        for user_id in self.user_ids:
            items = list()
            for k in range(int(count)):
                new_item = Item(
                        Name=f"{self.name_ds.random_choice()} {self.surname_ds.random_choice()}",
                        Subject=self.subject_ds.random_choice(),
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
                user_item = UserItem(
                            UserId=user_id,
                            ItemId=self.query(Item.ItemId).filter(
                                Item.Name == new_item.Name,
                                Item.CategoryId == new_item.CategoryId,
                                Item.Description == new_item.Description,
                                Item.AutoContinue == new_item.AutoContinue,
                                Item.ContactDataId == new_item.ContactDataId
                            ).scalar()
                        )

                self.db_object.session.add(
                        user_item
                    )

                self.commit()
            items.clear()