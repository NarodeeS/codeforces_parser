from aiogram import types
from aiogram.dispatcher import FSMContext
from loguru import logger

from loader import dp, bot
from utils import prepare_task_message
from states.contest_settings_state import ContestSettingState
from api_crud.contests_crud import get_contests, get_contest
from api_crud.tasks_crud import get_task
from api_crud.difficulties_crud import get_difficulties
from keyboards.get_all_items_keyboard import get_all_items_keyboard
from keyboards.callback_data import *


@dp.callback_query_handler(text_contains='theme_data',
                           state=ContestSettingState.contest_theme)
async def accept_contest_theme(query: types.CallbackQuery, 
                               state: FSMContext):
    query_data = query.data.split(':')
    str_page_number = query_data[2]
    

    if str_page_number == 'None': #  touched theme
        theme = query_data[1]
        await state.update_data(theme=theme)
        
        difficulties = await get_difficulties()
        await state.update_data(difficulties=difficulties)
        await bot.send_message(query.from_user.id, 
                            'Теперь введите уровень сложности заданий',
                            reply_markup=get_all_items_keyboard(difficulty_data, 
                                                                difficulties,
                                                                current_page=1))
        
        await query.message.delete()
        await ContestSettingState.contest_difficulty.set()
        return
    
    page_number = int(str_page_number)
    data = await state.get_data()
    await query.message.edit_reply_markup(get_all_items_keyboard(theme_data, 
                                                                 data['themes'],
                                                                 current_page=page_number))
    
    await ContestSettingState.contest_theme.set()
    

@dp.callback_query_handler(text_contains='difficulty_data',
                           state=ContestSettingState.contest_difficulty)
async def accept_contest_difficulty(query: types.CallbackQuery, 
                                    state: FSMContext):
    query_data = query.data.split(':')
    str_page_number = query_data[2]
    
    if str_page_number == 'None': # touched difficulty
        difficulty = int(query_data[1].strip())
        
        await state.update_data(difficulty=difficulty)
        state_data = await state.get_data()
        await state.finish()
        
        contests = await get_contests(state_data['theme'], 
                                      state_data['difficulty'])
        if len(contests) == 0:
            await bot.send_message(query.from_user.id,
                                   'Не нашлось контестов по заданным параметрам')
            await query.message.delete()
            return

        await bot.send_message(query.from_user.id, 
                               'Выберите один из предложенных контестов',
                               reply_markup=get_all_items_keyboard(contest_data,
                                                                   contests))    
        await query.message.delete()
        return
    
    page_number = int(str_page_number)
    data = await state.get_data()
    await query.message.edit_reply_markup(get_all_items_keyboard(difficulty_data, 
                                                                 data['difficulties'],
                                                                 current_page=page_number))
    
    await ContestSettingState.contest_difficulty.set()
    

@dp.callback_query_handler(text_contains='contest_data')
async def get_contest_tasks(query: types.CallbackQuery):
    query_data = query.data.split(':')
    contest_id = int(query_data[1])
    contest = await get_contest(contest_id)
    await bot.send_message(query.from_user.id, 
                           'Выберите задание для просмотра подробностей',
                           reply_markup=get_all_items_keyboard(task_data, 
                                                               contest.tasks))
    await query.message.delete()


@dp.callback_query_handler(text_contains='task_data')
async def get_task_data(query: types.CallbackQuery):
    query_data = query.data.split(':')
    task_id = int(query_data[1])
    task = await get_task(task_id)
    await bot.send_message(query.from_user.id,
                           prepare_task_message(task))
