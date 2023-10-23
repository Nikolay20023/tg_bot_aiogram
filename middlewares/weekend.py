from datetime import datetime
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


def is_weekend() -> bool:
    return datetime.utcnow().weekday() in (1, 2)


class WeekendMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        events: Message,
        data: Dict[str, Any]
    ):
        if not is_weekend():
            return await handler(events, data)


class WeekendCallbackMiddleware():
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        events: Message,
        data: Dict[str, Any]
    ):
        if is_weekend():
            return await handler(events, data)

        await events.answer(
            "Бот по выходным не работает",
            show_alert=True
        )

        return
