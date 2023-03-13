from typing import TypeVar

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from schemas import KeyboardItem
from .add_control_buttons import add_control_buttons
from .utils import get_indexes
from . import PAGE_SIZE


T = TypeVar('T', bound=KeyboardItem)


def get_all_items_keyboard(callback_data: CallbackData, 
                           items: list[T], 
                           current_page=None) -> InlineKeyboardMarkup:
    inline_keyboard = []
    start_index, end_index = ((0, len(items)-1) 
                              if current_page is None 
                              else get_indexes(items, current_page, PAGE_SIZE))
    
    for i in range(start_index, end_index+1):
        item = items[i]
        
        params = {
            'id': item.get_identifier()
        }
        
        if current_page is not None:
            params['page_number'] = 'None'
        inline_keyboard.append(
            [InlineKeyboardButton(item.get_title(), 
                                  callback_data=callback_data.new(**params))]
        )
    
    if current_page is None:
        return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    add_control_buttons(keyboard, 
                        items, 
                        callback_data, 
                        {'id': 'None'}, 
                        current_page)
    return keyboard    
