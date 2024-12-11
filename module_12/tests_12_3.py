import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tr = Runner('User')
        [tr.walk() for _ in range(10)]
        self.assertEqual(tr.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tr = Runner('User')
        [tr.run() for _ in range(10)]
        self.assertEqual(tr.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tr1 = Runner('User1')
        tr2 = Runner('User2')
        [tr1.walk() for _ in range(10)]
        [tr2.run() for _ in range(10)]
        self.assertNotEqual(tr1.distance, tr2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runners = []
        self.runners.append(Runner('Усэйн', 10))
        self.runners.append(Runner('Андрей', 9))
        self.runners.append(Runner('Ник', 3))

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f"{key}: {result}")

    def run_tournament(self, distance, expected_winner, *participants):
        tournament = Tournament(distance, *participants)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = {place: runner.name for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name, expected_winner)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_usain_nik(self):
        self.run_tournament(90, 'Ник', self.runners[0], self.runners[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_andrey_nik(self):
        self.run_tournament(90, 'Ник', self.runners[1], self.runners[2])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_all(self):
        self.run_tournament(90, 'Ник', *self.runners)
