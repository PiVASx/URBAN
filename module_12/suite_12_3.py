import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание объекта TestSuite
suite = unittest.TestSuite()


# Добавление тестов из RunnerTest и TournamentTest
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))

# Создание объекта TextTestRunner с verbosity=2
if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

