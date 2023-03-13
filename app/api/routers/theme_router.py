from fastapi import APIRouter, Depends, HTTPException, status

from db.models import Theme
from ..schemas import ThemeSchema
from ..get_db_session import get_db_session


theme_router = APIRouter(prefix='/themes',
                         tags=['themes'])


@theme_router.get('/', response_model=list[ThemeSchema])
def get_all_themes(db_session = Depends(get_db_session)):
    return db_session.query(Theme).all()


@theme_router.get('/{id}', response_model=ThemeSchema)
def get_theme(id: int, db_session = Depends(get_db_session)):
    theme = db_session.query(Theme).filter_by(id=id).first()
    if not theme:
        raise HTTPException(detail='no theme with such id', 
                            status_code=status.HTTP_404_NOT_FOUND)        
    return theme
