from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


DeclarativeBase = declarative_base()


task_theme = Table(
    "task_themes",
    DeclarativeBase.metadata,
    Column("task_id", ForeignKey("tasks.id"), primary_key=True),
    Column("theme_id", ForeignKey("themes.id"), primary_key=True),
)


class Task(DeclarativeBase):
    __tablename__ = 'tasks'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    number = Column(String(10), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    solved_count = Column(Integer, nullable=False)
    
    difficulty_id = Column(Integer, ForeignKey('difficulty_classifiers.id'), nullable=False)
    difficulty = relationship('DifficultyClassifier')
    
    themes = relationship('Theme', secondary=task_theme, back_populates='tasks')
    
    contest_id = Column(Integer, ForeignKey('contests.id'), nullable=True)
    contest = relationship('Contest', back_populates='tasks')


class Theme(DeclarativeBase):
    __tablename__ = 'themes'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    description = Column(String, unique=True, nullable=False)
    
    tasks = relationship('Task', secondary=task_theme, back_populates='themes')
    contests = relationship('Contest', back_populates='theme')
    
    
class DifficultyClassifier(DeclarativeBase):
    __tablename__ = 'difficulty_classifiers'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    value = Column(Integer, unique=True, nullable=False)


class Contest(DeclarativeBase):
    __tablename__ = 'contests'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    difficulty_id = Column(Integer, ForeignKey('difficulty_classifiers.id'), nullable=False)
    difficulty = relationship('DifficultyClassifier')
    
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
    theme = relationship('Theme', back_populates='contests')
    
    tasks = relationship('Task', back_populates='contest')
