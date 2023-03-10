from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


DeclarativeBase = declarative_base()


class Task(DeclarativeBase):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    number = Column(Text(10), unique=True, nullable=False)
    title = Column(Text(255), unique=True, nullable=False)
    difficulty = Column(Integer, nullable=False)
    solved_count = Column(Integer, nullable=False)
    
    task_id = Column(Integer, ForeignKey('task_types.id'), nullable=False)
    task_type = relationship('TaskType', back_populates='tasks')
    
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
    theme = relationship('Theme', back_populates='tasks')


class Theme(DeclarativeBase):
    __tablename__ = 'themes'
    
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)
    
    tasks = relationship('Task', back_populates='theme')
    contests = relationship('Contest', back_populates='theme')
    

class TaskType(DeclarativeBase):
    __tablename__ = 'task_types'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(Text, unique=True, nullable=False)
    tasks = relationship('Task', back_populates='task_type')


class Contest(DeclarativeBase):
    __tablename__ = 'contests'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    difficulty = Column(Integer, nullable=False)
    
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
    theme = relationship('Theme', back_populates='contests')
