from ai.ai_data_gen import AiDataGen


class AddressDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str):
        prompt = [
            {"role": "system", "content": "Ти - громадянин або громадянка України"},
            {"role": "user", "content": "Згенеруй мені українську домашню адресу без назви міста. Лише адресу і нічого більше."}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)