import os

import aiohttp
from pydantic import parse_obj_as

from schemas import ContestSchema


API_URL = os.getenv('API_URL')


async def get_contests(theme: str, difficulty: int) -> list[ContestSchema]:
    params = {
        'theme': theme,
        'difficulty': difficulty
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}/contests/', params=params) as response:
            return parse_obj_as(list[ContestSchema], await response.json())


async def get_contest(id: int) -> ContestSchema:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}/contests/{id}/') as response:
            return ContestSchema.parse_obj(await response.json())

