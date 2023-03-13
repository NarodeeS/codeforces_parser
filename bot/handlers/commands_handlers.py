from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from states.contest_settings_state import ContestSettingState
from api_crud.themes_crud import get_themes
from keyboards.get_all_items_keyboard import get_all_items_keyboard
from keyboards.callback_data import theme_data


@dp.message_handler(Command("start"))
async def show_start_message(message: types.Message):
    await message.answer(('Добро пожаловать! Выберите команду /contests'
                          ' для получения контестов'))


@dp.message_handler(Command('contests'))
async def start_contest_settings(message: types.Message, state: FSMContext):
    themes = await get_themes()
    
    if len(themes) == 0:
        await message.answer('Темы не найдены')
        return
    
    await state.update_data(themes=themes)
    await state.update_data(current_page=1)
    
    await bot.send_message(message.from_id,
                           'Выберите одну из тем',
                           reply_markup=get_all_items_keyboard(theme_data, 
                                                               themes,
                                                               current_page=1))
    await ContestSettingState.contest_theme.set()
