import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, FSMI18nMiddleware

from factor_bok.admin import admin_router
from factor_bok.config import TOKEN, database
from factor_bok.contact import contact_router
from factor_bok.handler import user_router
from factor_bok.help import help_router
from factor_bok.inline_mode import inline_mode_router


dp = Dispatcher()


async def on_startup(bot: Bot) -> None:
    if not database.get('categories'):
        database['categories'] = {}
    if not database.get('products'):
        database['products'] = {}
    if not database.get('users'):
        database['users'] = {}
    if not database.get('basket'):
        database['basket'] = {}
    if not database.get('order_user'):
        database['order_user'] = {}
    if not database.get('order_count'):
        database['order_count'] = 0


    command_list = [
        BotCommand(command='start', description='to start bot'),
        BotCommand(command='help', description='help')
    ]
    await bot.set_my_commands(command_list)




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    i18n = I18n(path="locales", default_locale="en", domain="messages")
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))
    dp.startup.register(on_startup)
    dp.include_routers(admin_router, user_router, contact_router, help_router, inline_mode_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
