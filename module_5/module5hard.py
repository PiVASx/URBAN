import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *args):
        for vid in args:
            if not any(vid.title == t_video.title for t_video in self.videos):
                self.videos.append(vid)

    def log_in(self, nickname, password):
        for us in self.users:
            if us.nickname == us.nickname and us.password == hash(password):
                self.current_user = nickname

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def get_videos(self, google):
        return [vid.title for vid in self.videos if vid.title.lower().find(google.lower()) != -1]

    def watch_video(self, google):
        if not self.current_user:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return
        for us in self.users:
            if us.nickname == self.current_user:
                if us.age < 18:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
        for second in range(1, self.videos.duration + 1):
            print(f"Секунда: {second}")
            time.sleep(1)
        #if any(vid for vid in self.videos if vid.title == google):

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Лучший язык программирования 2024 года', 200)

# Добавление видео
ur.add(v1, v2, v3)
print(f'Количество видео в архиве {len(ur.videos)}')

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
