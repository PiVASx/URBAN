def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid = ['@', '.com', '.ru', '.net']
    check = []  # храним bool
    # В цикле проходимся по recipient и sender для определения корректности
    # Собирая все в check
    for email in [recipient, sender]:
        for val in valid[1:]:
            if val in email:
                check.append(True)
            else:
                check.append(False)

    if not all([valid[0] in recipient, valid[0] in sender, any(check[:3]), any(check[3:])]):
        return print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    if sender == recipient:
        return print(f"Нельзя отправить письмо самому себе!")
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    # message определил чтоб не болталась.
    if message:
        pass


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender='urban.infogmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', sender='urban.info@gmail.su')
