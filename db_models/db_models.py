from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = "City"

    CityId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)


class Category(Base):
    __tablename__ = "Category"
    CategoryId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    ParentCategoryId = Column(Integer, ForeignKey("Image.ImageId"))


class ContactData(Base):
    __tablename__ = "ContactData"
    ContactDataId = Column(Integer, primary_key=True, autoincrement=True)
    Email = Column(String)
    Phone = Column(String)
    CityId = Column(Integer, ForeignKey("City.CityId"))


class ContactPerson(Base):
    __tablename__ = "ContactPerson"
    ContactPersonId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    CityId = Column(Integer, ForeignKey("City.CityId"))


class Image(Base):
    __tablename__ = "Image"
    ImageId = Column(Integer, primary_key=True, autoincrement=True)
    Path = Column(String)


class Item(Base):
    __tablename__ = "Item"
    ItemId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    CategoryId = Column(Integer, ForeignKey("Category.CategoryId"))
    Description = Column(String)
    ImageId = Column(Integer, ForeignKey("Image.ImageId"), nullable=True)
    AutoContinue = Column(Boolean)
    ContactDataId = Column(Integer, ForeignKey("ContactData.ContactDataId"))


class Requisites(Base):
    __tablename__ = "Requisites"
    RequisitesId = Column(Integer, primary_key=True, autoincrement=True)
    LowName = Column(String)
    LowAddress = Column(String)
    ZipCode = Column(Integer)
    CityId = Column(Integer, ForeignKey("City.CityId"))
    SingleRegId = Column(Integer)
    IsTaxesPayer = Column(Integer)
    TaxationId = Column(Integer)
    ContactPersonName = Column(String)


class User(Base):
    __tablename__ = "User"
    UserId = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String)
    Password = Column(String)
    Email = Column(String)
    ContactPersonId = Column(Integer, ForeignKey("ContactPerson.ContactPersonId"))
    RequisitesId = Column(Integer, ForeignKey("Requisites.RequisitesId"))


class UserItem(Base):
    __tablename__ = "UserItem"
    UserItemId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey("User.UserId"))
    ItemId = Column(Integer, ForeignKey("Item.ItemId"))