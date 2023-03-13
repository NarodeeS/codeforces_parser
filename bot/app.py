from aiogram import executor

from loader import dp
from on_start import start
from handlers.commands_handlers import *
from handlers.contests_search_handlers import *


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, on_startup=start)
    