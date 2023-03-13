from fastapi import FastAPI

from .routers.contest_router import contest_router
from .routers.task_router import task_router


api = FastAPI(title='Codeforces tasks API',
              description='API for getting task information from codeforces')


api.include_router(contest_router, prefix='/api')
api.include_router(task_router, prefix='/api')
