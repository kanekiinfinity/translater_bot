import logging
from googletrans import Translator

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6504569612:AAFxj8umi8lZZsB4-RTZidutSchM1pRHpzQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Music botimizga xush kelibsiz

    Yordam kerak bo'lsa (/help) deb yozishingiz mumkin""")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("""Bizning botimiz haqida malumot olmoqchi bo'lsangiz
    (/malumotlar) deb yozing

    Bot kodi haqida bilmoqchi bo'lsangiz (/code) deb yozing

     Bot yaratuvchisi haqida esa (/author)""")


@dp.message_handler(commands=['malumotlar'])
async def send_welcome(message: types.Message):
    await message.answer("Bu bot PyCharm yordami bilan yaratildi")


@dp.message_handler(commands=['code'])
async def code_haqida(message: types.Message):
    with open('code.txt', 'r') as file:
        read = file.read()

    await message.answer(read)


@dp.message_handler(commands=['author'])
async def yaratuvchi_mf(message: types.Message):
    with open('mf.txt', 'r') as about_the_programmer:
        read2 = about_the_programmer.read()

    await message.answer(read2)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
