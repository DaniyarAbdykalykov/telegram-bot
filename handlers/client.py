from ast import parse
from importlib.abc import PathEntryFinder
from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import *
from aiogram.types import ReplyKeyboardRemove
from service_templates import *
# Приветствие------------------------------------------------------------------------------------
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Саламатсызбы! Сиз менен Кыргыз Республикасынын Россия \
        Федерациясындагы Элчилигинин электрондук консулу байланышта. Керектүү тилди тандаңыз\n\n\
Вас приветствует электронный консул Посольства Кыргызской Республики в Российской Федерации! \
Выберите нужный язык обслуживания', reply_markup=kb_language)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/KyrgyzConsulate_ruBot')



# Выбор языка------------------------------------------------------------------------------------
async def service_language_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_main_kg_menu)

async def service_language_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_main_ru_menu)



# Главное меню------------------------------------------------------------------------------------
async def mainMenu_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_main_kg_menu)

async def mainMenu_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_main_ru_menu)



# Адрес и график работы------------------------------------------------------------------------------------
async def consulate_open_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, consulate_open_ru_tmp, parse_mode=types.ParseMode.HTML)

async def consulate_open_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, consulate_open_kg_tmp, parse_mode=types.ParseMode.HTML)



# Паспорт------------------------------------------------------------------------------------
async def passport_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_passport_kg)

async def passport_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_passport_ru)


# ОГП
async def passport_kg_ogp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_ogp)

async def passport_ru_ogp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_ogp)



async def passport_kg_ogpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpBefore18_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_ogpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpBefore18_tmp, parse_mode=types.ParseMode.HTML)



async def passport_kg_ogpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_ogpAfter18)

async def passport_ru_ogpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_ogpAfter18)



async def passport_kg_ogpAfter18Tern_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpAfter18Tern_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_ogpAfter18Tern_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpAfter18Tern_tmp, parse_mode=types.ParseMode.HTML)



async def passport_kg_ogpAfter18Loss_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpAfter18Loss_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_ogpAfter18Loss_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpAfter18Loss_tmp, parse_mode=types.ParseMode.HTML)



async def passport_kg_ogpAfter18Change(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpAfter18Change_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_ogpAfter18Change(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpAfter18Change_tmp, parse_mode=types.ParseMode.HTML)


# ID паспорт
async def passport_kg_idp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_idp)

async def passport_ru_idp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_idp)



async def passport_kg_idpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpBefore18_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_idpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpBefore18_tmp, parse_mode=types.ParseMode.HTML)



async def passport_kg_idpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_idpAfter18)

async def passport_ru_idpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_idpAfter18)


async def passport_kg_idpAfter18Tern_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpAfter18Tern_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_idpAfter18Tern_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpAfter18Tern_tmp, parse_mode=types.ParseMode.HTML)


async def passport_kg_idpAfter18Loss_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpAfter18Loss_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_idpAfter18Loss_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpAfter18Loss_tmp, parse_mode=types.ParseMode.HTML)


async def passport_kg_idpAfter18Change_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpAfter18Change_tmp, parse_mode=types.ParseMode.HTML)

async def passport_ru_idpAfter18Change_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpAfter18Change_tmp, parse_mode=types.ParseMode.HTML)


# Водительское удостоверение
async def driversLincense_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, driversLincense_kg_tmp, parse_mode=types.ParseMode.HTML)
    await message.reply(driversLincense_kg_tmp, parse_mode=types.ParseMode.HTML)

async def driversLincense_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, driversLincense_ru_tmp, parse_mode=types.ParseMode.HTML)
    await message.reply(driversLincense_ru_tmp, parse_mode=types.ParseMode.HTML)



# Предварительная запись------------------------------------------------------------------------------------
async def preRegstration_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Алдын ала катталуу үчүн төмөндөгү шилтемени басыңыз:', reply_markup=urlKb_kg_preReg)

async def preRegstration_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Для записи необходимо перейти по ссылке ниже:', reply_markup=urlKb_ru_preReg)



# Свидетельство о возвращении на Родину----------------------------------------------------------------------
async def svr_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_svr)

async def svr_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_svr)

async def svrBefore18_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrBefore18_kg_tmp, parse_mode=types.ParseMode.HTML)

async def svrBefore18_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrBefore18_ru_tmp, parse_mode=types.ParseMode.HTML)

async def svrAfter18_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrAfter18_kg_tmp, parse_mode=types.ParseMode.HTML)

async def svrAfter18_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrAfter18_ru_tmp, parse_mode=types.ParseMode.HTML)



