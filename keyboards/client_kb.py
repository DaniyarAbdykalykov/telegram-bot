from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import request

# КНОПКИ----------------------------------------------------------------------------------------------------
# Паспорт
btn_kg = KeyboardButton('/Кыргыз_тили')
btn_ru = KeyboardButton('/Русский_язык')

btn_kg_mainMenu = KeyboardButton('Башкы меню')
btn_ru_mainMenu = KeyboardButton('Главное меню')

btn_kg_schedule = KeyboardButton('Дареги жана иш тартиби')
btn_ru_schedule = KeyboardButton('Адрес и график работы')

btn_kg_passport = KeyboardButton('Паспортту тариздөө')
btn_ru_passport = KeyboardButton('Оформление паспорта')

btn_kg_ogp = KeyboardButton('Жалпы жарандык паспорт (Загранпаспорт)')
btn_ru_ogp = KeyboardButton('Общегражданский паспорт (Загранпаспорт)')

btn_kg_ogpBefore18 = KeyboardButton('18 жашка чейинки өспүрүмдөргө')
btn_ru_ogpBefore18 = KeyboardButton('ОГП гражданам до 18 лет')

btn_kg_ogpAfter18 = KeyboardButton('18 жашка толгон жарандарга')
btn_ru_ogpAfter18 = KeyboardButton('ОГП гражданам старше 18 лет')

btn_kg_ogpAfter18Tern = KeyboardButton('Паспорттун мөөнөтү өтүп (бузулуп) калган')
btn_ru_ogpAfter18Tern = KeyboardButton('Истечение срока действия (порча) паспорта')

btn_kg_ogpAfter18Loss = KeyboardButton('Паспортту жоготуп (уурдатып) алган учурларда')
btn_ru_ogpAfter18Loss = KeyboardButton('Утеря (кража) паспорта')

btn_kg_ogpAfter18Change = KeyboardButton('Өздүк маалыматтарын өзгөрткөн учурунда (ОГП)')
btn_ru_ogpAfter18Change = KeyboardButton('Изменение персональных данных (ОГП)')

btn_kg_idpasport = KeyboardButton('Идентификациялык карта (ID-карта)')
btn_ru_idpasport = KeyboardButton('Идентификационная карта (ID-карта)')

btn_kg_idpBefore18 = KeyboardButton('18 жашка чыга элек жаранга ID-карта')
btn_ru_idpBefore18 = KeyboardButton('ID-карта гражданам до 18 лет')

btn_kg_idpAfter18 = KeyboardButton('18 жашка чыккан жарандарга ID-карта')
btn_ru_idpAfter18 = KeyboardButton('ID-карта гражданам старше 18 лет')

btn_kg_idpAfter18Tern = KeyboardButton('ID-картанын мөөнөтү өтүп (бузулуп) калган')
btn_ru_idpAfter18Tern = KeyboardButton('Истечение срока действия (порча) ID-карты')

btn_kg_idpAfter18Loss = KeyboardButton('ID картаны жоготуп (уурдатып) алган учурларда')
btn_ru_idpAfter18Loss = KeyboardButton('Утеря (кража) ID-карты')

btn_kg_idpAfter18Change = KeyboardButton('Өздүк маалыматтарын өзгөрткөн учурунда (ID)')
btn_ru_idpAfter18Change = KeyboardButton('Изменение персональных данных (ID)')


# Свидетельство о возвращении на Родину (СВР)
btn_kg_svr = KeyboardButton('Мекенге кайтуу күбөлүгүн алуу')
btn_ru_svr = KeyboardButton('Свидетельство на возвращение на родину')

btn_kg_svrBefore18 = KeyboardButton('18 жашка чейинки балдарга СВР алуу')
btn_ru_svrBefore18 = KeyboardButton('Получение СВР для лиц до 18 лет')

btn_kg_svrAfter18 = KeyboardButton('18 жаштан өйдө жарандарга СВР алуу')
btn_ru_svrAfter18 = KeyboardButton('Получение СВР для лиц, старше 18 лет')


# Водительское удостоверение
btn_kg_driversLincense = KeyboardButton('Айдоочулук күбөлүгүн алмаштыруу')
btn_ru_driversLincense = KeyboardButton('Водительское удостоверение')


# Истребование
btn_kg_reclamation = KeyboardButton('Документтерди суратып алдыруу')
btn_ru_reclamation = KeyboardButton('Истребование документов')

