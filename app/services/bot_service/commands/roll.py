"""This file represents a start logic."""


from aiogram import Router, types
from aiogram.filters import Command
from app.services.bot_service.utils.roll_func import roll_dice, get_yes_or_no, get_coin

roll_router = Router(name="roll")


@roll_router.message(Command(commands="roll"))
async def roll_cmd(message: types.Message):
    """Help command handler."""
    text = message.text
    # try:
    #     stop_value = int(text.split()[-1])
    # except Exception:
    #     return await message.answer(
    #         f'Напишите в формате "/roll 100", где "100" ваше число, число должно быть целым и меньше 10_000')

    try:
        value = roll_dice()
        # if not stop_value:
        #     value = roll_dice(stop=stop_value)
        # else:
        #
        return await message.answer(f"{value}")
    except Exception as e:
        return await message.answer(f'{e}')


@roll_router.message(Command(commands="yes_no"))
async def yes_or_no_cmd(message: types.Message):
    """Help command handler."""
    value = get_yes_or_no()
    return await message.answer(f"{value}")

@roll_router.message(Command(commands="coin"))
async def yes_or_no_cmd(message: types.Message):
    """Help command handler."""
    value = get_coin()
    return await message.answer(f"{value}")


@roll_router.message(Command("dice"))
async def handle_roll(message: types.Message):
    # Отправляем кубик, ждем результата
    sent_message = await message.reply_dice(emoji="🎲") # "🎲" - стандартный кубик
    # sent_message.dice.value содержит число (1-6)
    await message.reply(f"Выпало: {sent_message.dice.value} 🎲")
