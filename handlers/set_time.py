"""используем from для импорта aiogram """
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.set_time import SetTime
from models import User
from datetime import time
router = Router()

@router.message(Command("set_time"))
async def set_time_handler(msg: Message, state: FSMContext):
    """мы используем async def для определения функции"""
    await msg.answer("Введите время в формате чч:мм для рассылки аниме")
    await state.set_state(SetTime.time)

@router.message(SetTime.time)
async def set_time_by_notification_handler(msg: Message, state: FSMContext):
    """мы используем async def для определения функции"""
    from main import GLOBAL_VARS

    user_id = msg.from_user.id
    time_str = msg.text
    try:
        # Парсинг времени
        hours, minutes = map(int, time_str.split(':'))
        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError

        # Сохранение времени пользователя в базе данных
        user, created = User.get_or_create(tg_user=user_id)
        user.time = time_str
        user.save()

        await msg.answer(f"Время {time_str} успешно сохранено для пользователя {user_id}.")
        state.clear
    except ValueError:
        await msg.answer("Некорректный формат времени. Пожалуйста, введите время в формате чч:мм.")