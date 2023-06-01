from ai.ai_data_gen import AiDataGen


class ItemDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str, category_name: str):
        self.category_name = category_name
        prompt = [
            {"role": "system", "content": "Ти - користувач порталу OLX"},
            {"role": "user", "content": f"Згенеруй мені фіктивне оголошення до 20 слів в категорії: {self.category_name}"}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)