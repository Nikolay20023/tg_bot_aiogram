from aiogram import Router, F
from aiogram.types import Message


router = Router()


# @router.message(F.text)
# async def message_with_text(message: Message):
#     await message.answer("Это текствовое сообщение!")


@router.message(F.sticker)
async def message_with_text(message: Message):
    await message.answer("Это СТИКЕР!!!")


@router.message(F.animation)
async def message_with_text(message: Message):
    await message.answer("Это GIF!")