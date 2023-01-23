
from aiogram import types
from keyboards import get_keyboard_main
from config import dp, bot
from aiogram.types import Message
from callbacks import handle_callback


class BotHandler:
    def __init__(self, bot: bot):
        self.bot = bot
        dp.register_message_handler(self.handle_message, commands=['start', 'help'])
        dp.register_message_handler(self.handle_message, text=['привет', 'пока'])
        dp.register_callback_query_handler(self.handle_callbacks, lambda c: c.data in  ['post_announcement','announcement' ])

    


    async def handle_message(self, message: Message):
        if message.text == '/start':
            await message.reply("Привет! Я бот для объявлений. Воспользуйтесь командой /help чтобы узнать доступные команды.", reply_markup=get_keyboard_main("main"))
        elif message.text == '/help':
            await message.reply("Доступные команды: \n /search - поиск объявлений \n /create - создание нового объявления")
        elif message.text == 'привет':
            await message.reply("Привет! Я бот для объявлений. Воспользуйтесь командой ", reply_markup=get_keyboard_main("main"))
        elif message.text == 'пока':
            await message.reply("Пока! Я бот для объявлений. Воспользуйтесь командой ", reply_markup=get_keyboard_main("main"))

        else:
            await message.reply("Извините, я не понимаю вашу команду. Воспользуйтесь командой /help чтобы узнать доступные команды.")




   

    async def handle_callbacks(self, callback_query: types.CallbackQuery):
        await handle_callback(callback_query)