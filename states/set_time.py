"""используем from для импорта aiogram """
from aiogram.fsm.state import State, StatesGroup


class SetTime(StatesGroup):
    """используем class для создания объектов """
    time = State()

