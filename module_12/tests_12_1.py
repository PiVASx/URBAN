import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        tr = Runner('User')
        [tr.walk() for _ in range(10)]
        self.assertEqual(tr.distance, 50)

    def test_run(self):
        tr = Runner('User')
        [tr.run() for _ in range(10)]
        self.assertEqual(tr.distance, 100)

    def test_challenge(self):
        tr1 = Runner('User1')
        tr2 = Runner('User2')
        [tr1.walk() for _ in range(10)]
        [tr2.run() for _ in range(10)]
        self.assertNotEqual(tr1.distance, tr2.distance)

if __name__ == '__main__':
    unittest.main()