import unittest
import assignment1.tweet_sentiment as ts

__author__ = 'Artur Khalikov'

class TestTweetSentiment(unittest.TestCase):

    def setUp(self):
        self.scores = ts.load_scores('AFINN-111.txt')

    def test_score_tweet(self):
        score = ts.score_tweet("", self.scores)
        self.assertEqual(0, score)
        
        score = ts.score_tweet("theres a guy in this resturaunt who looks like ed im in heaven theres chicken wings and a beautiful ginger man", self.scores)
        self.assertEqual(7, score)
        
        score = ts.score_tweet("My knee hurts so bad and it itches but I can't get to the itchy spot due the the wrap! Ugh #Struggles", self.scores)
        self.assertEqual(-7, score)
        
        score = ts.score_tweet("abandon abandon abandon", self.scores)
        self.assertEqual(-6, score)
        
        score = ts.score_tweet("@BT_toner wish I could! Samford problems, two weeks left.", self.scores)
        self.assertEqual(-1, score)
    
if __name__ == '__main__':
    unittest.main()
