from ai.ai_data_gen import AiDataGen


class UserNameDataGenerator(AiDataGen):
    def __init__(self, amount: int, openai_key: str):
        prompt = [
            {"role": "system", "content": "You register a new user on OLX"},
            {"role": "user", "content": "Generate me one real username. Tell me only username and nothing else."}
        ]
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key)
