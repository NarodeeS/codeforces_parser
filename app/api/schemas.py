from pydantic import BaseModel


class TaskBaseSchema(BaseModel):
    number: str
    title: str
    difficulty: int
    solved_count : int
    contest_id: int | None = None
    
    class Config:
        orm_mode = True
        frozen = True
