from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import request

# Кнопки
btn_kg = KeyboardButton('/Кыргыз_тили')
btn_ru = KeyboardButton('/Русский_язык')

btn_kg_schedule = KeyboardButton('/Дареги_жана_иш_тартиби')
btn_ru_schedule = KeyboardButton('/Адрес_и_график_работы')

btn_kg_passport = KeyboardButton('/Паспорт_алуу')
btn_ru_passport = KeyboardButton('/Получение_паспорта')

btn_kg_ogp = KeyboardButton('/Жалпы_жарандык_паспорт')
btn_ru_ogp = KeyboardButton('/Общегражданский_паспорт(Загран_паспорт)')

btn_kg_ogpBefore18 = KeyboardButton('/18-жашка_чейинки_өспүрүмдөргө')
btn_ru_ogpBefore18 = KeyboardButton('/Для_граждан_до_18_лет')

btn_kg_ogpAfter18 = KeyboardButton('/18-жашка_толгон_жарандарга')
btn_ru_ogpAfter18 = KeyboardButton('/Для_граждан_старше_18_лет')

btn_kg_idpasport = KeyboardButton('/Идентификациялык_карта(ID-паспорт)')
btn_ru_idpasport = KeyboardButton('/Идентификационный_паспорт_(ID)')

btn_kg_idpBefore18 = KeyboardButton('/18-жашка_чыга_элек_жаранга_ID-паспорт_алуу')
btn_ru_idpBefore18 = KeyboardButton('/Для_граждан_до_18_лет')

btn_kg_idpAfter18 = KeyboardButton('/18-жашка_чыккан_жарандарга_ID-паспорт_алуу')
btn_ru_idpAfter18 = KeyboardButton('/Для_граждан_старше_18_лет')


btn_kg_preReg = KeyboardButton('/Электрондук_иретке_катталуу')
btn_ru_preReg = KeyboardButton('/Электронная_очередь')


urlBtn_kg_preReg = InlineKeyboardButton(text='Электрондук иретке катталуу', url='https://reg.documentkg.ru/portal/que/pre-registrationkg')
urlBtn_ru_preReg = InlineKeyboardButton(text='Электронная очередь', url='https://reg.documentkg.ru/portal/que/pre-registrationkg')


urlKb_kg_preReg = InlineKeyboardMarkup(row_width=1)
urlKb_kg_preReg.add(urlBtn_kg_preReg)

urlKb_ru_preReg = InlineKeyboardMarkup(row_width=1)
urlKb_ru_preReg.add(urlBtn_ru_preReg)

# b4 = KeyboardButton('Поделиться номером', request_contact=True) 
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_language.add(btn_kg).add(btn_ru)


# Меню и подменю
kb_main_kg_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_kg_menu.add(btn_kg_schedule).add(btn_kg_passport)

kb_main_ru_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_ru_menu.add(btn_ru_schedule).add(btn_ru_passport)


kb_passport_kg = ReplyKeyboardMarkup(resize_keyboard=True)
kb_passport_kg.add(btn_kg_ogp).add(btn_kg_idpasport).add(btn_kg_preReg)

kb_passport_ru = ReplyKeyboardMarkup(resize_keyboard=True)
kb_passport_ru.add(btn_ru_ogp).add(btn_ru_idpasport).add(btn_ru_preReg)


kb_kg_ogp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_ogp.add(btn_kg_ogpBefore18).add(btn_kg_ogpAfter18)

kb_ru_ogp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_ogp.add(btn_ru_ogpBefore18).add(btn_ru_ogpAfter18)


kb_kg_idp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_idp.add(btn_kg_idpBefore18).add(btn_kg_idpAfter18)

kb_ru_idp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_idp.add(btn_ru_idpBefore18).add(btn_ru_idpAfter18)




# kb_ru_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_ru_schedule.add(btn_ru_schedule)

# kb_kg_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_kg_schedule.add(btn_kg_schedule)



# kb_client.row(b1, b2, b3)