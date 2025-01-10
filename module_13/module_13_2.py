from aiogram import Bot, Dispatcher, executor, types
from settings import API_TOKEN

# API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
