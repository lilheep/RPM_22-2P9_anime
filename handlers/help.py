"""Обработка команды start"""
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command('help'))
async def help_hanler(msg: Message):
    """Выполненине по команде help"""
    await msg.answer(text='\nДля того чтобы бот заработал установите время рассылки аниме\
                    \nСписок команд:\
                    \n/set_time - команда, введя которую можно укстановить время рассылки\
                    \n/random - команда, введя ее вы получить одно случайное аниме;\
                    \n/menu - команда, которая открывать меню.\
                    \n Если возникли проблемы с ботом обращайтесь в поддержку https://t.me/whounek')
