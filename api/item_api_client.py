import json
import random
from pprint import pprint

from api.abstract_api_client import AbstractApiClient
from data_generators.category_data_generator import CategoryDataGenerator
from data_generators.cities_data_generator import CitiesDataGenerator
from data_generators.email_data_generator import EmailDataGenerator
from data_generators.item_data_generator import ItemDataGenerator
from data_generators.item_image_data_generator import ItemImageDataGenerator
from data_generators.name_data_generator import NameDataGenerator
from data_generators.phone_data_generator import PhoneDataGenerator


class ItemApiClient(AbstractApiClient):
    def __init__(self, host: str, port: int, openai_api_key: str, auth_token: str):
        super().__init__(host, port, "/api/items")
        self.auth_token = auth_token
        self.name_data_gen = NameDataGenerator(1, openai_api_key)
        self.phone_data_gen = PhoneDataGenerator(1, openai_api_key)
        self.city_data_gen = CitiesDataGenerator(self.host, self.port, 1)
        self.category_data_gen = CategoryDataGenerator(self.host, self.port, 1)
        self.email_data_gen = EmailDataGenerator(1, openai_api_key)
        self.openai_api_key = openai_api_key

    def update_auth_token(self, new_auth_token: str):
        self.auth_token = new_auth_token

    async def add_item(self):
        category = (await self.category_data_gen.generate())[0]
        item_pictures = await ItemImageDataGenerator(category, 8, self.openai_api_key).generate()
        item = (await ItemDataGenerator(1, self.openai_api_key, category).generate())[0]
        payload = {
            "name": (await self.name_data_gen.generate())[0],
            "subject": " ".join(item.split(" ")[:2]),
            "category": category,
            "price": random.randint(1, 10000),
            "description": item,
            "autoContinue": bool(random.randint(0, 1)),
            "contactEmail": (await self.email_data_gen.generate())[0],
            "contactPhone": (await self.phone_data_gen.generate())[0],
            "contactCity": (await self.city_data_gen.generate())[0],
            "images": item_pictures
        }
        return await self.post("/add", payload, auth_token=self.auth_token)
