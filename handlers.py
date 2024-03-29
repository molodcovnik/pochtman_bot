from aiogram import Router, F


from content import about_pochtmen, func_list, success_subscribe, success_unsubscribe, welcome_text, profile_text, \
    contacts_text
from keyboards import start_kb, get_keyboard, about_kb
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils import reg_user, unsubscribe_user

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text=welcome_text, reply_markup=start_kb, parse_mode="HTML")


@router.message(F.text.lower() == "профиль")
async def get_profile(message: Message):
    user_id = message.from_user.id
    kb = await get_keyboard(user_id)
    await message.answer(text=profile_text, reply_markup=kb, parse_mode="HTML")


@router.message(F.text.lower() == "подписаться")
async def subscribe(message: Message):
    res = await reg_user(message)
    if res == 201:
        await message.answer(text=success_subscribe, reply_markup=start_kb)
    else:
        kb = await get_keyboard(message.from_user.id)
        await message.answer(text="Ошибка, попробуйте еще раз...", reply_markup=kb)


@router.message(F.text.lower() == "отписаться")
async def unsubscribe(message: Message):
    res = await unsubscribe_user(message)
    if res == 204:
        await message.answer(text=success_unsubscribe, reply_markup=start_kb)
    else:
        kb = await get_keyboard(message.from_user.id)
        await message.answer(text="Ошибка, попробуйте еще раз...", reply_markup=kb)


@router.message(F.text.lower() == "о сервисе")
async def get_description(message: Message):
    await message.answer(text=about_pochtmen, reply_markup=about_kb, parse_mode="HTML")


@router.message(F.text.lower() == "функционал")
async def get_functions(message: Message):
    await message.answer(**func_list.as_kwargs(), reply_markup=about_kb)


@router.message(F.text.lower() == "контакты")
async def get_contacts(message: Message):

    await message.answer(text=contacts_text, reply_markup=about_kb, parse_mode="HTML")



@router.message(F.text.lower() == "назад")
async def get_back(message: Message):
    await message.answer(text="Главное меню", reply_markup=start_kb)
