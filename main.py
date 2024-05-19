"""Запуск всего бота"""
import asyncio
from aiogram import Dispatcher, Bot
from datetime import time, timedelta, datetime
import random
from peewee import fn

from handlers import include_routers
from config import TOKEN
from models import User, SentAnime,Anime
from keyboards.set_time import kb_status


bot = Bot(TOKEN)
dp = Dispatcher()
GLOBAL_VARS = {'SEND_TIME': None}

def get_random_anime_for_user(user):
    # Получаем все аниме, которые уже отправлялись пользователю
    sent_anime_ids = SentAnime.select(SentAnime.anime).where(SentAnime.user == user)
    # Извлекаем случайное аниме, которое не было отправлено пользователю
    random_anime = Anime.select().where(Anime.id.not_in(sent_anime_ids)).order_by(fn.Random()).first()
    
    if random_anime:
        # Записываем, что это аниме было отправлено пользователю
        SentAnime.create(user=user, anime=random_anime)
    
    return random_anime

async def get_time_notify():
    now = datetime.now()
    users = User.filter(User.time > now).order_by(User.time.asc())
    if users.count() > 0:
        return (users.first()).time 

async def send_admin():
    GLOBAL_VARS['SEND_TIME'] = await get_time_notify()
    await bot.send_message(1894835556, "Бот запущен!")
    while True:
        print(datetime.now().time(), GLOBAL_VARS['SEND_TIME'])
        now_time = datetime.now().time()
        now_time = time(now_time.hour, now_time.minute)
        if GLOBAL_VARS['SEND_TIME'] and GLOBAL_VARS['SEND_TIME'] == now_time:
            # рассылка уведомлений всем пользователям
            for user in User.filter(time=GLOBAL_VARS['SEND_TIME']):
                anime = get_random_anime_for_user(user)
                if anime:
                    genre = anime.Genre.Genre
                    year = anime.Years.Year
                    photo = anime.PhotoUrl.PhotoUrl
                    await bot.send_photo(user.tg_user,photo=photo,
                                         caption=f'Вот ваше аниме:\
                                                \nНазвание аниме: {anime.Anime}\
                                                \nГод выпуска аниме: {year}\
                                                \nЖанры аниме: {genre}\
                                                \nСсылка на аниме: {anime.Link}',
                                                reply_markup=kb_status)

            GLOBAL_VARS['SEND_TIME'] = await get_time_notify()
              
            print(GLOBAL_VARS['SEND_TIME'])
               
        now_time = (datetime.now() + timedelta(minutes=1))
        now_time = datetime(now_time.year, now_time.month, now_time.day, 
                            now_time.hour, now_time.minute)
        seconds = (now_time - datetime.now()).seconds + 1
        
        await asyncio.sleep(seconds)

async def update_schedule():
    while True:
        await asyncio.sleep(10)  # Проверяем каждую минуту
        new_time = await get_time_notify()
        if new_time != GLOBAL_VARS['SEND_TIME']:
            GLOBAL_VARS['SEND_TIME'] = new_time

async def on_startup():
    asyncio.create_task(send_admin())
    asyncio.create_task(update_schedule())
async def main():
    dp.startup.register(on_startup)
    include_routers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
