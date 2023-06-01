from ai.ai_data_gen import AiDataGen


class NameDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str):
        prompt = [
            {"role": "system", "content": "Ти - громадянин або громадянка України"},
            {"role": "user", "content": "Згенеруй мені українське імʼя і прізвище через пробіл. Лише імʼя і прізвище."}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)
