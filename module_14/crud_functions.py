import sqlite3

def create_connection(db_file):
    """Создание подключения к базе данных SQLite."""
    conn = sqlite3.connect(db_file)
    return conn

def drop_tables(conn):
    """Удаление Products, если она существует."""
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Products')
    conn.commit()

def initiate_db(conn):
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
