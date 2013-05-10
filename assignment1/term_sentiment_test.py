import unittest
import term_sentiment as ts

class TestTermSentiment(unittest.TestCase):

    def setUp(self):
        self.scores = ts.load_scores('AFINN-111.txt')

    def test_score_tweet(self):
        score = ts.score_tweet("", self.scores)
        self.assertEqual(0, score[0])
        
        score = ts.score_tweet("theres a guy in this resturaunt who looks like ed im in heaven theres chicken wings and a beautiful ginger man", self.scores)
        self.assertEqual(7, score[0])
        
        score = ts.score_tweet("My knee hurts so bad and it itches but I can't get to the itchy spot due the the wrap! Ugh #Struggles", self.scores)
        self.assertEqual(-7, score[0])
        
        score = ts.score_tweet("abandon abandon abandon", self.scores)
        self.assertEqual(-6, score[0])
        
        score = ts.score_tweet("@BT_toner wish I could! Samford problems, two weeks left.", self.scores)
        self.assertEqual(1, score[0])
        
        score = ts.score_tweet("@JonasBrothers New POM POMS single is available NOW on iTunes: http://smarturl.it/jbtw FREE APP: iTunes: http://bit.ly/N5t6uR  and Android: http://bit.ly/TJRJfz", self.scores)
        print score
        #self.assertEqual(-1, score[0])
    
if __name__ == '__main__':
    unittest.main()
