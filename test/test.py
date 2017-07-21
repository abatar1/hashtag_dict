# coding=utf-8
import unittest
from core import HashtagFormatter as f
from core import HashtagTop as t


class TestHashtagFormatter(unittest.TestCase):
    def test_formatword(self):
        self.assertEqual(f.formatword('#word'), '#word')
        self.assertEqual(f.formatword('%$ab@c'), 'abc')
        self.assertEqual(f.formatword('#'), '')

    def test_ishashtag(self):
        self.assertEqual(f.ishashtag('#hashtag'), True)
        self.assertEqual(f.ishashtag('hashtag'), False)
        self.assertEqual(f.ishashtag('#'), False)
        self.assertEqual(f.ishashtag('#a,pp'), True)

class TestHashtagTop(unittest.TestCase):
    def setUp(self):
        twits = [u"#hashtaga a b",
                 u"#Hashtaga a b c a,b a.c #hash,tag hello #,",
                 u"#Привет #привет привет",
                 u"#ПРИВЕТ"]
        self.topcounter = t.HashtagTop(twits)

    def test_get_hashtags(self):
        hashtags = [u"#привет", u"#hashtaga", u"#hash"]
        self.assertEqual(self.topcounter.gettop_hashtags(), hashtags)

    def test_get_hashtags_inf(self):
        words = [u"a", u"b", u"c", u"tag", u"hello"]
        self.assertEqual(self.topcounter.gettop_words()[u'#hashtaga'], words)

if __name__ == "__main__":
    unittest.main()
