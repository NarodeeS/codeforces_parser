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
    

class ThemeSchema(BaseModel):
    description: str
    
    class Config:
        orm_mode = True
    

class DifficultySchema(BaseModel):
    value: int
    
    class Config:
        orm_mode = True


class ContestTaskSchema(BaseModel):
    id: int
    number: str
    title: str
    solved_count: int
    
    class Config:
        orm_mode = True
        

class TaskSchema(ContestTaskSchema):
    difficulty: DifficultySchema
    themes: list[ThemeSchema]


class ContestReturnSchema(BaseModel):
    id: int
    theme: ThemeSchema
    difficulty: DifficultySchema
    tasks: list[ContestTaskSchema]
    
    class Config:
        orm_mode = True
