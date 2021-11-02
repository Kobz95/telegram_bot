from aiogram import Bot, Dispatcher, executor
from config import API_TOKEN


bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

if __name__ == '__name__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)