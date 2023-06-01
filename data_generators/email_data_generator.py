from ai.ai_data_gen import AiDataGen


class EmailDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str):
        prompt = [
            {"role": "system", "content": "You register a new user on OLX"},
            {"role": "user", "content": "Generate me one fake email address. Tell me only email address and nothing else."}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)
