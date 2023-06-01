from random import randint

from api.abstract_api_client import AbstractApiClient
from data_generators.address_data_generator import AddressDataGenerator
from data_generators.cities_data_generator import CitiesDataGenerator
from data_generators.email_data_generator import EmailDataGenerator
from data_generators.name_data_generator import NameDataGenerator
from data_generators.phone_data_generator import PhoneDataGenerator
from data_generators.username_data_generator import UserNameDataGenerator
from data_generators.userpic_data_generator import UserPicDataGenerator


class UserApiClient(AbstractApiClient):
    def __init__(self, host: str, port: int, openai_api_key: str, user_password: str):
        super().__init__(host, port, "/api/users")
        self.user_password = user_password
        self.username_data_gen = UserNameDataGenerator(1, openai_api_key)
        self.name_data_gen = NameDataGenerator(1, openai_api_key)
        self.email_data_gen = EmailDataGenerator(1, openai_api_key)
        self.phone_data_gen = PhoneDataGenerator(1, openai_api_key)
        self.city_data_gen = CitiesDataGenerator(self.host, self.port, 1)
        self.address_data_gen = AddressDataGenerator(1, openai_api_key)
        self.openapi_key = openai_api_key

    async def register(self):
        username = (await self.username_data_gen.generate())[0].replace('"', '').replace("'", "")
        email = (await self.email_data_gen.generate())[0]
        name = (await self.name_data_gen.generate())[0]
        user_pic = (await UserPicDataGenerator(name, 1, self.openapi_key).generate())[0]

        payload = {
            "userId": username,
            "password": self.user_password,
            "contactPersonName": name,
            "email": email,
            "phoneNumber": (await self.phone_data_gen.generate())[0],
            "contactCity": (await self.city_data_gen.generate())[0],
            "image": user_pic,
            "lowName": name,
            "lowAddress": (await self.address_data_gen.generate())[0],
            "zipCode": randint(65000, 80000),
            "requisitesCity": (await self.city_data_gen.generate())[0],
            "singleRegId": (await self.username_data_gen.generate())[0],
            "isTaxesPayer": bool(randint(0, 1)),
            "taxationId": randint(100000, 300000),
            "requisitesContactPersonName": name
        }
        res = await self.post("/register", payload)

        if isinstance(res, str):
            raise RuntimeError(f"Something went wrong: {res}")
        return {"username": email, "password": self.user_password}

    async def login(self, email: str, password: str):
        return (await self.post("/login", {"userId": email, "password": password}))["token"]