btn_kg_reclamationCrimRec = KeyboardButton('КРнын аймагында соттолбогондугу жөнүндө маалымкат')
btn_ru_reclamationCrimRec = KeyboardButton('Справка об отсутствии судимости в КР')

btn_kg_reclamationAuthDL = KeyboardButton('Айдоочулук күбөлүктүн аныктыгын тастыктаган маалымкат')
btn_ru_reclamationAuthDL = KeyboardButton('Справка о подтверждении подлинности ВУ')

btn_kg_reclamationMarriage = KeyboardButton('Никелешуу укугу жөнүндө маалымкат')
btn_ru_reclamationMarriage = KeyboardButton('Справка о семейном положении')


# Вопросы ЗАГС
btn_kg_issuesMar = KeyboardButton('ЗАГС маселелери')
btn_ru_issuesMar = KeyboardButton('Вопросы ЗАГС')

btn_kg_issuesMarRegistration = KeyboardButton('Никелешүүнү мамлекеттик каттоо')
btn_ru_issuesMarRegistration = KeyboardButton('Регистрация брака и получение свидетельства о заключении брака КР')

btn_kg_issuesMarChild = KeyboardButton('Баланын туулгандыгын каттоо жана КРнын туулгандыгы тууралуу күбөлүгүн берүү')
btn_ru_issuesMarChild = KeyboardButton('Регистрация рождения ребенка и получение свидетельства о рождении КР')


# Нотариат
btn_kg_notaries = KeyboardButton('Нотариат маселелери')
btn_ru_notaries = KeyboardButton('Вопросы нотариата')


# Юридическая помощь
btn_kg_lawyesr = KeyboardButton('Юридикалык жардам')
btn_ru_lawyesr = KeyboardButton('Юридическая помощь')


# Груз 200
btn_kg_cargo200 = KeyboardButton('Жүк-200')
btn_ru_cargo200 = KeyboardButton('Груз-200')


# Мекен карт
btn_kg_meken_card = KeyboardButton('Мекендеш статусу (Мекен-карт)')
btn_ru_meken_card = KeyboardButton('Статус соотечественника (Мекен-карт)')


urlBtn_kg_meken_card = InlineKeyboardButton(text="Керектүү документтердин тизмеси", url='https://mfa.gov.kg/kg/dm/posolstvo-kyrgyzskoy-respubliki-v-rossiyskoy-federacii/menyu---inostrannoe/konsulduk-maseleler/kyzmat/onsulduk-kyzmat')
urlBtn_ru_meken_card = InlineKeyboardButton(text="Перечень необходимых документов", url='https://mfa.gov.kg/ru/dm/pkr-v-rf/menyu---inostrannoe/konsulskie-voprosy/uslugi/onsulskie-uslugi')

urlKb_kg_mecen_card = InlineKeyboardMarkup(row_width=1)
urlKb_kg_mecen_card.add(urlBtn_kg_meken_card)

urlKb_ru_mecen_card = InlineKeyboardMarkup(row_width=1)
urlKb_ru_mecen_card.add(urlBtn_ru_meken_card)


# Предварительная регистрация
btn_kg_preReg = KeyboardButton('Электрондук иретке катталуу')
btn_ru_preReg = KeyboardButton('Электронная очередь')


urlBtn_kg_preReg = InlineKeyboardButton(text='Электрондук иретке катталуу', url='https://reg.documentkg.ru/portal/que/pre-registrationkg')
urlBtn_ru_preReg = InlineKeyboardButton(text='Электронная очередь', url='https://reg.documentkg.ru/portal/que/pre-registrationkg')


urlKb_kg_preReg = InlineKeyboardMarkup(row_width=1)
urlKb_kg_preReg.add(urlBtn_kg_preReg)

urlKb_ru_preReg = InlineKeyboardMarkup(row_width=1)
urlKb_ru_preReg.add(urlBtn_ru_preReg)


# Соцсети
btn_kg_contacts = KeyboardButton('Байланыш маалыматы')
btn_ru_contacts = KeyboardButton('Контактная информация')

urlBtn_kg_contactSite = InlineKeyboardButton(text='Элчиликтин расмий сайты', url='https://mfa.gov.kg/kg/dm/posolstvo-kyrgyzskoy-respubliki-v-rossiyskoy-federacii')
urlBtn_ru_contactSite = InlineKeyboardButton(text='Официальный сайт Посольства', url='https://mfa.gov.kg/ru/dm/posolstvo-kyrgyzskoy-respubliki-v-rossiyskoy-federacii')


