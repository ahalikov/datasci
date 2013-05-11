import unittest
import term_sentiment as ts

class TestTermSentiment(unittest.TestCase):

    def setUp(self):
        self.scores = ts.load_scores('AFINN-111.txt')

    def test_score_tweet(self):
        ts.score_tweet("", self.scores)
        self.assertEqual({}, ts.new_scores)
        
        ts.score_tweet("foo bar abandon bar", self.scores)
        self.assertEqual({'foo':(-2,1), 'bar':(-2,2)}, ts.new_scores)
        
        ts.score_tweet("accept absolved adorable adventure award backing backs awesome attracts benefit stress", self.scores)
        self.assertEqual((21.0, 1), ts.new_scores['stress'])
        self.assertEqual((-2.0, 1), ts.new_scores['foo'])
        self.assertEqual((-2.0, 2), ts.new_scores['bar'])
        
        ts.score_tweet("barrier bastards benefitted chastises charged charmless chastises cheat giddy gloomy friend", self.scores)
        self.assertEqual((-21.0, 1), ts.new_scores['friend'])
        
        ts.score_tweet("barrier fuck bad worse bastards benefitted chastises charged charmless chastises cheat giddy gloomy stress", self.scores)
        self.assertEqual((-10.0, 2), ts.new_scores['stress'])
        
        ts.score_tweet("foo bar stress bar", self.scores)
        self.assertEqual((-16.0, 3), ts.new_scores['stress'])
        self.assertEqual((-16.0, 2), ts.new_scores['foo'])
        self.assertEqual((-16.0, 4), ts.new_scores['bar'])
        
        ts.score_tweet("Suicide Doesnt End The Chances Of Life Gettin Worse, Suicide Eliminates The Possibility Of It Ever Gettin Better", self.scores)
        #print ts.new_scores
        
    def test_find(self):
        terms = ['love', 'happiness', 'ship', 'love']
        count = ts.find(terms, 'love')
        self.assertEqual(2, count)
        
        terms = "barrier bastards benefitted chastises charged charmless chastises cheat giddy gloomy stress".split()
        ts.find(terms, 'barrier')
        ts.find(terms, 'bastards')
        ts.find(terms, 'benefitted')
        ts.find(terms, 'charged')
        ts.find(terms, 'charmless')
        count = ts.find(terms, 'chastises')                
        self.assertEqual(2, count)
        self.assertEqual("cheat giddy gloomy stress".split(), terms)
   
if __name__ == '__main__':
    unittest.main()
