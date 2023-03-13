from aiogram.dispatcher import FSMContext
from aiogram import types

from loader import dp, bot
from utils import prepare_task_message
from states.contest_settings_state import ContestSettingState
from api_crud.contests_crud import get_contests, get_contest
from api_crud.tasks_crud import get_task
from keyboards.contest_keybords.utils import get_contests_keyboard
from keyboards.task_keyboards.utils import get_tasks_keyboard


@dp.message_handler(state=ContestSettingState.contest_theme)
async def accept_contest_theme(message: types.Message, state: FSMContext):
    await state.update_data(theme=message.text)
    await message.answer('Теперь введите уровень сложности заданий')
    await ContestSettingState.contest_difficulty.set()
    

@dp.message_handler(state=ContestSettingState.contest_difficulty)
async def accept_contest_difficulty(message: types.Message, state: FSMContext):
    try:
        difficulty = int(message.text)
    except ValueError:
        await message.answer('Некорректная сложность!')
        return
    await state.update_data(difficulty=difficulty)
    state_data = await state.get_data()
    await state.finish()
    
    contests = await get_contests(state_data['theme'], state_data['difficulty'])
    if len(contests) == 0:
        await message.answer('Не нашлось контестов по заданным параметрам')
        return
    await bot.send_message(message.from_id, 
                           'Выберите один из предложенных контестов',
                           reply_markup=get_contests_keyboard(contests))


@dp.callback_query_handler(text_contains='contest_data')
async def get_contest_tasks(query: types.CallbackQuery):
    query_data = query.data.split(':')
    contest_id = int(query_data[1])
    contest = await get_contest(contest_id)
    await bot.send_message(query.from_user.id, 
                           'Выберите задание для просмотра подробностей',
                           reply_markup=get_tasks_keyboard(contest.tasks))


@dp.callback_query_handler(text_contains='task_data')
async def get_task_data(query: types.CallbackQuery):
    query_data = query.data.split(':')
    task_id = int(query_data[1])
    task = await get_task(task_id)
    await bot.send_message(query.from_user.id,
                           prepare_task_message(task))
    