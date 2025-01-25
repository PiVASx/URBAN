import sqlite3

# подключение к базе
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Удаление пользователя с id=6
cursor.execute('''
DELETE FROM Users WHERE id = 6
''')

# Подсчёт общего количества пользователей
cursor.execute('''
SELECT COUNT(*) FROM Users
''')
total_users = cursor.fetchone()[0]  # Получаем общее количество записей

# Подсчёт суммы всех балансов
cursor.execute('''
SELECT SUM(balance) FROM Users
''')

# Подсчет среднего баланса пользователей
cursor.execute('''
SELECT AVG(balance) FROM Users
''')

average_balance = cursor.fetchone()[0]  # Получаем средний баланс

# Вывод среднего баланса
print(average_balance)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
