from abc import ABC

from pydantic import BaseModel


class KeyboardItem(ABC, BaseModel):
    id: int
    
    def get_identifier(self) -> int | str:
        return self.id
    
    def get_title(self) -> str: ...


class ThemeSchema(KeyboardItem):
    description: str
    
    def get_title(self) -> str:
        return self.description
    
    def get_identifier(self) -> int | str:
        return self.description
    

class DifficultySchema(KeyboardItem):
    value: int
    
    def get_title(self) -> str:
        return str(self.value)
    
    def get_identifier(self) -> int | str:
        return self.value


class ContestTaskSchema(KeyboardItem):
    number: str
    title: str
    solved_count: int
    
    def get_title(self) -> str:
        return self.title
        

class TaskSchema(ContestTaskSchema):
    difficulty: DifficultySchema
    themes: list[ThemeSchema]


class ContestSchema(KeyboardItem):
    theme: ThemeSchema
    difficulty: DifficultySchema
    tasks: list[ContestTaskSchema]
    
    def get_title(self) -> str:
        return f'Контест {self.id}'
