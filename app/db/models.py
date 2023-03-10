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
    
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    number = Column(String(10), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    difficulty = Column(Integer, nullable=False)
    solved_count = Column(Integer, nullable=False)
    
    themes = relationship('Theme', secondary=task_theme, back_populates='tasks')
    
    contest_id = Column(Integer, ForeignKey('contests.id'), nullable=True)
    contest = relationship('Contest', back_populates='tasks')


class Theme(DeclarativeBase):
    __tablename__ = 'themes'
    
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    description = Column(String, unique=True, nullable=False)
    
    tasks = relationship('Task', secondary=task_theme, back_populates='themes')
    contests = relationship('Contest', back_populates='theme')


class Contest(DeclarativeBase):
    __tablename__ = 'contests'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    difficulty = Column(Integer, nullable=False)
    
    theme_id = Column(Integer, ForeignKey('themes.id'), nullable=False)
    theme = relationship('Theme', back_populates='contests')
    
    tasks = relationship('Task', back_populates='contest')
