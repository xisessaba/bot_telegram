from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_main(name: str):
    if name == "main":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Поиск объявлений", callback_data="announcement"))
        keyboard.add(InlineKeyboardButton("Разместить Объявление", callback_data="post_announcement"))
        keyboard.add(InlineKeyboardButton("Тех.Поддержка", callback_data="support"))
    elif name == "search":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Транспорт", callback_data="transport"))
        keyboard.add(InlineKeyboardButton("Электроника", callback_data="electronic"))
        keyboard.add(InlineKeyboardButton("Недвижимость", callback_data="housed"))
        keyboard.add(InlineKeyboardButton("Работа", callback_data="work"))
        keyboard.add(InlineKeyboardButton("Услуги", callback_data="services"))
        keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))
    elif name == "kb_cars":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Автомобили", callback_data="cars"))
        keyboard.add(InlineKeyboardButton("Аренда авто", callback_data="cars_rent"))
        keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))
    elif name == "kb_electronic":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Мобильные телефоны", callback_data="phones"))
        keyboard.add(InlineKeyboardButton("Компьютеры, ноутбуки", callback_data="computers"))
        keyboard.add(InlineKeyboardButton("Игровые приставки", callback_data="game"))
        keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))
    
    elif name == "kb_housed":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Квартиры", callback_data="flats"))
        keyboard.add(InlineKeyboardButton("Комнаты", callback_data="rooms"))
        keyboard.add(InlineKeyboardButton("Дома, дачи, коттеджи", callback_data="houses"))
        keyboard.add(InlineKeyboardButton("Земельные участки", callback_data="land"))
        keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))
        
    elif name == "kb_work":
        keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        keyboard.add(InlineKeyboardButton("Вакансии", callback_data="vacancies"))
        keyboard.add(InlineKeyboardButton("Резюме", callback_data="resume"))
        keyboard.add(InlineKeyboardButton("Назад", callback_data="back"))


    return keyboard