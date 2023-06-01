from ai.ai_data_gen import AiDataGen


class PhoneDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str):
        prompt = [
            {"role": "system", "content": "Ти - реєструєш свій профіль на порталі OLX"},
            {"role": "user", "content": "Згенеруй меі фіктивний мобільний номер з території України. Опублікуй лише номер і нічого більше"}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)
