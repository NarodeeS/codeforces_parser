from fastapi import FastAPI

from .routers.contest_router import contest_router
from .routers.task_router import task_router
from .routers.theme_router import theme_router
from .routers.difficulty_router import difficulty_router


openapi_tags = [
    {
        'name': 'contests',
        'description': 'Operations with contests'
    },
    {
        'name': 'tasks',
        'description': 'Operations with tasks'
    },
    {
        'name': 'themes',
        'description': 'Operations with themes'
    },
    {
        'name': 'difficulties',
        'description': 'Operations with difficulties'    
    }
]

api = FastAPI(title='Codeforces tasks API',
              description='API for getting tasks information from codeforces',
              openapi_tags=openapi_tags)


api.include_router(contest_router, prefix='/api')
api.include_router(task_router, prefix='/api')
api.include_router(theme_router, prefix='/api')
api.include_router(difficulty_router, prefix='/api')
