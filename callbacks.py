from keyboards import get_keyboard_main
from aiogram import types

# from cars import AutomobileCategoryHandler
# from electronic import ElectronicCategoryHandler
# from house import HouseHandler
# from works import WorkHandler

# class CallbackHandler:
#     def init(self, automobile_handler: AutomobileCategoryHandler, electronic_handler: ElectronicCategoryHandler, house_handler: HouseHandler, work_handler: WorkHandler):
#         self.automobile_handler = automobile_handler
#         self.electronic_handler = electronic_handler
#         self.house_handler = house_handler
#         self.work_handler = work_handler

async def handle_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    print('-----------------------')
    print(data)
    if data == "post_announcement":
        await callback_query.message.answer("Выберите категорию", reply_markup=get_keyboard_main("search"))

    elif data == "announcement":
        await callback_query.message.answer("Выберите категорию", reply_markup=get_keyboard_main("search"))

    else:
        await callback_query.message.answer("Извините, я не понимаю вашу команду.")





# @dp.callback_query_handler(lambda c: c.data in ["announcement", "post_announcement", "support"])
# async def process_callback(callback_query: types.CallbackQuery):
#     if callback_query.data == "announcement":
#        await bot.send_message(callback_query.from_user.id, "Выберите категорию для поиска", reply_markup=get_keyboard_main("search"))
#     elif callback_query.data == "post_announcement":
#         #ПРИ НАЖАТИИ НА КНОПКУ post_announcement ВЫВОДИМ ДРУГУЮ КЛАВИАТУРУ
#         # await bot.send_message(callback_query.from_user.id, "Выберите категорию", reply_markup=get_keyboard_main("search"))
#         print('-----')
#     elif callback_query.data == "support":
#         pass
#     await bot.answer_callback_query(callback_query.id)

# @dp.callback_query_handler(lambda c: c.data in ["cars","electronic", "housed", "work", "serviced", "back"])
# async def process_callback_categories(callback_query: types.CallbackQuery):
#     if callback_query.data == "cars":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию автомобилей", reply_markup=get_keyboard_main("kb_cars"))
#     elif callback_query.data == "transport":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию транспорта", reply_markup=get_keyboard_main("kb_cars"))
#     elif callback_query.data == "electronic":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию электроники", reply_markup=get_keyboard_main("kb_electronic"))

#     elif callback_query.data == "housed":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию недвижимости", reply_markup=get_keyboard_main("kb_housed"))

#     elif callback_query.data == "work":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию работы", reply_markup=get_keyboard_main("kb_work"))

#     elif callback_query.data == "services":
#         await bot.send_message(callback_query.from_user.id, "Выберите категорию услуг", reply_markup=get_keyboard_main("kb_services"))
    
#     elif callback_query.data == "back":
#         pass
#     await bot.answer_callback_query(callback_query.id)

# @dp.callback_query_handler(lambda c: c.data in ["cars"])
# async def process_callback(callback_query: types.CallbackQuery):    
#     automobile_handler = AutomobileCategoryHandler(bot)
#     await automobile_handler.handle_create_car(callback_query.message)
#     await bot.answer_callback_query(callback_query.id)

