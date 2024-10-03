# test_main.py
# This file tests the sentiment analysis function using various text inputs.

import unittest
from main import analyze_sentiment


class TestSentimentAnalysis(unittest.TestCase):

    def test_positive_sentiment(self):
        self.assertGreater(analyze_sentiment("I love this product!"), 0)

    def test_negative_sentiment(self):
        self.assertLess(analyze_sentiment("I hate this service."), 0)

    def test_neutral_sentiment(self):
        self.assertEqual(analyze_sentiment("It's a book."), 0)


if __name__ == "__main__":
    unittest.main()
