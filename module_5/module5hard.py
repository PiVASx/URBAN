class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.password == hash(other)

class UrTube:
    pass


class Video:
    pass


x = User('asdasd', '123', 12)
print(x.password)
print(x.password == hash('123'))
