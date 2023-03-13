from typing import TypeVar

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from schemas import KeyboardItem


T = TypeVar('T', bound=KeyboardItem)


def get_all_items_keyboard(callback_data: CallbackData, items: list[T]) -> InlineKeyboardMarkup:
    inline_keyboard = []
    
    for item in items:
        inline_keyboard.append(
            [InlineKeyboardButton(item.get_title(), 
                                  callback_data=callback_data.new(id=item.get_identifier()))]
        )
    
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
