from ai.ai_data_gen import AiDataGen


class UserPicDataGenerator(AiDataGen):
    def __init__(self, name: str, amount: int, openai_key: str):
        prompt = f"Аватар користувача {name}"
        super().__init__(amount=amount, prompt=prompt, openai_key=openai_key, is_image=True, img_size='256x256', img_fname_template="userpic")