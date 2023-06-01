import base64
import datetime

import aiohttp
import openai


class AiDataGen:
    def __init__(self, prompt: [dict], amount: int, openai_key: str, is_image: bool = False, img_size: str=None, img_fname_template: str="tmp_img"):
        self.img_size = img_size if img_size else "1024x1024"
        self.prompt = prompt
        self.amount = amount
        openai.api_key = openai_key
        self.model = 'gpt-3.5-turbo'
        self.is_image = is_image
        self.img_fname_template = img_fname_template
        self.completion = openai.ChatCompletion() if not is_image else openai.Image

    async def convert_image_to_base64(self, url):
        async with aiohttp.ClientSession() as session:
            content = await session.get(url, ssl=False)
            return {"fileName": f"{self.img_fname_template}_{int(datetime.datetime.timestamp(datetime.datetime.now()))}.png", "base64Content": base64.b64encode(await content.read()).decode('utf-8')}

    async def generate(self):
        if self.is_image:
            return [await self.convert_image_to_base64(res['url']) for res in self.completion.create(prompt=self.prompt, n=self.amount, size=self.img_size)['data']]
        return [self.completion.create(model=self.model, messages=self.prompt).choices[0]['message']['content'] for _ in range(self.amount)]

