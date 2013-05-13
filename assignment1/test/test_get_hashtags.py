from unittest import TestCase
from assignment1.top_ten import get_hashtags
import assignment1.top_ten as topten

__author__ = 'Artur'

class TestGet_hashtags(TestCase):

    def setUp(self):
        self.temp_dir = '../temp/'

    def test_get_hashtags(self):
        topten.encode_text = False
        test = 'test5.txt'
        fp = open(self.temp_dir + test)
        hashtags = get_hashtags(fp)
        print(hashtags)

        return