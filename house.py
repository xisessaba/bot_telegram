from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot
from aiogram.types import Message
from bot import dp


class HouseHandler:
    def __init__(self, bot: Bot):
        self.bot = bot

    
    async def handle_create_house(self, message: Message):
        class House(StatesGroup):
            house_name = State()
            house_price = State()
            house_description = State()
            house_photo = State()
            house_phone = State()
            house_whatsapp = State()

           

        await message.answer('Как вас зовут?')
        await House.house_name.set()

        @dp.message_handler(state=House.house_name)
        async def house_name(message: types.Message, state: FSMContext):
            await House.house_name.set()
            async with state.proxy() as data:
                data['house_name'] = message.text
            await House.next()
            await message.answer('Напишите цену вашего дома')

        @dp.message_handler(state=House.house_price)
        async def house_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['house_price'] = message.text
            await House.next()
            await message.answer('Отправьте несколько фотографий вашего дома')
        
        @dp.message_handler(state=House.house_photo, content_types=['photo'])
        async def house_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['house_photo'] = message.photo[-1].file_id
            await House.next()
            await message.answer('Напишите дополнительную информацию о вашем доме')
        
        @dp.message_handler(state=House.house_description)
        async def house_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['house_description'] = message.text
            await House.next()
            await message.answer('Напишите ваш номер телефона')

        @dp.message_handler(state=House.house_phone)
        async def house_phone(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['house_phone'] = message.text
            await House.next()
            await message.answer('Напишите ваш номер WhatsApp')

        @dp.message_handler(state=House.house_whatsapp)
        async def house_whatsapp(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['house_whatsapp'] = message.text
            await House.next()
            await message.answer('Ваше объявление успешно создано!')
            await state.finish()
        
    async def create_apartment(self, message: Message):
        class Apartment(StatesGroup):
            apartment_name = State()
            apartment_price = State()
            apartment_description = State()
            apartment_photo = State()
            apartment_phone = State()
            apartment_whatsapp = State()

           

        await message.answer('Как вас зовут?')
        await Apartment.apartment_name.set()

        @dp.message_handler(state=Apartment.apartment_name)
        async def apartment_name(message: types.Message, state: FSMContext):
            await Apartment.apartment_name.set()
            async with state.proxy() as data:
                data['apartment_name'] = message.text
            await Apartment.next()
            await message.answer('Напишите цену вашей квартиры')

        @dp.message_handler(state=Apartment.apartment_price)
        async def apartment_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_price'] = message.text
            await Apartment.next()
            await message.answer('Отправьте несколько фотографий вашей квартиры')
        
        @dp.message_handler(state=Apartment.apartment_photo, content_types=['photo'])
        async def apartment_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_photo'] = message.photo[-1].file_id
            await Apartment.next()
            await message.answer('Напишите дополнительную информацию о вашей квартире')
        
        @dp.message_handler(state=Apartment.apartment_description)
        async def apartment_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_description'] = message.text
            await Apartment.next()
            await message.answer('Напишите ваш номер телефона')

        @dp.message_handler(state=Apartment.apartment_phone)
        async def apartment_phone(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_phone'] = message.text
            await Apartment.next()
            await message.answer('Напишите ваш номер WhatsApp')

        @dp.message_handler(state=Apartment.apartment_whatsapp)
        async def apartment_whatsapp(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_whatsapp'] = message.text
            await Apartment.next()
            await message.answer('Ваше объявление успешно создано!')
            await state.finish()

        
    async def create_apartment_day(self, message: Message):
        class ApartmentDay(StatesGroup):
            apartment_day_name = State()
            apartment_day_price = State()
            apartment_day_description = State()
            apartment_day_photo = State()
            apartment_day_phone = State()
            apartment_day_whatsapp = State()

        

        await message.answer('Как вас зовут?')
        await ApartmentDay.apartment_day_name.set()

        @dp.message_handler(state=ApartmentDay.apartment_day_name)
        async def apartment_day_name(message: types.Message, state: FSMContext):
            await ApartmentDay.apartment_day_name.set()
            async with state.proxy() as data:
                data['apartment_day_name'] = message.text
            await ApartmentDay.next()
            await message.answer('Напишите цену аренды вашей комнаты')
        
        @dp.message_handler(state=ApartmentDay.apartment_day_price)
        async def apartment_day_price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_day_price'] = message.text
            await ApartmentDay.next()
            await message.answer('Отправьте несколько фотографий вашей квартиры')

        @dp.message_handler(state=ApartmentDay.apartment_day_photo, content_types=['photo'])
        async def apartment_day_photo(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_day_photo'] = message.photo[-1].file_id
            await ApartmentDay.next()
            await message.answer('Напишите дополнительную информацию о вашей квартире')

        @dp.message_handler(state=ApartmentDay.apartment_day_description)
        async def apartment_day_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_day_description'] = message.text
            await ApartmentDay.next()
            await message.answer('Напишите ваш номер телефона')

        @dp.message_handler(state=ApartmentDay.apartment_day_phone)
        async def apartment_day_phone(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_day_phone'] = message.text
            await ApartmentDay.next()
            await message.answer('Напишите ваш номер WhatsApp')

        @dp.message_handler(state=ApartmentDay.apartment_day_whatsapp)
        async def apartment_day_whatsapp(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['apartment_day_whatsapp'] = message.text
            await ApartmentDay.next()
            await message.answer('Ваше объявление успешно создано!')
            await state.finish()

        
        
    
