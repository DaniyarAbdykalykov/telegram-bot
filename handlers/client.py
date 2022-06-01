from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import *
from aiogram.types import ReplyKeyboardRemove

# Приветствие
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Саламатсызбы! Сиз менен Кыргыз Республикасынын Россия Федерациясындагы Элчилигинин электрондук консулу байланышта. Керектүү тилди тандаңыз\n\nВас приветствует электронный консул Посольства Кыргызской Республики в Российской Федерации! Выберите нужный язык обслуживания', reply_markup=kb_language)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/KyrgyzConsulate_ruBot')



# Выбор языка
async def service_language_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Кызматты тандаңыз', reply_markup=kb_main_kg_menu)

async def service_language_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=kb_main_ru_menu)



# Адрес и график работы
async def consulate_open_ru_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'График работы: Пн-Пт с 9:00 до 18:00. Адрес: Москва, ул. Большая Ордынка, 62 стр. 2 (вход с Погорельского переулка')

async def consulate_open_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Москва ш. Большая Ордынка к. 62/1. (метро Добрынинская). Дүйшөмбү-Жума күндөрү саат 9:00-18:00 чейин.')



# Паспорт
async def passport_kg_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_passport_kg)

async def passport_kg_ogp_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, 'Ылайыктуу себебин тандаңыз', reply_markup=kb_kg_ogp)

async def passport_kg_ogpBefore18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, '18-жашка чыга элек КРнын жаранынын атына КРнын жалпы жарандык паспортун тариздөө/алмаштыруу максатында төмөндөгү документтер керектелет:')

async def passport_kg_ogpAfter18_cmd(message : types.Message):
    await bot.send_message(message.from_user.id, '18-жашка чыккан КРнын жарандын атына КРнын жалпы жарандык паспортун алмаштыруу максатында төмөндөгү документтер керектелет (жаран өздүк маалыматтарын өзгөрткөн учурунда):')

# Хэндлеры для импорта
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])

    dp.register_message_handler(service_language_ru_cmd, commands='Русский_язык')
    dp.register_message_handler(service_language_kg_cmd, commands='Кыргыз_тили')

    dp.register_message_handler(consulate_open_ru_cmd, commands=['Адрес_и_график_работы'])
    dp.register_message_handler(consulate_open_kg_cmd, commands=['Дареги_жана_иш_тартиби'])

    dp.register_message_handler(passport_kg_cmd, commands=['Паспорт_алуу'])

    dp.register_message_handler(passport_kg_ogp_cmd, commands=['Жалпы_жарандык_паспорт'])

    dp.register_message_handler(passport_kg_ogpBefore18_cmd, commands=['18-жашка_чейинки_өспүрүмдөргө'])
    dp.register_message_handler(passport_kg_ogpAfter18_cmd, commands=['18-жашка_толгон_жарандарга'])