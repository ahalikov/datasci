from unittest import TestCase
import assignment1.happiest_state as hs
from assignment1.happiest_state import load_scores
from assignment1.happiest_state import get_happiest_state

__author__ = 'Artur'

class TestGet_happiest_state(TestCase):
    def setUp(self):
        self.temp_dir = '../temp/'
        self.scores = load_scores(self.temp_dir + 'AFINN-111.txt')

    def test_get_happiest_state(self):
        hs.ENCODE_TEXT = False
        test = 'test5.txt'
        file = open(self.temp_dir + test)
        self.assertEqual('CA', get_happiest_state(file, self.scores))
        return