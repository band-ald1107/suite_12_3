import unittest
from module_12_2 import Runner, TournamentTest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertTrue(True)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertTrue(True)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
