team1_num = 5
print("В команде Мастера кода участников: %s !" % team1_num)

# Переменные: количество участников в обеих командах (team1_num, team2_num).
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
#
# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
score_2 = 42
print("Команда Волшебники данных решила задач: {0} !".format(score_2))
# Пример итоговой строки: "Команда Волшебники данных решила задач: 42 !"
#
# Переменные: время за которое команда 2 решила задачи (team1_time).
team1_time = 18015.2
print("Волшебники данных решили задачи за {0} с !".format(team1_time))
# Использование f-строк:
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")

# Переменные: исход соревнования (challenge_result).
print(f"Результат битвы: победа команды Мастера кода!")

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
