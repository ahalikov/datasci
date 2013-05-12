import unittest
import term_sentiment as ts

class TestTermSentiment2(unittest.TestCase):

    def setUp(self):
        self.scores = ts.load_scores('AFINN-111.txt')
        self.temp_dir = '/home/artur/work/study/datasci/temp/'
       
    def test_score_file(self):        
        tf = open(self.temp_dir + 'output_full.txt') # tweet file
        res = ts.score_file(tf, self.scores)
        #print 'stress={0} friend={1}'.format(res['stress'], res['friend'])
        self.assertGreater(res['hello'][0], 0)
        self.assertGreater(res['friend'][0], 0)
        self.assertLess(res['stress'][0], res['friend'][0])
        self.assertLess(res['trying'][0], res['friend'][0])
        self.assertLess(res['homework'][0], res['believe'][0])        
        return
   
if __name__ == '__main__':
    unittest.main()
