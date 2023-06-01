from ai.ai_data_gen import AiDataGen


class ItemImageDataGenerator(AiDataGen):
    def __init__(self, category: str, amount: int, openai_key: str):
        prompt = f"Зображення товару на порталі OLX в категорії {category}"
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key, is_image=True, img_size='256x256', img_fname_template="item")

    async def generate(self):
        res = await super().generate()
        is_favorite = True
        for i in range(len(res)):
            res[i]["isFavorite"] = is_favorite
            if is_favorite:
                is_favorite = False

        return res