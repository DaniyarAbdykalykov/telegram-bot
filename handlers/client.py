from aiogram import Dispatcher, types
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вас приветствует чат-бот консульского отдела Посольства КР в РФ!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/KyrgyzConsulate_ruBot')

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
