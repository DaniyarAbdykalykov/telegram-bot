from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import request

# КНОПКИ----------------------------------------------------------------------------------------------------
# Паспорт
btn_kg = KeyboardButton('/Кыргыз_тили')
btn_ru = KeyboardButton('/Русский_язык')

btn_kg_mainMenu = KeyboardButton('/Башкы_меню')
btn_ru_mainMenu = KeyboardButton('/Главное_меню')

btn_kg_schedule = KeyboardButton('/Дареги_жана_иш_тартиби')
btn_ru_schedule = KeyboardButton('/Адрес_и_график_работы')

btn_kg_passport = KeyboardButton('/Паспорт_алуу')
btn_ru_passport = KeyboardButton('/Получение_паспорта')

btn_kg_ogp = KeyboardButton('/Жалпы_жарандык_паспорт')
btn_ru_ogp = KeyboardButton('/Общегражданский_паспорт(Загран_паспорт)')

btn_kg_ogpBefore18 = KeyboardButton('/18-жашка_чейинки_өспүрүмдөргө')
btn_ru_ogpBefore18 = KeyboardButton('/ОГП_гражданам_до_18_лет')

btn_kg_ogpAfter18 = KeyboardButton('/18-жашка_толгон_жарандарга')
btn_ru_ogpAfter18 = KeyboardButton('/ОГП_гражданам_старше_18_лет')

btn_kg_ogpAfter18Tern = KeyboardButton('/паспорттун_мөөнөтү_өтүп(бузулуп)_калган')
btn_ru_ogpAfter18Tern = KeyboardButton('/истечение_срока_действия(порча)_паспорта')

btn_kg_ogpAfter18Loss = KeyboardButton('/паспортту_жоготуп(уурдатып)_алган_учурларда')
btn_ru_ogpAfter18Loss = KeyboardButton('/утеря(кража)_паспорта')

btn_kg_ogpAfter18Change = KeyboardButton('/өздүк_маалыматтарын_өзгөрткөн_учурунда(ОГП)')
btn_ru_ogpAfter18Change = KeyboardButton('/изменение_персональных_данных(ОГП)')

btn_kg_idpasport = KeyboardButton('/Идентификациялык_карта(ID)')
btn_ru_idpasport = KeyboardButton('/Идентификационная_карта_(ID)')

btn_kg_idpBefore18 = KeyboardButton('/18-жашка_чыга_элек_жаранга_ID-карта')
btn_ru_idpBefore18 = KeyboardButton('/ID_карта_гражданам_до_18_лет')

btn_kg_idpAfter18 = KeyboardButton('/18-жашка_чыккан_жарандарга_ID-карта')
btn_ru_idpAfter18 = KeyboardButton('/ID_карта_гражданам_старше_18_лет')

btn_kg_idpAfter18Tern = KeyboardButton('/ID-картанын_мөөнөтү_өтүп(бузулуп)_калган')
btn_ru_idpAfter18Tern = KeyboardButton('/истечение_срока_действия(порча)_ID-карты')

btn_kg_idpAfter18Loss = KeyboardButton('/ID-картаны_жоготуп(уурдатып)_алган_учурларда')
btn_ru_idpAfter18Loss = KeyboardButton('/утеря(кража)_ID-карты')

btn_kg_idpAfter18Change = KeyboardButton('/өздүк_маалыматтарын_өзгөрткөн_учурунда(ID)')
btn_ru_idpAfter18Change = KeyboardButton('/изменение_персональных_данных(ID)')


# Свидетельство о возвращении на Родину (СВР)
btn_kg_svr = KeyboardButton('/Мекенге_кайтуу_күбөлүгү')
btn_ru_svr = KeyboardButton('/Свидетельство_на_возвращение_на_родину')

btn_kg_svrBefore18 = KeyboardButton('/18-жашка_чейинки_балдарга_СВР_алуу')
btn_ru_svrBefore18 = KeyboardButton('/Получение_СВР_до_18-летнего_возраста')

btn_kg_svrAfter18 = KeyboardButton('/18-жаштан_өйдө_жарандарга_СВР_алуу')
btn_ru_svrAfter18 = KeyboardButton('/Получение_СВР_старше_18-лет_(при_утере_документов)')


# Предварительная регистрация
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


# МЕНЮ И ПОДМЕНЮ----------------------------------------------------------------------------------------------------
# Главное меню
kb_main_kg_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_kg_menu.add(btn_kg_schedule).add(btn_kg_passport).add(btn_kg_svr)

kb_main_ru_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_ru_menu.add(btn_ru_schedule).add(btn_ru_passport).add(btn_ru_svr)


# Паспорт
kb_passport_kg = ReplyKeyboardMarkup(resize_keyboard=True)
kb_passport_kg.add(btn_kg_ogp).add(btn_kg_idpasport).add(btn_kg_preReg).add(btn_kg_mainMenu)

kb_passport_ru = ReplyKeyboardMarkup(resize_keyboard=True)
kb_passport_ru.add(btn_ru_ogp).add(btn_ru_idpasport).add(btn_ru_preReg).add(btn_ru_mainMenu)


kb_kg_ogp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_ogp.add(btn_kg_ogpBefore18).add(btn_kg_ogpAfter18).add(btn_kg_mainMenu)

kb_ru_ogp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_ogp.add(btn_ru_ogpBefore18).add(btn_ru_ogpAfter18).add(btn_ru_mainMenu)

kb_kg_ogpAfter18 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_ogpAfter18.add(btn_kg_ogpAfter18Tern).add(btn_kg_ogpAfter18Loss).add(btn_kg_ogpAfter18Change).add(btn_kg_mainMenu)

kb_ru_ogpAfter18 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_ogpAfter18.add(btn_ru_ogpAfter18Tern).add(btn_ru_ogpAfter18Loss).add(btn_ru_ogpAfter18Change).add(btn_ru_mainMenu)


kb_kg_idp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_idp.add(btn_kg_idpBefore18).add(btn_kg_idpAfter18).add(btn_kg_mainMenu)

kb_ru_idp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_idp.add(btn_ru_idpBefore18).add(btn_ru_idpAfter18).add(btn_ru_mainMenu)

kb_kg_idpAfter18 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_idpAfter18.add(btn_kg_idpAfter18Tern).add(btn_kg_idpAfter18Loss).add(btn_kg_idpAfter18Change).add(btn_kg_mainMenu)

kb_ru_idpAfter18 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_idpAfter18.add(btn_ru_idpAfter18Tern).add(btn_ru_idpAfter18Loss).add(btn_ru_idpAfter18Change).add(btn_ru_mainMenu)


# СВР
kb_kg_svr = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_svr.add(btn_kg_svrBefore18).add(btn_kg_svrAfter18).add(btn_kg_mainMenu)

kb_ru_svr = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_svr.add(btn_ru_svrBefore18).add(btn_ru_svrAfter18).add(btn_ru_mainMenu)




# kb_ru_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_ru_schedule.add(btn_ru_schedule)

# kb_kg_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_kg_schedule.add(btn_kg_schedule)



# kb_client.row(b1, b2, b3)