from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot
from aiogram.types import Message
from bot import dp


class WorkHandler:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def handle_create_work(self, message: Message):
            
            class Work(StatesGroup):
                work_name = State()
                work_price = State()
                work_description = State()
    
            await message.answer('Введите название вашей компании')
            await Work.work_name.set()
    
            @dp.message_handler(state=Work.work_name)
            async def work_name(message: types.Message, state: FSMContext):
                await Work.work_name.set()
                async with state.proxy() as data:
                    data['work_name'] = message.text
                await Work.next()
                await message.answer('Напишите зарплату от-до')
    
            @dp.message_handler(state=Work.work_price)
            async def work_price(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['work_price'] = message.text
                await Work.next()
                await message.answer('Напишите дополнительную информацию')
    
            @dp.message_handler(state=Work.work_description)
            async def work_description(message: types.Message, state: FSMContext):
                async with state.proxy() as data:
                    data['work_description'] = message.text
                await Work.next()
    
                data = await state.get_data()
    
                work_name =  data.get('work_name')
                work_price = data.get('work_price')
                work_photo = data.get('work_photo')
                work_description = data.get('work_description')
    
                await message.answer(f'Название работы: {work_name}\nЦена: {work_price}\nОписание: {work_description}')
                await message.answer_photo(work_photo)
                await state.finish()


        
    async def create_resume(self, message: Message):

        class Resume(StatesGroup):
            resume_name = State()
            resume_phone = State()
            resume_whatsapp = State()
            resume_description = State()

        
        await message.answer('Как вас зовут?')
        await Resume.resume_name.set()

        @dp.message_handler(state=Resume.resume_name)
        async def resume_name(message: types.Message, state: FSMContext):
            await Resume.resume_name.set()
            async with state.proxy() as data:
                data['resume_name'] = message.text
            await Resume.next()
            await message.answer('Отправьте свой рабочий номер телефона')

        @dp.message_handler(state=Resume.resume_phone)
        async def resume_phone(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['resume_phone'] = message.text
            await Resume.next()
            await message.answer('Отправьте свой номер WhatsApp')

        @dp.message_handler(state=Resume.resume_whatsapp)
        async def resume_whatsapp(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['resume_whatsapp'] = message.text
            await Resume.next()
            await message.answer('Напишите о себе\nМожете отправить сюда ваше резюме')


        @dp.message_handler(state=Resume.resume_description)
        async def resume_description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['resume_description'] = message.text
            await Resume.next()

            data = await state.get_data()

            resume_name =  data.get('resume_name')
            resume_phone = data.get('resume_phone')
            resume_whatsapp = data.get('resume_whatsapp')
            resume_description = data.get('resume_description')

            await message.answer(f'Имя: {resume_name}\nТелефон: {resume_phone}\nWhatsApp: {resume_whatsapp}\nО себе: {resume_description}')
            await state.finish()