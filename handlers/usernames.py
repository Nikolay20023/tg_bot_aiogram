from typing import List

from aiogram import F, Router
from aiogram.types import Message

from filters.find_username import HasUsernameFilter


router = Router()


@router.message(
    F.text,
    HasUsernameFilter()
)
async def message_with_text(
    message: Message,
    username: List[str]
):
    await message.reply(
        f"Спасибо, обязательно подпишусь на"
        f'{", ".join(username)}'
    )
