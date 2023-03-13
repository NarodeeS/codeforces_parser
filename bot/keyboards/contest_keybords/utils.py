from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from schemas import ContestSchema
from .contest_callback_data import contest_data


def get_contests_keyboard(contests: list[ContestSchema]) -> InlineKeyboardMarkup:
    inline_keyboard = []
    
    # maybe add page-by-page transition
    for contest in contests:
        inline_keyboard.append(
            [InlineKeyboardButton(text=f'Контест {str(contest.id)}', 
                                  callback_data=contest_data.new(contest_id=contest.id))]
        )
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
