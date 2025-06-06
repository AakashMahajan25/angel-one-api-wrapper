import aiohttp
from config import get_headers

class AngelClient:
    def __init__(self):
        self.headers = get_headers()
    
    async def get(self, url, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers, params=params) as response:
                return await response.json()
    

    async def post(self, url, payload):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=payload) as response:
                return await response.json()