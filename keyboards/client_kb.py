from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiohttp import request

b_kg = KeyboardButton('/Кыргыз_тили')
b_ru = KeyboardButton('/Русский_язык')
b_ru_schedule = KeyboardButton('/Режим_работы')
# b4 = KeyboardButton('Поделиться номером', request_contact=True) 
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_language.add(b_kg).add(b_ru)

kb_ru_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_schedule.add(b_ru_schedule)
# kb_client.row(b1, b2, b3)