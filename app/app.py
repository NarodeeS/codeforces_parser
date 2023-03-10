import uvicorn

from api import api
from db.utils import wait_unlesss_db_started
from db.models import DeclarativeBase
from db.base import engine


if __name__ == '__main__':
    wait_unlesss_db_started()
    DeclarativeBase.metadata.create_all(bind=engine)
    
    uvicorn.run(app=api,  # change to 'app:api' in prod
                host='0.0.0.0', 
                port=8000) 
