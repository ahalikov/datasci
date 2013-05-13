from unittest import TestCase
from assignment1.top_ten import get_hash_tags
import assignment1.top_ten as topten

__author__ = 'Artur'

class TestGet_hash_tags(TestCase):

    def setUp(self):
        self.temp_dir = '../temp/'

    def test_get_hash_tags(self):
        topten.encode_text = False
        test = 'test5.txt'
        fp = open(self.temp_dir + test)
        tags = get_hash_tags(fp)
        self.assertEqual({'#Love':2, '#Streets':1, '#NewYork':1}, tags)


        return