# Истребование--------------------------------------------------------------------------------------------
async def reclamation_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamation_kg_tmp, reply_markup=kb_kg_reclamation, parse_mode=types.ParseMode.HTML)

async def reclamation_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamation_ru_tmp, reply_markup=kb_ru_reclamation, parse_mode=types.ParseMode.HTML)


async def reclamationCrimRec_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationCrimRec_kg_tmp, parse_mode=types.ParseMode.HTML)

async def reclamationCrimRec_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationCrimRec_ru_tmp, parse_mode=types.ParseMode.HTML)


async def reclamationAuthDL_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationAuthDL_kg_tmp, parse_mode=types.ParseMode.HTML)

async def reclamationAuthDL_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationAuthDL_ru_tmp, parse_mode=types.ParseMode.HTML)


async def reclamationMarriage_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationMarriage_kg_tmp, parse_mode=types.ParseMode.HTML)

async def reclamationMarriage_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, reclamationMarriage_ru_tmp, parse_mode=types.ParseMode.HTML)



# Вопросы ЗАГС
async def issuesMar_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_issuesMar)

async def issuesMar_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_issuesMar)

async def issuesMarRegistration_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, issuesMarRegistration_kg_tmp, parse_mode=types.ParseMode.HTML)

async def issuesMarRegistration_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, issuesMarRegistration_ru_tmp, parse_mode=types.ParseMode.HTML)

async def issuesMarChild_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, issuesMarChild_kg_tmp, parse_mode=types.ParseMode.HTML)

async def issuesMarChild_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, issuesMarChild_ru_tmp, parse_mode=types.ParseMode.HTML)



# Нотариат
async def notaries_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, notaries_kg_tmp, parse_mode=types.ParseMode.HTML)

async def notaries_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, notaries_ru_tmp, parse_mode=types.ParseMode.HTML)


# Юридическая помощь
async def lawyesr_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, lawyesr_kg_tmp, parse_mode=types.ParseMode.HTML)

async def lawyesr_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, lawyesr_ru_tmp, parse_mode=types.ParseMode.HTML)


# Груз 200
async def cargo200_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, cargo200_kg_tmp, parse_mode=types.ParseMode.HTML)

async def cargo200_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, cargo200_ru_tmp, parse_mode=types.ParseMode.HTML)


# Хэндлеры для импорта------------------------------------------------------------------------------------
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

    dp.register_message_handler(service_language_ru_cmd, commands='Русский_язык')
    dp.register_message_handler(service_language_kg_cmd, commands='Кыргыз_тили')

    dp.register_message_handler(mainMenu_kg_cmd, lambda message: 'башкы меню' in message.text.lower())
    dp.register_message_handler(mainMenu_ru_cmd, lambda message: 'главное меню' in message.text.lower())

    dp.register_message_handler(consulate_open_ru_cmd, lambda message: 'график' in message.text.lower()\
        or 'адрес' in message.text.lower())

    dp.register_message_handler(consulate_open_kg_cmd, lambda message: 'дарег' in message.text.lower()\
        or 'иш тартиб' in message.text.lower() or 'кайсыл кундору иш' in message.text.lower())


# Паспорт--------------------------------------------------------------------
    dp.register_message_handler(passport_kg_cmd, lambda message: 'паспорт' in message.text.lower()\
        and 'алуу' in message.text.lower())

    dp.register_message_handler(passport_ru_cmd, lambda message: 'паспорт' in message.text.lower()\
        and 'получ' in message.text.lower())

