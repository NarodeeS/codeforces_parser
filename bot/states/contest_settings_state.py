from aiogram.dispatcher.filters.state import StatesGroup, State


class ContestSettingState(StatesGroup):
    contest_theme = State()
    contest_difficulty = State()
