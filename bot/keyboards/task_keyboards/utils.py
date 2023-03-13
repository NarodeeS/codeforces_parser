from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from schemas import ContestTaskSchema
from ..callback_data.task_data import task_data


def get_tasks_keyboard(tasks: list[ContestTaskSchema]) -> InlineKeyboardMarkup:
    inline_keyboard = []
    
    for task in tasks:
        inline_keyboard.append(
            [InlineKeyboardButton(task.title, 
                                  callback_data=task_data.new(task_id=task.id))]
        )
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
