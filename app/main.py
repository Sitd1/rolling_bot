"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from app.config.settings import config

from app.services.bot_service.commands.roll import roll_dice
from app.services.bot_service.commands.start import start_router
from app.services.bot_service.commands.help import help_router
from app.services.bot_service.commands.roll import roll_router
from app.services.bot_service.commands.bot_commands import bot_commands


async def start_bot():
    """This function will start bot with polling mode."""
    logging.basicConfig(level=logging.DEBUG)

    commands_for_bot = [
        BotCommand(command=cmd[0], description=cmd[1]) for cmd in bot_commands
    ]

    dp = Dispatcher()

    dp.include_routers(
        start_router,
        help_router,
        roll_router,
    )

    bot = Bot(
        token=config.tg.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    # регистрация комманд - в боте показываются комманды
    await bot.set_my_commands(commands_for_bot)

    # logging.basicConfig(level=conf.logging_level)

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
    )


if __name__ == "__main__":
    asyncio.run(start_bot())
