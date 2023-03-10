from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.dialects.mssql import DATETIMEOFFSET, DATETIME
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
    Subject = Column(String)
    CategoryId = Column(Integer, ForeignKey("Category.CategoryId"))
    Description = Column(String)
    AutoContinue = Column(Boolean)
    ContactDataId = Column(Integer, ForeignKey("ContactData.ContactDataId"))

class ItemImage(Base):
    __tablename__ = "ItemImage"
    ItemImageId = Column(Integer, primary_key=True, autoincrement=True)
    ItemId = Column(Integer, ForeignKey("Item.ItemId"))
    ImageId = Column(Integer, ForeignKey("Image.ImageId"))

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


class AspNetUsers(Base):
    __tablename__ = "AspNetUsers"
    Id = Column(String, primary_key=True)
    UserName = Column(String)
    NormalizedUserName = Column(String)
    Email = Column(String)
    NormalizedEmail = Column(String)
    EmailConfirmed = Column(Boolean)
    PasswordHash = Column(String)
    SecurityStamp = Column(String)
    ConcurrencyStamp = Column(String)
    PhoneNumber = Column(String)
    PhoneNumberConfirmed = Column(String)
    TwoFactorEnabled = Column(Boolean)
    LockoutEnd = Column(DATETIMEOFFSET)
    LockoutEnabled = Column(Boolean)
    AccessFailedCount = Column(Integer)


class UserUnited(Base):
    __tablename__ = "UserUnited"
    UnitedUserId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey("AspNetUsers.Id"))
    ContactPersonId = Column(Integer, ForeignKey("ContactPerson.ContactPersonId"))
    ImageId = Column(Integer, ForeignKey("Image.ImageId"))
    RequisitesId = Column(Integer, ForeignKey("Requisites.RequisitesId"))

class UserItem(Base):
    __tablename__ = "UserItem"
    UserItemId = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey("AspNetUsers.Id"))
    ItemId = Column(Integer, ForeignKey("Item.ItemId"))

class RefreshToken(Base):
    __tablename__ = "RefreshToken"
    Id = Column(Integer, primary_key=True, autoincrement=True)
    UserId = Column(Integer, ForeignKey("AspNetUsers.Id"))
    Token = Column(String)
    JwtId = Column(String)
    IsUsed = Column(Boolean)
    IsRevoked = Column(Boolean)
    AddedDate = Column(DATETIME)
    ExpiryDate = Column(DATETIME)