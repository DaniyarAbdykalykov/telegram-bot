from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiohttp import request

# Кнопки
btn_kg = KeyboardButton('/Кыргыз_тили')
btn_ru = KeyboardButton('/Русский_язык')

btn_kg_schedule = KeyboardButton('/Дареги_жана_иш_тартиби')
btn_ru_schedule = KeyboardButton('/Адрес_и_график_работы')

btn_kg_passport = KeyboardButton('/Паспорт_алуу')
btn_kg_ogp = KeyboardButton('/Жалпы_жарандык_паспорт')
btn_kg_ogpBefore18 = KeyboardButton('/18-жашка_чейинки_өспүрүмдөргө')
btn_kg_ogpAfter18 = KeyboardButton('/18-жашка_толгон_жарандарга')
# b4 = KeyboardButton('Поделиться номером', request_contact=True) 
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_language.add(btn_kg).add(btn_ru)

# Меню и подменю
kb_main_kg_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_kg_menu.add(btn_kg_schedule).add(btn_kg_passport)

kb_main_ru_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_ru_menu.add(btn_ru_schedule)

kb_passport_kg = ReplyKeyboardMarkup(resize_keyboard=True)
kb_passport_kg.add(btn_kg_ogp)

kb_kg_ogp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_ogp.add(btn_kg_ogpBefore18).add(btn_kg_ogpAfter18)




# kb_ru_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_ru_schedule.add(btn_ru_schedule)

# kb_kg_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_kg_schedule.add(btn_kg_schedule)



# kb_client.row(b1, b2, b3)