"""Запуск всего бота"""
import asyncio
from aiogram import Dispatcher, Bot
from handlers import include_routers
from datetime import time, timedelta, datetime
from config import TOKEN
from models import User


bot = Bot(TOKEN)
dp = Dispatcher()

GLOBAL_VARS = {'SEND_TIME': None}

async def get_time_notify():
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time 

async def send_admin():
    GLOBAL_VARS['SEND_TIME'] = await get_time_notify()
    await bot.send_message(1894835556, "Бот запущен!")
    while True:
        
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if GLOBAL_VARS['SEND_TIME'] and GLOBAL_VARS['SEND_TIME'] == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=GLOBAL_VARS['SEND_TIME']):
                await bot.send_message(user.tg_user, 'чири чири')

            GLOBAL_VARS['SEND_TIME'] = await get_time_notify()
              

               
        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day, 
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1

        await asyncio.sleep(seconds)

async def on_startup():
    asyncio.create_task(send_admin())

async def main():
    '''Старт бота'''
    dp.startup.register(on_startup)
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
