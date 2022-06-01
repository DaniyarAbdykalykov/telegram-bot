from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_language, kb_ru_schedule
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Саламатсызбы! Сиз менен электрондук консул байланышта. Керектүү тилди тандаңыз\nВас приветствует электронный консул Посольства Кыргызской Республики в Российской Федерации! Выберите язык обслуживания', reply_markup=kb_language)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/KyrgyzConsulate_ruBot')

# язык обслуживания
async def service_language_ru(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберите услугу', reply_markup=kb_ru_schedule)

# @dp.message_handler(commands=['Режим_работы'])
async def consulate_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 18:00')

# @dp.message_handler(commands=['Расположение'])
async def consulate_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Москва, ул. Большая Ордынка, 62 стр. 2 (вход с Погорельского переулка)') #reply_markup=ReplyKeyboardRemove())

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(consulate_open_command, commands=['Режим_работы'])
    dp.register_message_handler(consulate_place_command, commands='Расположение')
    dp.register_message_handler(service_language_ru, commands='Русский_язык')
