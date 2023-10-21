from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.checkin import get_checkin_kb
from middlewares.weekend import WeekendCallbackMiddleware


router = Router()
router.message.filter(F.chat.type == "private")
router.message.middleware(WeekendCallbackMiddleware())


@router.message(Command("checkin"))
async def cmd_checkin(message: Message):
    await message.answer(
        "Пожалуйста, нажмите на кнопку",
        reply_markup=get_checkin_kb()
    )


@router.callback_query(F.data == "confirm")
async def checkin_confirm(message: Message):
    await message.answer(
        "Спасибо, потверждено!",
        show_alert=True
    )