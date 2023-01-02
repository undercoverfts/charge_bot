import logging
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  ReplyKeyboardRemove
import btn as nav
import time
from aiogram.utils.markdown import hlink
import config as cfg

API_TOKEN = cfg.Token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#loop for cheks sub on chanels
async def check_sub_channels (channels, user_id):
     for channel in channels:
         chat_member = await bot.get_chat_member(chat_id=channel[1], user_id=user_id)
         if chat_member['status'] == 'left':
             return False
     return True


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
"""Привет! Это команда 'Заряди онлайн'.

Мы поможем тебе подключить функцию онлайн зарядки на свой Iphone / Android через сервер резервного питания! 

Чтобы получить инструкцию, жми кнопку "ПРОДОЛЖИТЬ" 👇

С тобой свяжется ассисент Максим 😉""", 
reply_markup = nav.kb_klient)
    

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "ПРОДОЛЖИТЬ":
        await message.answer(
"""Это ассистент Максим 👋

Выбери, пожалуйста, свою операционную систему ⬇️""", 
reply_markup=nav.mainmenu)

@dp.callback_query_handler(text="btnos")
async def ios(message: types.Message):
    await message.message.answer("Соединение с сервером...",
    reply_markup=ReplyKeyboardRemove())
    time.sleep(5)
    await message.message.answer("""
Успешно! Мы обнаружили твою модель телефона и начали подключение к серверу резервного питания! 
Для получения интсрукции жми кнопку 'ПОЛУЧИТЬ'""", 
reply_markup = nav.btnmaint)

@dp.callback_query_handler(text="btnandroid")
async def android(message: types.Message):
    await message.message.answer("Соединение с сервером...",
    reply_markup=ReplyKeyboardRemove())
    time.sleep(5)
    await message.message.answer("""
Успешно! Мы обнаружили твою модель телефона и начали подключение к серверу резервного питания! 
Для получения интсрукции жми кнопку 'ПОЛУЧИТЬ'""",
reply_markup=nav.btnmaint)

@dp.callback_query_handler(text="btnmain")
async def mainbtn(message: types.Message):

    await message.message.answer("Отлично! Для получения инструкции тебе необходимо выполнить последний шаг 👉 подписаться на наши каналы-спонсоры,\nБлагодаря им наш сервис работает абсолютно бесплатно! Ни за что платить ненужно 😉", reply_markup=nav.showChannels())
@dp.callback_query_handler(text="btndone")
async def subsdone(message: types.Message):
    await message.message.answer("""
Отлично! Задание выполнено! Плагин подключится в ближайшее время, обычно это занимает не больше 2-3 дней.

Все зависит от количества заявок на подключение 😉

📍Также во время ожидани нельзя отписываться от каналов спонсоров, иначе подключение будет остановлено и ты переместишься в конец очереди! 

С уважением, бот Стивен хелпер ❤️
""")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
