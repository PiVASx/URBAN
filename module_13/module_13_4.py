from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


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


@dp.message_handler(text='Calories')
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
    print(f"id_user: {user_data['id_user']}, Возраст: {user_data['age']}, Рост: {user_data['growth']}, Вес: {user_data['weight']}")

    # Извлекаем данные
    age = int(user_data['age'])
    weight = float(user_data['weight'])
    growth = float(user_data['growth'])

    # Расчет BMR по формуле Миффлина-Сан Жеора для мужчины
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваш норма калорий в день {bmr:.2f}.")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