urlBtn_contactInst = InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/invites/contact/?i=vc9nup8rpkcf&utm_content=miojb3c')
urlBtn_contactFb = InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/kg.consul.ru')
urlBtn_contactTelegram = InlineKeyboardButton(text='Telegram канал', url='https://t.me/kg_consul')
urlBtn_contactBot = InlineKeyboardButton(text='Робот-консультант', url='https://t.me/kg_consulBot')

urlBtn_kg_other_consulate = InlineKeyboardButton(text="КРнын РФдагы консулдук мекемелери", url='https://mfa.gov.kg/ru/dm/pkr-v-rf/menyu---inostrannoe/o-posolstve/konsulskiy-otdel/onsulskiy-otdel')
urlBtn_ru_other_consulate = InlineKeyboardButton(text="Консульские учреждения КР в РФ", url='https://mfa.gov.kg/ru/dm/pkr-v-rf/menyu---inostrannoe/o-posolstve/konsulskiy-otdel/onsulskiy-otdel')

urlKb_kg_contact = InlineKeyboardMarkup(row_width=1)
urlKb_kg_contact.add(urlBtn_kg_contactSite).row(urlBtn_contactInst, urlBtn_contactFb).add(urlBtn_contactTelegram).add(urlBtn_kg_other_consulate)

urlKb_ru_contact = InlineKeyboardMarkup(row_width=1)
urlKb_ru_contact.add(urlBtn_ru_contactSite).row(urlBtn_contactInst, urlBtn_contactFb).add(urlBtn_contactTelegram).add(urlBtn_ru_other_consulate)

urlKb_contactBot = InlineKeyboardMarkup(row_width=1)
urlKb_contactBot.add(urlBtn_contactBot)
# b4 = KeyboardButton('Поделиться номером', request_contact=True) 
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_language = ReplyKeyboardMarkup(resize_keyboard=True)
kb_language.add(btn_kg).add(btn_ru)


# МЕНЮ И ПОДМЕНЮ----------------------------------------------------------------------------------------------------

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


# Водительское удостоверение
# kb_kg_driversLincense = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_kg_driversLincense.add(btn_kg_driversLincenseChange).add(btn_kg_driversLincenseLoss)

# kb_ru_driversLincense = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_ru_driversLincense.add(btn_ru_driversLincenseChange).add(btn_ru_driversLincenseLoss)


# Истребование
kb_kg_reclamation = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_reclamation.add(btn_kg_reclamationCrimRec).add(btn_kg_reclamationAuthDL).add(btn_kg_reclamationMarriage).add(btn_kg_mainMenu)

kb_ru_reclamation = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_reclamation.add(btn_ru_reclamationCrimRec).add(btn_ru_reclamationAuthDL).add(btn_ru_reclamationMarriage).add(btn_ru_mainMenu)


# Вопросы ЗАГС
kb_kg_issuesMar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_kg_issuesMar.add(btn_kg_issuesMarRegistration).add(btn_kg_issuesMarChild).add(btn_kg_mainMenu)

kb_ru_issuesMar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ru_issuesMar.add(btn_ru_issuesMarRegistration).add(btn_ru_issuesMarChild).add(btn_ru_mainMenu)


# Главное меню
kb_main_kg_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_kg_menu.row(btn_kg_schedule, btn_kg_contacts).row(btn_kg_preReg, btn_kg_passport).add(btn_kg_driversLincense).add(btn_kg_svr).add(btn_kg_reclamation)\
.row(btn_kg_issuesMar, btn_kg_notaries).row(btn_kg_lawyesr).add(btn_kg_meken_card)


kb_main_ru_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main_ru_menu.row(btn_ru_schedule, btn_ru_contacts).row(btn_ru_preReg, btn_ru_passport).add(btn_ru_driversLincense).add(btn_ru_svr).add(btn_ru_reclamation).\
row(btn_ru_issuesMar, btn_ru_notaries).row(btn_ru_lawyesr).add(btn_ru_meken_card)


# kb_ru_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_ru_schedule.add(btn_ru_schedule)

# kb_kg_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_kg_schedule.add(btn_kg_schedule)



# kb_client.row(b1, b2, b3)