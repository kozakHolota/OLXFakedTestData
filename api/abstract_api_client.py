import asyncio
import ssl
from abc import ABC

import aiohttp


class AbstractApiClient(ABC):
    def __init__(self, host: str, port: int, base_endpoint: str):
        self.base_endpoint = base_endpoint
        self.port = port
        self.host = host
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False
        ssl_ctx.verify_mode = ssl.CERT_NONE
        self.basic_url = f"https://{host}:{port}"
        self.__tasks = []

    async def add_task(self, func):
        self.__tasks.append(func)

    async def get(self, endpoint: str, auth_token=None, **kwargs):
        async with aiohttp.ClientSession(self.basic_url) as session:
            if auth_token:
                session.headers["Authorization"] = f"Bearer {auth_token}"
            async with session.get(self.base_endpoint + endpoint, ssl=False, **kwargs) as result:
                if not result.ok:
                    return f"Status code: {result.status}. Message: {await result.text()}"
                return await result.json()

    def get_await(self, endpoint: str, **kwargs):
        self.__tasks.append(self.get(endpoint, **kwargs))
        return self

    async def post(self, endpoint: str, payload: dict, auth_token=None, **kwargs):
        async with aiohttp.ClientSession(self.basic_url) as session:
            if auth_token:
                session.headers["Authorization"] = f"Bearer {auth_token}"
            async with session.post(self.base_endpoint + endpoint, ssl=False, json=payload, **kwargs) as result:
                if not result.ok:
                    return f"Status code: {result.status}. Message: {await result.text()}"
                return await result.json()

    def post_await(self, endpoint: str, payload: dict, **kwargs):
        self.__tasks.append(self.post(endpoint, payload, **kwargs))
        return self

    async def perform(self):
        results = await asyncio.gather(*self.__tasks)
        self.__tasks.clear()
        return results
