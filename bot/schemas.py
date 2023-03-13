from pydantic import BaseModel


class ThemeSchema(BaseModel):
    description: str
    

class DifficultySchema(BaseModel):
    value: int


class ContestTaskSchema(BaseModel):
    id: int
    number: str
    title: str
    solved_count: int
        

class TaskSchema(ContestTaskSchema):
    difficulty: DifficultySchema
    themes: list[ThemeSchema]


class ContestSchema(BaseModel):
    id: int
    theme: ThemeSchema
    difficulty: DifficultySchema
    tasks: list[ContestTaskSchema]
