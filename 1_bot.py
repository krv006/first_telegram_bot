import asyncio
import logging
import sys
# from os import getenv

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, FSInputFile

# from aiogram.utils.markdown import hbold
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6486896121:AAHXOONfeCinTCCkYgukqD9wGgs0fufr9QY"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

router = Router()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = [
        [KeyboardButton(text="Aloqa"),
         KeyboardButton(text="Test"),
         KeyboardButton(text="Ovqatlar"), ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Xush kelibsiz, {message.from_user.full_name}",
                           reply_markup=markup)


@router.message(F.text == "Aloqa")
async def echo_handler(message: types.Message) -> None:
    photo = FSInputFile("dispatcher-flat-icon-vector-16074191.jpg")
    msg = await bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption="<b>Telefon:</b> +998902646366\n<b>Manzil:</b> Mirzo Ulug'bek tumani",
        parse_mode="HTML")
    print(msg)


@router.message(F.text == "Ovqatlar")
async def echo_handler(message: types.Message) -> None:
    keyboard = [
        [KeyboardButton(text="Suyuq ovqatlar"),
         KeyboardButton(text="Quyuq ovqatlar"),
         KeyboardButton(text="Ichimliklar"),
         KeyboardButton(text="Orqaga qaytish")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Qanday ovqat xoxlaysiz , {message.from_user.full_name}",
                           reply_markup=markup)

    photo = FSInputFile("woman-call-center-icon-simple-style-vector-32225284.jpg")
    msg = await bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption="<b>Telefon:</b> +998902646366\n<b>Narxi:</b> Mirzo Ulug'bek tumani",
        parse_mode="HTML")
    print(msg)


@router.message(F.text == "Suyuq ovqatlar")
async def echo_handler(message: types.Message) -> None:
    keyboard = [
        [KeyboardButton(text="Sho'rva"),
         KeyboardButton(text="Mastava"),
         KeyboardButton(text="Chuchvara"),
         KeyboardButton(text="Ovqatlar MENU bolimiga qaytish")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Ovqatlarimizdan birini tanlang, {message.from_user.full_name}",
                           reply_markup=markup)


@router.message(F.text == "Sho'rva")
async def echo_handler(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Siz buyurtma bergan taomingiz")
    photo = FSInputFile("maxresdefault.jpg")
    msg = await bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption="<b>Taom nomi:</b> SHo'rva\n<b>Narxi:</b> 26 000",
        parse_mode="HTML")
    print(msg)


@router.message(F.text == "Mastava")
async def echo_handler(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Siz buyurtma bergan taomingiz")
    photo = FSInputFile("maxresdefault (1).jpg")
    msg = await bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption="<b>Taom nomi:</b> Mastava\n<b>Narxi:</b> 26 000",
        parse_mode="HTML")
    print(msg)


@router.message(F.text == "Chuchvara")
async def echo_handler(message: types.Message) -> None:
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Siz buyurtma bergan taomingiz")
    photo = FSInputFile("download.jpeg")
    msg = await bot.send_photo(
        message.from_user.id,
        photo=photo,
        caption="<b>Taom nomi:</b> Chuchvara\n<b>Narxi:</b> 26 000",
        parse_mode="HTML")
    print(msg)


@router.message(F.text == "Ovqatlar MENU bolimiga qaytish")
async def echo_handler(message: types.Message) -> None:
    keyboard = [
        [KeyboardButton(text="Suyuq ovqatlar"),
         KeyboardButton(text="Quyuq ovqatlar"),
         KeyboardButton(text="Ichimliklar"), ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Ovqatlarimizdan birini tanlang, {message.from_user.full_name}",
                           reply_markup=markup)


@router.message(F.text == "Orqaga qaytish")
async def echo_handler(message: types.Message) -> None:
    keyboard = [
        [KeyboardButton(text="Aloqa"),
         KeyboardButton(text="Test"),
         KeyboardButton(text="Ovqatlar"), ]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Orqaga qaytdingiz, {message.from_user.full_name}",
                           reply_markup=markup)


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
