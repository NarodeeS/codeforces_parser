from fastapi import APIRouter, Depends, HTTPException, status

from db.models import DifficultyClassifier
from ..schemas import DifficultySchema
from ..get_db_session import get_db_session


difficulty_router = APIRouter(prefix='/difficulties', 
                              tags=['difficulties'])


@difficulty_router.get('/', response_model=list[DifficultySchema])
def get_all_difficulties(db_session = Depends(get_db_session)):
    return db_session.query(DifficultyClassifier).all()


@difficulty_router.get('/{id}', response_model=DifficultySchema)
def get_difficulty(id: int, db_session = Depends(get_db_session)):
    difficulty = db_session.query(DifficultyClassifier).filter_by(id=id).first()
    if not difficulty:
        raise HTTPException(detail='no difficulty with such id', 
                            status_code=status.HTTP_404_NOT_FOUND)        
    return difficulty
