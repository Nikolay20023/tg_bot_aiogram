import asyncio
from aiogram import Bot, Dispatcher
from core.config import config
from handlers import different_types, questions, group_games
from handlers import checkin, in_pm, bot_in_group


async def main():
    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_routers(
        questions.router,
        different_types.router,
        group_games.router,
        checkin.router,
        in_pm.router,
        bot_in_group.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())