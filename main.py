import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "6068900832:AAESMuQLAP5P1KlLAcjcTndF5d2qt4eSa7E"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)

@dp.message(F.audio)
async def audio(message:Message):
    audio = message.audio
    
    await message.answer("Xabar yuborildi")
    await message.answer_audio(audio.file_id)


    
#document,video, photo, audio, location, animation,video_note
#contact, game, dice, voice,media_group, poll, sticker


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
