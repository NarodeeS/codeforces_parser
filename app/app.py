import uvicorn

from api import api


if __name__ == '__main__':
    uvicorn.run(app=api,  # change to 'app:api' in prod
                host='0.0.0.0', 
                port=8000, 
                reload=False, 
                workers=2) 
