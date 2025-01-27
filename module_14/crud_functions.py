import sqlite3

def create_connection(db_file):
    """Создание подключения к базе данных SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

def clear_tables_products(conn):
    """Удаляем Products, если она существует."""
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Products')
    conn.commit()

def initiate_db_products(conn):
    """Создание таблицы Products."""
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    conn.commit()

def initiate_db_users(conn):
    """Создание таблицы User."""
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age TEXT NOT NULL,
        balance INTEGER NOT NULL
    )
    ''')
    conn.commit()

def clear_tables_users(conn):
    """Удаляем Users, если она существует."""
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Users')
    conn.commit()

def get_all_products(conn):
    """Получение всех записей из таблицы Products."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_product(conn, title, description, price):
    """Добавление нового продукта в таблицу Products."""
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))
    conn.commit()

def add_user(conn, username, email, age):
    """Добавление нового пользователя в таблицу Users."""
    cursor = conn.cursor()
    balance = 1000
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, balance))
    conn.commit()

def is_included(conn, username):
    """Проверяет пользователя, возвращает True,
     если такой пользователь есть в таблице Users,
     в противном случае False"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    # Получаем одну запись
    result = cursor.fetchone()
    return result is not None
