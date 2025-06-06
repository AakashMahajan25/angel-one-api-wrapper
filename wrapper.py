from client import AngelClient
from config import LOGIN_PAYLOAD
from endpoints import PLACE_ORDER, GET_ORDER_BOOK, GET_PROFILE, AUTHENTICATE

class AngelAPIWrapper:
    def __init__(self):
        self.client = AngelClient()

    async def login(self):
        payload = LOGIN_PAYLOAD
        return await self.client.post(AUTHENTICATE, payload)

    async def get_profile(self):
        return await self.client.get(GET_PROFILE)
    
    async def place_order(self):
        payload = LOGIN_PAYLOAD
        return await self.client.post(PLACE_ORDER, payload)
    
    async def get_order_book(self):
        payload = LOGIN_PAYLOAD
        return await self.client.post(GET_ORDER_BOOK, payload)
    

    
    