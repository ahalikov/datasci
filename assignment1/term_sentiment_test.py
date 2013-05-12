import unittest
import term_sentiment as ts

class TestTermSentiment(unittest.TestCase):

    def setUp(self):
        self.scores = ts.load_scores('AFINN-111.txt')
        self.temp_dir = '/home/artur/work/study/datasci/temp/'

    def test_score_tweet(self):
        score, new_terms, n = ts.score_tweet([], self.scores)
        self.assertEqual(0, score)
        self.assertEqual({}, new_terms)
        
        score, new_terms, n = ts.score_tweet("foo bar abandon bar".split(), self.scores)
        self.assertEqual(-2, score)
        self.assertEqual({'foo':1, 'bar':1}, new_terms)
        
        score, new_terms, n = ts.score_tweet("foo bar abandon bar abandon".split(), self.scores)
        self.assertEqual(-2, score)
        self.assertEqual({'foo':1, 'bar':1}, new_terms)
    
        score, new_terms, n = ts.score_tweet("accept friend".split(), self.scores)
        self.assertEqual(1, score)
        return
        
    def test_score_new_terms(self):
        new_scores = ts.score_new_terms("foo bar abandon bar", self.scores, {})
        self.assertEqual({'foo':-0.5, 'bar':-0.5}, new_scores)
        return
        
    def test_score_file(self):        
        tf = open(self.temp_dir + 'test1.txt') # tweet file
        res = ts.score_file(tf, self.scores)
        self.assertEqual({'stress': -21.0/11}, res)
        
        tf = open(self.temp_dir + 'test2.txt') # tweet file
        res = ts.score_file(tf, self.scores)
        self.assertEqual({'friend': 0.65625}, res)
        
        tf = open(self.temp_dir + 'test3.txt') # tweet file
        res = ts.score_file(tf, self.scores)
        self.assertEqual({'the': 0}, res)
        
        tf = open(self.temp_dir + 'test4.txt') # tweet file
        res = ts.score_file(tf, self.scores)
        print '------------------------------------------------'
        return
        
        
    def test_find(self):
        terms = ['love', 'happiness', 'ship', 'love']
        self.assertEqual(True, ts.find(terms, 'love'))
        self.assertEqual(['happiness', 'ship'], terms)
   
if __name__ == '__main__':
    unittest.main()
