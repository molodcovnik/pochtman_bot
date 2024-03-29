from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from utils import check_user_reg

start_buttons = [
    KeyboardButton(text="Профиль"),
    KeyboardButton(text="О сервисе"),
]

start_kb = ReplyKeyboardMarkup(
    keyboard=[start_buttons],
    resize_keyboard=True,
)

about_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Функционал"), KeyboardButton(text="Контакты"),],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)


desc_kb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Функционал"),
        KeyboardButton(text="Отмена"),
    ]],
    resize_keyboard=True
)


async def get_keyboard(user_id):
    if await check_user_reg(user_id):
        profile_kb = ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text="Отписаться"),
                KeyboardButton(text="Назад"),
            ]],
            resize_keyboard=True
        )
    else:
        profile_kb = ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text="Подписаться"),
                KeyboardButton(text="Назад"),
            ]],
            resize_keyboard=True
        )

    return profile_kb
