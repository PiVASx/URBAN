from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

from settings import API_TOKEN

# API_TOKEN = ''
storage = MemoryStorage()  # Используем хранилище для управления состоянием
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


# States
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup()
batton = KeyboardButton(text='Рассчитать')
batton2 = KeyboardButton(text='Информация')
kb.row(batton, batton2)



@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Что я умею:\nМогу посчитать суточную норму калорий.', reply_markup=kb)


# Подсчёт калорий
@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(id_user=message.from_user.id)
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    user_data = await state.get_data()
    print(
        f"id_user: {user_data['id_user']}, Возраст: {user_data['age']}, Рост: {user_data['growth']}, Вес: {user_data['weight']}")

    # Извлекаем данные
    age = int(user_data['age'])
    weight = float(user_data['weight'])
    growth = float(user_data['growth'])

    # Расчет BMR по формуле Миффлина-Сан Жеора для мужчины
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваш норма калорий в день {bmr:.2f}.")
    await state.finish()


@dp.message_handler()
async def all_massages(message: types.Message):
    await message.answer('Жми /start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
