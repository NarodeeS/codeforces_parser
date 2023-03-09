from fastapi import FastAPI

api = FastAPI(title='Codeforces tasks API',
              description='API for getting task information from codeforces')


@api.get('/')
async def home():
    return {'message': 'Hello, FastAPI'}
