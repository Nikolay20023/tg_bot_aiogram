import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from core.config import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token, parse_mode="HTML")

dp = Dispatcher()


# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет")


@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


@dp.message(Command("test2"))
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="С пюрешкой")],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@dp.message(Command("test3"))
async def cmd_test3(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode=None)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
