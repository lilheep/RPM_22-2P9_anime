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
    await state.set_state(SetTime.time)
    await msg.answer(text="Выберите время в формате чч:мм для рассылки аниме")


@router.message(SetTime.time)
async def set_time_by_notification_handler(msg: Message, state: FSMContext):
    """мы используем async def для определения функции"""
    from main import GLOBAL_VARS
    User.get_or_create(time=state)
    await state.clear()
