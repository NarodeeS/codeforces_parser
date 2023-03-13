from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp
from states.contest_settings_state import ContestSettingState


@dp.message_handler(Command("start"))
async def show_start_message(message: types.Message):
    await message.answer(('Добро пожаловать! Выберите команду /contests'
                          ' для получения контестов'))


@dp.message_handler(Command('contests'))
async def start_contest_settings(message: types.Message):
    await message.answer('Введите интересующую вас тему')
    await ContestSettingState.contest_theme.set()
