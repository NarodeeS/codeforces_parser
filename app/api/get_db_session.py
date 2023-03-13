from db.base import Session


def get_db_session():
    session = Session()
    try:
        yield session
    finally: 
        session.close()
