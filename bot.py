import asyncio
import logging

from aiogram import Bot, Dispatcher
from core.config import config
from handlers import different_types, questions, group_games, events_in_group
from handlers import checkin, in_pm, bot_in_group, admin_changes_in_group
from handlers import ordering_dfood


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    bot = Bot(token=config.bot_token)
    dp = Dispatcher()

    dp.include_routers(
        questions.router,
        different_types.router,
        group_games.router,
        checkin.router,
        in_pm.router,
        bot_in_group.router,
        admin_changes_in_group.router,
        events_in_group.router,
        ordering_dfood.router
    )
    

    admins = await bot.get_chat_administrators(config.chat_id)
    admins_id = {admin.user.id for admin in admins}
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, admins=admins_id)


if __name__ == "__main__":
    asyncio.run(main())
