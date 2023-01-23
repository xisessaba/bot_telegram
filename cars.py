from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot
from aiogram.types import Message
from bot import dp

class AutomobileCategoryHandler:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def handle_create_car(self, message: Message):
        # логика поиска объявлений об автомобилях
        # и отправка результатов в чат

        class Cars(StatesGroup):
            car_name = State()
            car_price = State()
            car_description = State()
            car_photo = State()

        await message.answer('Введите название автомобиля')
        await Cars.car_name.set()

        @dp.message_handler(state=Cars.car_name)
        async def car_name(message: types.Message, state: FSMContext):
            await Cars.car_name.set()
            async with state.proxy() as data:
                data['car_name'] = message.text
            await Cars.next()
            await message.answer('Введите цену автомобиля')

        @dp.message_handler(state=Cars.car_price)
        async def car_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_price'] = message.text
            await Cars.next()
            await message.answer('Введите описание автомобиля')

        @dp.message_handler(state=Cars.car_description)
        async def car_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_description'] = message.text
            await Cars.next()
            await message.answer('Отправьте фото автомобиля')

        @dp.message_handler(content_types=['photo'], state=Cars.car_photo)
        async def car_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_photo'] = message.photo[-1].file_id
            await Cars.next()
            data = await state.get_data()
            car_name = data.get('car_name')
            car_price = data.get('car_price')
            car_description = data.get('car_description')
            car_photo = data.get('car_photo')
            await message.answer(f'Название автомобиля: {car_name}\nЦена: {car_price}\nОписание: {car_description}\nФото: {car_photo}')
            await state.finish()
    async def handle_create_rent(self, message: Message):

        class Rent_Cars(StatesGroup):
            car_name = State()
            car_price = State()
            car_photo = State()
            car_description = State()


        await message.answer('Введите название автомобиля')
        await Rent_Cars.car.set()

        @dp.message_handler(state=Rent_Cars.car_name)
        async def car_name(message: types.Message, state: FSMContext):
            await Rent_Cars.car.set()
            async with state.proxy() as data:
                data['car_name'] = message.text
            await Rent_Cars.next()
            await message.answer('Введите модель автомобиля')

        @dp.message_handler(state=Rent_Cars.car_model)
        async def car_model(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_model'] = message.text
            await Rent_Cars.next()
            await message.answer('Введите цену аренды')

        @dp.message_handler(state=Rent_Cars.car_price)
        async def car_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_price'] = message.text
            await Rent_Cars.next()
            await message.answer('Отправьте фото автомобиля')

        @dp.message_handler(content_types=['photo'], state=Rent_Cars.car_photo)
        async def car_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_photo'] = message.photo[-1].file_id
            await Rent_Cars.next()
            await message.answer('Введите описание автомобиля\nЦвет\nСостояние\nБыл ли он в ремонте и т.д')

        @dp.message_handler(state=Rent_Cars.car_description)
        async def car_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['car_description'] = message.text
            await Rent_Cars.next()
        
            data = await state.get_data()
            
            car_name = data.get('car_name')
            car_price = data.get('car_price')
            car_photo = data.get('car_photo')
            car_description = data.get('car_description')

            await message.answer_photo(car_photo)
            await message.answer(f'Название автомобиля: {car_name}\nЦена аренды: {car_price}\nОписание автомобиля: {car_description}')

            await message.answer('Все верно?')
            await Rent_Cars.finish()

        
        
            


            
            

                
            
                







            

            












