from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from crud_functions import *
from settings import API_TOKEN


# Создание соединения с базой данных
conn = create_connection('not_telegram.db')

# Очищаем таблицу если она существует.
clear_tables_products(conn)

# Инициализация таблицы Products
initiate_db_products(conn)

# Очищаем таблицу если она существует.
clear_tables_users(conn)

# Инициализация таблицы Products
initiate_db_users(conn)


# Добавляем записи в базы
add_product(conn, 'Продукт 1', 'Описание продукта 1', 100)
add_product(conn, 'Продукт 2', 'Описание продукта 2', 200)
add_product(conn, 'Продукт 3', 'Описание продукта 3', 300)
add_product(conn, 'Продукт 4', 'Описание продукта 4', 400)

add_user(conn, 'newuser', 'user@gmail.com', '33')

# Получаем все записи из базы.
products = get_all_products(conn)



# Создаем хранилище для управления состоянием пользователя
storage = MemoryStorage()

# Инициализируем бота с токеном API
bot = Bot(token=API_TOKEN)

# Создаем диспетчер для управления обработчиками
dp = Dispatcher(bot, storage=storage)

# Определяем состояния для FSM (Finite State Machine) расчет калорий
class UserState(StatesGroup):
    age = State()  # Состояние для ввода возраста
    growth = State()  # Состояние для ввода роста
    weight = State()  # Состояние для ввода веса

# Определяем состояния для FSM (Finite State Machine) расчет калорий. Регистрация.
class RegistrationState(StatesGroup):
    username = State()  # Состояние для имени(латиница)
    email = State()  # Состояние для ввода email
    age = State()  # Состояние для ввода возраста


# Создаем клавиатуру для текстовых кнопок
start_menu = ReplyKeyboardMarkup(
    keyboard=[
        # Располагаем кнопки в строку
        [
            KeyboardButton(text='Рассчитать'),  # Кнопка для расчета калорий
            KeyboardButton(text='Информация')  # Кнопка для получения информации
        ],
        [
            KeyboardButton(text='Купить'),  # Кнопка каталога
        ],
        [
            KeyboardButton(text='Регистрация'),  # Кнопка Регистрации
        ]
    ], resize_keyboard=True
)

# Создаем инлайн-клавиатуру для выбора опции
ikb = InlineKeyboardMarkup()
i_batton = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
i_batton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.row(i_batton, i_batton2)  # Располагаем кнопки в строку

# Создаем инлайн-клавиатуру для продуктов
iprod = InlineKeyboardMarkup()
i_product1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
i_product2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
i_product3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
i_product4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
iprod.row(i_product1, i_product2, i_product3, i_product4)  # Располагаем кнопки в строку

# Обработчик команды /start и /help
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')
    # Вызываем клавиатуру Рассчитать/Информация
    await message.answer('Что я умею:\n- Могу посчитать суточную норму калорий.\n- Магазин гирь',
                         reply_markup=start_menu)


# Обработчик текстовой команды "Рассчитать"
@dp.message_handler(text='Рассчитать')
async def inline_menu(message: types.Message):
    # Вызываем инлайн-клавиатуру Рассчитать норму калорий/Формулы расчёта
    await message.answer('Выберите опцию:', reply_markup=ikb)


# Обработчик нажатия на инлайн-кнопку "Рассчитать норму калорий"
@dp.callback_query_handler(text='calories')
async def calculate_calories(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')  # Запрашиваем возраст
    await UserState.age.set()  # Устанавливаем состояние для возраста
    await call.answer()  # Подтверждаем нажатие кнопки


# Обработчик текста "Рассчитать норму калорий"
@dp.message_handler(text='Рассчитать норму калорий')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')  # Запрашиваем возраст
    await UserState.age.set()  # Устанавливаем состояние для возраста


# Обработчик состояния ввода возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(id_user=message.from_user.id)  # Сохраняем ID пользователя
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer('Введите свой рост:')  # Запрашиваем рост
    await UserState.growth.set()  # Устанавливаем состояние для роста


# Обработчик состояния ввода роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer('Введите свой вес:')  # Запрашиваем вес
    await UserState.weight.set()  # Устанавливаем состояние для веса


# Обработчик состояния ввода веса
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    user_data = await state.get_data()  # Извлекаем сохраненные данные
    print(
        f"id_user: {user_data['id_user']}, Возраст: {user_data['age']}, Рост: {user_data['growth']}, Вес: {user_data['weight']}")

    # Извлекаем данные
    age = int(user_data['age'])  # Преобразуем возраст в целое число
    weight = float(user_data['weight'])  # Преобразуем вес в число с плавающей точкой
    growth = float(user_data['growth'])  # Преобразуем рост в число с плавающей точкой

    # Расчет BMR по формуле Миффлина-Сан Жеора для мужчины
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий в день: {bmr:.2f}.")  # Отправляем результат пользователю
    await state.finish()  # Завершаем состояние

#### Блок регистрации ####

# Обработчик текста "Регистрация"
@dp.message_handler(text='Регистрация')
async def sing_up(message: types.Message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')  # Запрашиваем имя пользователя
    await RegistrationState.username.set()  # Устанавливаем состояние для имени

# Обработчик состояния ввода username
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    await state.update_data(username=message.text)  # Сохраняем username
    # Проверка на существующие имя
    if is_included(conn, message.text):
        await message.answer('Пользователь существует, введите другое имя')  # Запрашиваем имя пользователя
        await RegistrationState.username.set()  # Устанавливаем состояние для имени
    else:
        await message.answer('Введите свой email')  # Запрашиваем рост
        await RegistrationState.email.set()  # Устанавливаем состояние для роста

# Обработчик состояния ввода email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)  # Сохраняем email
    await message.answer('Введите свой возраст:')  # Запрашиваем рост
    await RegistrationState.age.set()  # Устанавливаем состояние для роста

# Обработчик состояния ввода возраст
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем email
    user_data = await state.get_data()  # Извлекаем сохраненные данные
    # Добавляем нового пользователя.
    add_user(conn, user_data['username'], user_data['email'], user_data['age'])
    await message.answer('=^◕⩊◕^=\nСпасибо, за регистрацию!!!')  # Запрашиваем рост
    print(
        f"Новый пользователь, Ник: {user_data['username']}, Мыло: {user_data['email']}, Возраст: {user_data['age']}")

    await state.finish()  # Завершаем состояние

##### Конец блока регистрации.  #####

# Обработчик нажатия на инлайн-кнопку "Информация"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()  # Подтверждаем нажатие кнопки


# Обработчик Покупок
@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    for product in products:
        with open('5.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        _, title, description, price = product
        await message.answer(
        f"Название: {title} | Описание: {description} | Цена: {price}₽"
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=iprod)

# Обработчик нажатия на инлайн-кнопку "Купить продукт"
@dp.callback_query_handler(text='product_buying')
async def buy_product(call: types.CallbackQuery):
    await call.message.answer("Вы выбрали продукт. Спасибо за покупку!")
    await call.answer()  # Подтверждаем нажатие кнопки


# Обработчик для всех остальных сообщений
@dp.message_handler()
async def all_massages(message: types.Message):
    await message.answer('Жми /start')  # Напоминаем пользователю о команде /start


# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
