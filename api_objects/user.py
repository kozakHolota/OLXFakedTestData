from dataclasses import dataclass


@dataclass
class User:
    userId: str
    password: str
    contactPersonName: str
    email: str = None
    phoneNumber: str = None
    contactCity: str = None
    imagePath: str = None
    lowName: str = None
    lowAddress: str = None
    zipCode: str = None
    requisitesCity: str = None
    singleRegId: str = None
    isTaxesPayer: bool = True
    taxationId: int = None
    requisitesContactPersonName: str = None