# ОГП
    dp.register_message_handler(passport_kg_ogp_cmd, lambda message: 'жалпы жарандык' in message.text.lower()\
        and 'паспорт' in message.text.lower())
 
    dp.register_message_handler(passport_ru_ogp_cmd, lambda message: 'общегражданский' in message.text.lower() \
        and 'паспорт' in message.text.lower())


    dp.register_message_handler(passport_kg_ogpBefore18_cmd, lambda message: '18 жашка чейинки' in message.text.lower()\
        and 'өспүрүмдөргө' in message.text.lower())
 
    dp.register_message_handler(passport_ru_ogpBefore18_cmd, lambda message: 'огп' in message.text.lower()\
        and 'до 18 лет' in message.text.lower())

 
    dp.register_message_handler(passport_kg_ogpAfter18_cmd, lambda message: '18 жашка толгон' in message.text.lower()\
        and 'жаран' in message.text.lower())
  
    dp.register_message_handler(passport_ru_ogpAfter18_cmd, lambda message: 'огп' in message.text.lower()\
        and 'старше 18 лет' in message.text.lower())

 
    dp.register_message_handler(passport_kg_ogpAfter18Tern_cmd, lambda message: 'паспорт' in message.text.lower()\
        and 'мөөнөтү өтүп' in message.text.lower() or 'срог' in message.text.lower() and 'бут' in message.text.lower())
 
    dp.register_message_handler(passport_ru_ogpAfter18Tern_cmd, lambda message: 'исте' in message.text.lower()\
        and 'паспорт' in message.text.lower() and 'срок' in message.text.lower() or 'испортился паспорт' in message.text.lower())

  
    dp.register_message_handler(passport_kg_ogpAfter18Loss_cmd, lambda message: 'паспорт' in message.text.lower()\
        and 'жоготуп' in message.text.lower() or 'уурда' in message.text.lower() and 'паспорт' in\
        message.text.lower())
  
    dp.register_message_handler(passport_ru_ogpAfter18Loss_cmd, lambda message: 'теря' in message.text.lower()\
        and 'паспорт' in message.text.lower() or 'украл' in message.text.lower() and 'паспорт' in message.text.lower())

 
    dp.register_message_handler(passport_kg_ogpAfter18Change, lambda message: 'өздүк' in message.text.lower() and 'маалымат' in\
        message.text.lower() and 'өзгө' in message.text.lower() and 'огп' in message.text.lower())
 
    dp.register_message_handler(passport_ru_ogpAfter18Change, lambda message: 'измен' in message.text.lower() and 'персональ' in\
        message.text.lower() and 'данн' in message.text.lower() and 'огп' in message.text.lower())

# ID паспорт
    dp.register_message_handler(passport_kg_idp_cmd, lambda message: 'идентификациялык' in message.text.lower()\
        and 'карт' in message.text.lower()) #or 'айди' in message.text.lower() and 'карт' in message.text.lower())
 
    dp.register_message_handler(passport_ru_idp_cmd, lambda message: 'идентификационная' in message.text.lower()\
        and 'карт' in message.text.lower())# or 'id' in message.text.lower() and 'карт' in message.text.lower())

  
    dp.register_message_handler(passport_kg_idpBefore18_cmd, lambda message: 'чыга элек' in message.text.lower()\
        and 'id' in message.text.lower())# and 'элек' in message.text.lower() and 'id' in message.text.lower())


    dp.register_message_handler(passport_ru_idpBefore18_cmd, lambda message: 'id' in message.text.lower()\
        and 'до 18 лет' in message.text.lower())


    dp.register_message_handler(passport_kg_idpAfter18_cmd, lambda message: 'чыккан' in message.text.lower()\
        and 'id' in message.text.lower())


    dp.register_message_handler(passport_ru_idpAfter18_cmd, lambda message: 'id' in message.text.lower()\
        and 'старше 18' in message.text.lower())


    dp.register_message_handler(passport_kg_idpAfter18Tern_cmd, lambda message: 'id' in message.text.lower()\
        and 'мөөнөтү өтүп' in message.text.lower())

    dp.register_message_handler(passport_ru_idpAfter18Tern_cmd, lambda message: 'истеч' in message.text.lower()\
        and 'срок' in message.text.lower() and 'id' in message.text.lower())


    dp.register_message_handler(passport_kg_idpAfter18Loss_cmd, lambda message: 'id' in message.text.lower()\
        and 'жого' in message.text.lower())

    dp.register_message_handler(passport_ru_idpAfter18Loss_cmd, lambda message: 'теря' in message.text.lower()\
        and 'id' in message.text.lower())


    dp.register_message_handler(passport_kg_idpAfter18Change_cmd, lambda message: 'маалымат' in message.text.lower()\
        and 'өзгөр' in message.text.lower() and 'id' in message.text.lower())


    dp.register_message_handler(passport_ru_idpAfter18Change_cmd, lambda message: 'измен' in message.text.lower()\
        and 'персональ' in message.text.lower() and 'id' in message.text.lower())


# Водительское удостоверение
    dp.register_message_handler(driversLincense_kg_cmd, lambda message: 'айдоочу' in message.text.lower()\
         and 'күбөлүк' in message.text.lower())

    dp.register_message_handler(driversLincense_ru_cmd, lambda message: 'водительское' in message.text.lower()\
         and 'удостоверение' in message.text.lower())


# Электронная очередь-------------------------------------------------------------------------------
    dp.register_message_handler(preRegstration_kg_cmd, lambda message: 'электрондук' in message.text.lower()\
        and 'иретке' in message.text.lower())

    dp.register_message_handler(preRegstration_ru_cmd, lambda message: 'электрон' in message.text.lower()\
        and 'очеред' in message.text.lower())

