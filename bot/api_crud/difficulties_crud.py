import os

import aiohttp
from pydantic import parse_obj_as

from schemas import DifficultySchema


API_URL = os.getenv('API_URL')


async def get_difficulties() -> list[DifficultySchema]:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}/difficulties/') as response:
            return parse_obj_as(list[DifficultySchema], await response.json())
