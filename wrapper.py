from .client import AngelClient
from .endpoints import PLACE_ORDER, GET_ORDER_BOOK, GET_PROFILE

class AngelAPIWrapper:
    def __init__(self):
        self.client = AngelClient()

        async def get_profile(self):
            return await self.client.get(GET_PROFILE)