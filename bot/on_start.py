from aiogram.types import BotCommand, BotCommandScopeDefault
from loader import bot


async def start(dp):
    await bot.set_my_commands(
        commands=[
            BotCommand("contests", "Поиск контестов"),
        ],
        scope=BotCommandScopeDefault()
    )
