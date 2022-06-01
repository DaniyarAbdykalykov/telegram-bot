# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram import Dispatcher, types
# from create_bot import dp
# from aiogram.dispatcher.filters import Text

# class FSMAdmin(StatesGroup):
#     service_name = State()
#     description = State() 

#                                                 # Начало диалога загрузки нового пункта услуги
# async def cm_start(message : types.Message):
#     await FSMAdmin.service_name.set()
#     await message.reply('Напишите название услуги')

#                                                 #Ловим первый ответ и пишем в словарь
# async def load_service_name(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['service_name'] = message.text
#     await FSMAdmin.next()
#     await message.reply('Теперь введите описание услуги')

#                                                 # Ловим второй ответ
# async def load_description(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['description'] = message.text
    
#     async with state.proxy() as data:
#         await message.reply(str(data))
#     await state.finish

#                                                 #Выход из состояний
# async def cancel_handler(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Ок')

#                                                 # Регистрируем хендлеры
# def register_handlers_admin(dp : Dispatcher):
#     dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
#     dp.register_message_handler(load_service_name, state=FSMAdmin.service_name)
#     dp.register_message_handler(load_description, state=FSMAdmin.description)
#     dp.register_message_handler(cancel_handler, state="*", commands='отмена')
#     dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
