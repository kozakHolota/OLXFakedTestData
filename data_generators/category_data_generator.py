import random

import aiohttp


class CategoryDataGenerator:
    def __init__(self, host: str, port: int, amount: int):
        self.amount = amount
        self.port = port
        self.host = host

    async def generate(self):
        async with aiohttp.ClientSession(f"https://{self.host}:{self.port}") as session:
            categories = []
            for cat in await (await session.get("/api/items/categories", ssl=False)).json():
                if not cat["subCategories"]:
                    categories.append(cat["name"])
                else:
                    for sub_cat in cat["subCategories"]:
                        categories.append(sub_cat["name"])

            return random.choices(categories, k=self.amount)
