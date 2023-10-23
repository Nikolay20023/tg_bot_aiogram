from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.for_questions import key_yes_no_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Вы довольны своей работой",
        reply_markup=key_yes_no_kb()
    )


@router.message(F.text.lower() == "yes")
async def answer_yes(message: Message):
    await message.answer(
        "Это здорово!",
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text.lower() == "no")
async def answer_no(message: Message):
    await message.answer(
        "Жаль...",
        reply_markup=ReplyKeyboardRemove()
    )
