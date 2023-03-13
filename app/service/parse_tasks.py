import time
from typing import TypeAlias

import httpx
from bs4 import BeautifulSoup

from api.schemas import TaskBaseSchema
from db.models import Task, Theme, DifficultyClassifier
from db.base import Session


URL_TEMPLATE = 'https://codeforces.com/problemset/page/{}?order=BY_SOLVED_DESC'

ParseResult: TypeAlias = tuple[list[TaskBaseSchema], 
                               dict[TaskBaseSchema, list[str]]]

TaskData: TypeAlias = tuple[TaskBaseSchema, list[str]]


def _try_create_difficulty_classifier(value: int) -> None:
    with Session() as db_session:
        if not bool(db_session.query(DifficultyClassifier)
                              .filter_by(value=value)
                              .first()):
            db_session.add(DifficultyClassifier(value=value))
            db_session.commit()


def _try_create_themes(themes: list[str]) -> None:
    with Session() as db_session:
        theme_exists = [bool(db_session.query(Theme)
                                       .filter_by(description=theme)
                                       .first())
                        for theme in themes 
        ]
        
        for i in range(len(themes)):
            if not theme_exists[i]:
                db_session.add(Theme(description=themes[i]))
        
        db_session.commit()


def _process_task(task_data: TaskData) -> None:
    new_task, themes = task_data
    _try_create_themes(themes)
    
    with Session() as db_session:    
        task_themes = (db_session.query(Theme)
                                 .filter(Theme.description.in_(themes)))
        
        _try_create_difficulty_classifier(new_task.difficulty)
        task_difficulty = (db_session.query(DifficultyClassifier)
                                     .filter_by(value=new_task.difficulty)
                                     .first())
        
        del new_task.difficulty
        
        task = Task(**new_task.dict(), 
                    difficulty=task_difficulty, 
                    themes=list(task_themes))
        
        if not bool(db_session.query(Task).filter_by(number=task.number).first()):
            db_session.add(task)
            db_session.commit()


def _parse_page(url: str) -> ParseResult:
    response = httpx.get(url)
    page_soup = BeautifulSoup(response.text, 'html.parser')
    problems_table = page_soup.find('table', class_='problems')
    problems = problems_table.find_all('tr')  # type: ignore
    
    tasks = []
    task_themes = {}
    for problem in problems:
        try:
            rows = problem.find_all('td')
            number = rows[0].find('a').string.strip()
            title = rows[1].find('div').find('a').string.strip()
            themes = [theme.string for theme in rows[1].find_all('div')[1].find_all('a')] 
            difficulty = int(rows[3].find('span').string)
            solved_count = int(rows[4].find('a').contents[-1].replace('x', '').strip())
            new_task = TaskBaseSchema(number=number, 
                                      title=title, 
                                      difficulty=difficulty, 
                                      solved_count=solved_count)
            tasks.append(new_task)
            task_themes[new_task] = themes
        except ValueError:  # validation error
            continue
        
        except Exception as err:
            print(err)
    
    time.sleep(2)  #  small delay to bypass the vian
            
    return (tasks, task_themes)


def parse_tasks() -> None:
    first_page_url = URL_TEMPLATE.format(1)
    first_page_response = httpx.get(first_page_url)
    first_page_soup = BeautifulSoup(first_page_response.text, 'html.parser')
    page_indexes_elements = first_page_soup.find_all('span', class_='page-index')
    last_page = int(page_indexes_elements[-1].get('pageindex'))
    
    urls = []
    for page_number in range(1, last_page+1):
        urls.append(URL_TEMPLATE.format(page_number))
    
    results = map(_parse_page, urls)
    
    for result in results:
        tasks, tasks_themes = result
        for task_data in zip(tasks, tasks_themes.values()):
            _process_task(task_data)
