
from aiogram.types import Message
from cars import AutomobileCategoryHandler
from electronic import ElectronicCategoryHandler

class MessageHandler:
    def init(self, automobile_handler: AutomobileCategoryHandler, electronic_handler: ElectronicCategoryHandler):
        self.automobile_handler = automobile_handler
        self.electronic_handler = electronic_handler

    async def handle_message(self, message: Message):

        text = message.text.lower()
        if 'автомобиль' in text:
            await self.automobile_handler.handle_create_car(message)
        elif 'Электроника' in text:
            await self.electronic_handler.handle_create_phone(message)

        else:
            await message.reply("К сожалению, мы не можем обработать ваше сообщение. Пожалуйста, используйте команду /help для получения списка доступных команд.")


