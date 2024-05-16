"""Обработка команды start"""
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import BotCommand, Message, CallbackQuery, FSInputFile
from models import User




router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    """Обработка команды start"""
    from main import bot
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='menu', description='Открыть меню'),
    ])
    User.get_or_create(tg_user=msg.from_user.id)
    await msg.answer_photo(caption='Здравствуй, я бот который поможет тебе подобрать аниме. \
                           \nЧтобы узнать как пользоваться ботом введите команду /help 🤖', photo=FSInputFile('to/AniVaultBotFinal.png'))
    
