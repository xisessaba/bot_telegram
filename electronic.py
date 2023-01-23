from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot
from aiogram.types import Message
from bot import dp


class ElectronicCategoryHandler:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def handle_create_phone(self, message: Message):

        
        class Electronic(StatesGroup):
            electronic_name = State()
            electronic_price = State()
            electronic_description = State()
            electronic_photo = State()

                                                                                
        await message.answer('Введите название телефона')
        await Electronic.electronic_name.set()

        @dp.message_handler(state=Electronic.electronic_name)
        async def electronic_name(message: types.Message, state: FSMContext):
            await Electronic.electronic_name.set()
            async with state.proxy() as data:
                data['electronic_name'] = message.text
            await Electronic.next()
            await message.answer('Введите цену телефона')

        @dp.message_handler(state=Electronic.electronic_price)
        async def electronic_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['electronic_price'] = message.text
            await Electronic.next()
            await message.answer('Отправьте фото телефона')

        @dp.message_handler(state=Electronic.electronic_photo, content_types=['photo'])
        async def electronic_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['electronic_photo'] = message.photo[-1].file_id
            await Electronic.next()
            await message.answer('Введите описание телефона')

        @dp.message_handler(state=Electronic.electronic_description)
        async def electronic_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['electronic_description'] = message.text
            await Electronic.next()

            data = await state.get_data()

            electronic_name =  data.get('electronic_name')
            electronic_price = data.get('electronic_price')
            electronic_photo = data.get('electronic_photo')
            electronic_description = data.get('electronic_description')


            await message.answer_photo(electronic_photo)
            await message.answer(f'Название телефона: {electronic_name}\nЦена телефона: {electronic_price}\nОписание телефона: {electronic_description}')                             
            
            await state.finish()

        async def handle_create_pc(self, message: Message):
            class Electronic_Pc(StatesGroup):
                electronic_name = State()
                electronic_price = State()
                electronic_photo = State()
                electronic_description = State()
            await message.answer('Введите название компьютера')
            await Electronic_Pc.electronic_name.set()

            @dp.message_handler(state=Electronic_Pc.electronic_name)
            async def electronic_name(message: types.Message, state: FSMContext):
                await Electronic_Pc.electronic_name.set()
                async with state.proxy() as data:
                    data['electronic_name'] = message.text
                await Electronic_Pc.next()
                await message.answer('Введите цену компьютера')

            @dp.message_handler(state=Electronic_Pc.electronic_price)
            async def electronic_price(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_price'] = message.text
                await Electronic_Pc.next()
                await message.answer('Отправьте фото компьютера')

            @dp.message_handler(state=Electronic_Pc.electronic_photo, content_types=['photo'])
            async def electronic_photo(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_photo'] = message.photo[-1].file_id
                await Electronic_Pc.next()
                await message.answer('Введите описание компьютера\nПроцессор\nОЗУ:\nЖесткий диск:\nВидеокарта:\nИ дополнительные характеристики')

            @dp.message_handler(state=Electronic_Pc.electronic_description)
            async def electronic_description(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_description'] = message.text
                await Electronic_Pc.next()

                data = await state.get_data()

                electronic_name =  data.get('electronic_name')
                electronic_price = data.get('electronic_price')
                electronic_photo = data.get('electronic_photo')
                electronic_description = data.get('electronic_description')


                await message.answer_photo(electronic_photo)
                await message.answer(f'Название компьютера: {electronic_name}\nЦена компьютера: {electronic_price}\nОписание компьютера: {electronic_description}')

                
                await state.finish()

        async def handle_create_game(self, message: Message):

            class Electronic_Game(StatesGroup):
                electronic_name = State()
                electronic_price = State()
                electronic_photo = State()
                electronic_description = State()
            await message.answer('Введите название приставки')
            await Electronic_Game.electronic_name.set()

            @dp.message_handler(state=Electronic_Game.electronic_name)
            async def electronic_name(message: types.Message, state: FSMContext):
                await Electronic_Game.electronic_name.set()
                async with state.proxy() as data:
                    data['electronic_name'] = message.text
                await Electronic_Game.next()
                await message.answer('Введите цену приставки')

            @dp.message_handler(state=Electronic_Game.electronic_price)
            async def electronic_price(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_price'] = message.text
                await Electronic_Game.next()
                await message.answer('Отправьте фото приставки')

            @dp.message_handler(state=Electronic_Game.electronic_photo, content_types=['photo'])
            async def electronic_photo(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_photo'] = message.photo[-1].file_id
                await Electronic_Game.next()
                await message.answer('Напишите сюда дополнительные характеристики приставки')
            @dp.message_handler(state=Electronic_Game.electronic_description)
            async def electronic_description(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['electronic_description'] = message.text
                await Electronic_Game.next()

                data = await state.get_data()

                electronic_name =  data.get('electronic_name')
                electronic_price = data.get('electronic_price')
                electronic_photo = data.get('electronic_photo')
                electronic_description = data.get('electronic_description')


                await message.answer_photo(electronic_photo)
                await message.answer(f'Название приставки: {electronic_name}\nЦена приставки: {electronic_price}\nОписание приставки: {electronic_description}')

                await state.finish()

        

        


            
        