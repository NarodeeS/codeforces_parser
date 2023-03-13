import os

import aiohttp
from pydantic import parse_obj_as

from schemas import ThemeSchema


API_URL = os.getenv('API_URL')


async def get_themes() -> list[ThemeSchema]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}/themes/') as response:
            return parse_obj_as(list[ThemeSchema], await response.json())
