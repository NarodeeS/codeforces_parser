import os

import aiohttp

from schemas import TaskSchema


API_URL = os.getenv('API_URL')


async def get_task(id: int) -> TaskSchema:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{API_URL}/tasks/{id}') as response:
            return TaskSchema.parse_obj(await response.json())
