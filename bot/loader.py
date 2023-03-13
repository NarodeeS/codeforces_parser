import os

from aiogram import Bot, Dispatcher


BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    exit(1)


bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot=bot)
