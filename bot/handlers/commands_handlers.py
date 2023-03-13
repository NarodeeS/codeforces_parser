from aiogram.dispatcher.filters import Command
from aiogram import types

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
async def start_contest_settings(message: types.Message):
    themes = await get_themes()
    await bot.send_message(message.from_id,
                           'Выберите одну из тем',
                           reply_markup=get_all_items_keyboard(theme_data, 
                                                               themes))
    await ContestSettingState.contest_theme.set()
