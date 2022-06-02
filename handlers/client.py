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
    await bot.send_message(message.from_user.id, 'Кызматты тандаңыз', reply_markup=kb_main_kg_menu)

async def service_language_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=kb_main_ru_menu)



# Главное меню------------------------------------------------------------------------------------
async def mainMenu_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Кызматты тандаңыз', reply_markup=kb_main_kg_menu)

async def mainMenu_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=kb_main_ru_menu)



# Адрес и график работы------------------------------------------------------------------------------------
async def consulate_open_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'График работы: Пн-Пт с 9:00 до 18:00. Адрес: Москва, ул. Большая Ордынка, 62 стр. 2 (вход с Погорельского переулка')

async def consulate_open_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Москва ш. Большая Ордынка к. 62/1. (метро Добрынинская). Дүйшөмбү-Жума күндөрү саат 9:00-18:00 чейин.')



# Паспорт------------------------------------------------------------------------------------
async def passport_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_passport_kg)

async def passport_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_passport_ru)



async def passport_kg_ogp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_ogp)

async def passport_ru_ogp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_ogp)



async def passport_kg_ogpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpBefore18_tmp)

async def passport_ru_ogpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpBefore18_tmp)



async def passport_kg_ogpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_ogpAfter18_tmp)

async def passport_ru_ogpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_ogpAfter18_tmp)



async def passport_kg_idp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_idp)

async def passport_ru_idp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_idp)



async def passport_kg_idpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpBefore18_tmp)

async def passport_ru_idpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpBefore18_tmp)



async def passport_kg_idpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_kg_idpAfter18_tmp)

async def passport_ru_idpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, passport_ru_idpAfter18_tmp)



# Предварительная запись------------------------------------------------------------------------------------
async def preRegstration_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Алдын ала катталуу үчүн төмөндөгү шилтемени басыңыз', reply_markup=urlKb_kg_preReg)

async def preRegstration_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Для записи необходимо перейти по ссылке ниже', reply_markup=urlKb_ru_preReg)



# Свидетельство о возвращении на Родину----------------------------------------------------------------------
async def svr_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_svr)

async def svr_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите нужный вариант', reply_markup=kb_ru_svr)

async def svrBefore18_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrBefore_kg_tmp)

async def svrBefore18_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrBefore_ru_tmp)

async def svrAfter18_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrAfter18_kg_tmp)

async def svrAfter18_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, svrAfter18_ru_tmp)


# Хэндлеры для импорта------------------------------------------------------------------------------------
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

    dp.register_message_handler(service_language_ru_cmd, commands='Русский_язык')
    dp.register_message_handler(service_language_kg_cmd, commands='Кыргыз_тили')

    dp.register_message_handler(mainMenu_kg_cmd, commands=['Башкы_меню'])
    dp.register_message_handler(mainMenu_ru_cmd, commands=['Главное_меню'])

    dp.register_message_handler(consulate_open_ru_cmd, commands=['Адрес_и_график_работы'])
    dp.register_message_handler(consulate_open_kg_cmd, commands=['Дареги_жана_иш_тартиби'])

    dp.register_message_handler(passport_kg_cmd, commands=['Паспорт_алуу'])
    dp.register_message_handler(passport_ru_cmd, commands=['Получение_паспорта'])

    dp.register_message_handler(passport_kg_ogp_cmd, commands=['Жалпы_жарандык_паспорт'])
    dp.register_message_handler(passport_ru_ogp_cmd, commands=['Общегражданский_паспорт(Загран_паспорт)'])

    dp.register_message_handler(passport_kg_ogpBefore18_cmd, commands=['18-жашка_чейинки_өспүрүмдөргө'])
    dp.register_message_handler(passport_ru_ogpBefore18_cmd, commands=['Для_получения_ОГП_гражданам_до_18_лет'])

    dp.register_message_handler(passport_kg_ogpAfter18_cmd, commands=['18-жашка_толгон_жарандарга'])
    dp.register_message_handler(passport_ru_ogpAfter18_cmd, commands=['Для_получения_ОГП_гражданам_старше_18_лет'])

    dp.register_message_handler(passport_kg_idp_cmd, commands=['Идентификациялык_карта(ID-паспорт)'])
    dp.register_message_handler(passport_ru_idp_cmd, commands=['Идентификационный_паспорт_(ID)'])

    dp.register_message_handler(passport_kg_idpBefore18_cmd, commands=['18-жашка_чыга_элек_жаранга_ID-паспорт_алуу'])
    dp.register_message_handler(passport_ru_idpBefore18_cmd, commands=['Для_получения_ID_паспорта_гражданам_до_18_лет'])

    dp.register_message_handler(passport_kg_idpAfter18_cmd, commands=['18-жашка_чыккан_жарандарга_ID-паспорт_алуу'])
    dp.register_message_handler(passport_ru_idpAfter18_cmd, commands=['Для_получения_ID_паспорта_гражданам_старше_18_лет'])

    dp.register_message_handler(preRegstration_kg_cmd, commands=['Электрондук_иретке_катталуу'])
    dp.register_message_handler(preRegstration_ru_cmd, commands=['Электронная_очередь'])

    dp.register_message_handler(svr_kg_cmd, commands=['Мекенге_кайтуу_күбөлүгү'])
    dp.register_message_handler(svr_ru_cmd, commands=['Свидетельство_на_возвращение_на_родину'])

    dp.register_message_handler(svrBefore18_kg_cmd, commands=['18-жашка_чейинки_балдарга_СВР_алуу'])
    dp.register_message_handler(svrBefore18_ru_cmd, commands=['Получение_СВР_до_18-летнего_возраста'])

    dp.register_message_handler(svrAfter18_kg_cmd, commands=['18-жаштан_өйдө_жарандарга_СВР_алуу'])
    dp.register_message_handler(svrAfter18_ru_cmd, commands=['Получение_СВР_старше_18-лет_(при_утере_документов)'])

