from unittest import TestCase
from assignment1.happiest_state import get_state
from assignment1.happiest_state import load_scores

__author__ = 'Artur'

class TestGet_state(TestCase):
    def setUp(self):
        self.temp_dir = '../temp/'
        self.scores = load_scores(self.temp_dir + 'AFINN-111.txt')

    def test_get_state(self):
        tweet = {"text":"", "user":{"location":"San-Francisco, CA"}, "place": {"country_code": "US"}}
        self.assertEqual('CA', get_state(tweet))

        tweet = {"text":"", "user":{}, "place": {"country_code": "US", "full_name": "Washington, DC"}}
        self.assertEqual('DC', get_state(tweet))
        return
