from typing import TypeAlias
from itertools import product

from db.base import Session
from db.models import Task, Theme, DifficultyClassifier, Contest


CONTEST_SIZE = 10


ResultDictType: TypeAlias = dict[tuple[Theme, DifficultyClassifier], list[Task]]


def allocate_contests():
    with Session() as db_session:
        all_themes = db_session.query(Theme).all()
        all_difficulties = db_session.query(DifficultyClassifier).all()
        suitable_tasks = db_session.query(Task).filter_by(contest_id=None)
                
        themes_and_difficulties = list(product(all_themes, all_difficulties))
        
        result: ResultDictType = {(theme, difficulty):list()
                                  for theme, difficulty in themes_and_difficulties}
        
        picked_tasks = []
        for theme, difficulty in themes_and_difficulties:
            current_tasks = result[(theme, difficulty)]
            for task in suitable_tasks:
                if (task.difficulty.value == difficulty.value
                    and theme in task.themes 
                    and task not in picked_tasks):
                    
                    current_tasks.append(task)
                    picked_tasks.append(task)
        
        for (theme, difficulty), tasks in result.items():
            tasks_slices = [tasks[i:i+CONTEST_SIZE] 
                            for i in range(0, len(tasks), CONTEST_SIZE)]
            for contest_tasks in tasks_slices:
                if len(contest_tasks) == CONTEST_SIZE:
                    contest = Contest(difficulty=difficulty, 
                                      theme=theme, 
                                      tasks=contest_tasks)
                    db_session.add(contest)
        
        db_session.commit()
