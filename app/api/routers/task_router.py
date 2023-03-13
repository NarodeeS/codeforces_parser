from fastapi import APIRouter, HTTPException, status, Depends

from db.models import Task
from ..schemas import TaskSchema
from ..get_db_session import get_db_session


task_router = APIRouter(prefix='/tasks',
                        tags=['tasks'])


@task_router.get('/{id}', response_model=TaskSchema)
def get_task(id: int, db_session = Depends(get_db_session)):
    task = db_session.query(Task).filter_by(id=id).first()
    if not task:
        raise HTTPException(detail='no task with such id', 
                            status_code=status.HTTP_404_NOT_FOUND)
    return task
