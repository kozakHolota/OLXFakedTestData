import json
import random

import aiohttp


class CitiesDataGenerator:
    def __init__(self, host: str, port: int, amount: int):
        self.amount = amount
        self.port = port
        self.host = host

    async def generate(self):
        async with aiohttp.ClientSession(f"https://{self.host}:{self.port}") as session:
            cities = [city_entry["name"] for city_entry in (await (await session.get("/api/cities/all?pageSize=500&pageNum=1", ssl=False)).json())["cities"]]
            return random.choices(cities, k=self.amount)

