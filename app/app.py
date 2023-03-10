import uvicorn

from api import api
from db.models import DeclarativeBase
from db.base import async_engine


if __name__ == '__main__':
    DeclarativeBase.metadata.create_all(bind=async_engine)
    
    uvicorn.run(app=api,  # change to 'app:api' in prod
                host='0.0.0.0', 
                port=8000) 
