from fastapi import APIRouter, HTTPException, status, Depends

from db.models import Contest, Theme, DifficultyClassifier
from ..schemas import ContestReturnSchema
from ..get_db_session import get_db_session


contest_router = APIRouter(prefix='/contests', 
                           tags=['contests'])


@contest_router.get('/', 
                    response_model=list[ContestReturnSchema])
def get_contests(theme: str, difficulty: int, 
                 db_session = Depends(get_db_session)):
    result = list(db_session.query(Contest)
                            .join(Theme)
                            .join(DifficultyClassifier)
                            .filter(Theme.description == theme)
                            .filter(DifficultyClassifier.value == difficulty))
    return list(result)


@contest_router.get('/{id}', response_model=ContestReturnSchema)
def get_contest(id: int, db_session = Depends(get_db_session)):
    contest = db_session.query(Contest).filter_by(id=id).first()
    if not contest:
        raise HTTPException(detail='no contest with such id', 
                            status_code=status.HTTP_404_NOT_FOUND)

    return contest
