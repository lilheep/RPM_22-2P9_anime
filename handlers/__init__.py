"""используем from для импорта aiogram """
from aiogram import Dispatcher
from handlers import start, set_time, help


def include_routers(dp: Dispatcher):
    """определяем функцию"""
    dp.include_routers(
        start.router,
        set_time.router,
        help.router
    )
