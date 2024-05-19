from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_status = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✔', callback_data='like'),InlineKeyboardButton(text='❌',callback_data='dislike')]])