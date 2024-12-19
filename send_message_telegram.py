
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from main import login, original_version, search_all_versions, serch_up_for_my_version, update_version, VERSION

import os


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

# Стартовое меню
@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['Текущая версия', 'Проверить обновление', 'Обновить версию']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Выберите действие', reply_markup=keyboard)
    
# Нажатие на кнопку Текущая версия
@dp.message_handler(Text(equals='Текущая версия'))
async def send_version(message: types.Message):    
    await message.answer(f'Текущая версия: {original_version(VERSION)}')

# Нажатие на кнопку Проверить обновление
@dp.message_handler(Text(equals='Проверить обновление'))
async def search_updates(message: types.Message):
    login(os.getenv('URL'), os.getenv('LOGIN'), os.getenv('PASSWORD'))   
    search_all_versions('list_base.html')
    await message.answer(serch_up_for_my_version('list_releases.json', VERSION))

# Нажатие на кнопку Обновить версию
@dp.message_handler(Text(equals='Обновить версию'))
async def update_version_in_sistem(message: types.Message): 
    up_kb = ["Обновить версию", "Назад"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*up_kb)
    await message.answer('Выберите действие', reply_markup=keyboard)

@dp.message_handler(Text(equals='Обновить версию'))
async def send_version(message: types.Message):
    if message.text =='Обновить версию':
        update_version(message.text)        
        await message.answer(f'Версия обновлена. Текущая версия: {VERSION[0]}')
    # elif message.text =='Назад':
    #     start()

   
    
def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()