# СВР----------------------------------------------------------------------------------
    dp.register_message_handler(svr_kg_cmd, lambda message: 'мекенге' in message.text.lower()\
        and 'кайт' in message.text.lower())

    dp.register_message_handler(svr_ru_cmd, lambda message: 'свидетельство' in message.text.lower()\
        and 'возвращен' in message.text.lower())


    dp.register_message_handler(svrBefore18_kg_cmd, lambda message: 'чейинки' in message.text.lower()\
        and 'свр' in message.text.lower())

    dp.register_message_handler(svrBefore18_ru_cmd, lambda message: '18 летнего' in message.text.lower()\
        and 'свр' in message.text.lower())


    dp.register_message_handler(svrAfter18_kg_cmd, lambda message: 'жаштан' in message.text.lower()\
        and 'свр' in message.text.lower())

    dp.register_message_handler(svrAfter18_ru_cmd, lambda message: 'получ' in message.text.lower()\
        and 'свр' in message.text.lower())

# Истребование---------------------------------------------------------------------------------------------
    dp.register_message_handler(reclamation_kg_cmd, lambda message: 'документ' in message.text.lower()\
        and 'сурат' in message.text.lower())

    dp.register_message_handler(reclamation_ru_cmd, lambda message: 'истребова' in message.text.lower()\
        and 'документ' in message.text.lower())


    dp.register_message_handler(reclamationCrimRec_kg_cmd, lambda message: 'соттолгон' in message.text.lower()\
        and 'эмес' in message.text.lower() and 'маалымдама' in message.text.lower())

    dp.register_message_handler(reclamationCrimRec_ru_cmd, lambda message: 'справка' in message.text.lower()\
        and 'отсутств' in message.text.lower() and 'судимост' in message.text.lower())


    dp.register_message_handler(reclamationAuthDL_kg_cmd, lambda message: 'айдоочу' in message.text.lower()\
        and 'күбөлүг' in message.text.lower() and 'нускасы' in message.text.lower())

    dp.register_message_handler(reclamationAuthDL_ru_cmd, lambda message: 'подтверждение' in message.text.lower()\
        and 'подлинности' in message.text.lower() and 'ву' in message.text.lower())


    dp.register_message_handler(reclamationMarriage_kg_cmd, lambda message: 'нике' in message.text.lower()\
        and 'тууралуу' in message.text.lower() and 'күбөлүк' in message.text.lower())

    dp.register_message_handler(reclamationMarriage_ru_cmd, lambda message: 'справка' in message.text.lower()\
        and 'семейн' in message.text.lower() and 'положен' in message.text.lower())

# Вопросы ЗАГС-----------------------------------------------------------------------------------------
    dp.register_message_handler(issuesMar_kg_cmd, lambda message: 'загс' in message.text.lower()\
        and 'маселе' in message.text.lower())

    dp.register_message_handler(issuesMar_ru_cmd, lambda message: 'вопрос' in message.text.lower()\
        and 'загс' in message.text.lower())


    dp.register_message_handler(issuesMarRegistration_kg_cmd, lambda message: 'нике' in message.text.lower()\
        and 'катт' in message.text.lower())

    dp.register_message_handler(issuesMarRegistration_ru_cmd, lambda message: 'регистр' in message.text.lower()\
        and 'брак' in message.text.lower())


    dp.register_message_handler(issuesMarChild_kg_cmd, lambda message: 'бала' in message.text.lower()\
        and 'туулган' in message.text.lower() and 'күбөлүг' in message.text.lower())

    dp.register_message_handler(issuesMarChild_ru_cmd, lambda message: 'ребен' in message.text.lower()\
        and 'свидетел' in message.text.lower() and 'рождени' in message.text.lower())


    dp.register_message_handler(notaries_kg_cmd, lambda message: 'нотари' in message.text.lower()\
        and 'маселе' in message.text.lower())
        
    dp.register_message_handler(notaries_ru_cmd, lambda message: 'нотари' in message.text.lower()\
        and 'вопрос' in message.text.lower())

# Юридическая помощь----------------------------------------------------------------------------------
    dp.register_message_handler(lawyesr_kg_cmd, lambda message: 'юрид' in message.text.lower()\
        and 'жардам' in message.text.lower())
   
    dp.register_message_handler(lawyesr_ru_cmd, lambda message: 'юрид' in message.text.lower()\
        and 'помощь' in message.text.lower())

# Груз 200
    dp.register_message_handler(cargo200_kg_cmd, lambda message: 'жүк' in message.text.lower()\
        and '200' in message.text.lower())

    dp.register_message_handler(cargo200_ru_cmd, lambda message: 'груз' in message.text.lower()\
        and '200' in message.text.lower())

