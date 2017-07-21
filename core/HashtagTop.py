import operator
import HashtagCounter as c

class HashtagTop(object):
    def __init__(self, tweets):
        self.__counter = c.HashtagCounter(tweets)

    def __get_topsorted__(self, input, ntop):
        return sorted(input.iteritems(), key=operator.itemgetter(1), reverse=True)[:ntop]

    def gettop_hashtags(self, ntop=10):
        hashtags = self.__counter.get_hashtags()
        return [item[0] for item in self.__get_topsorted__(hashtags, ntop)]

    def gettop_words(self, ntop=10):
        hashtags = self.__counter.get_hashtags_inf()
        return {key: [word[0] for word in self.__get_topsorted__(value.words, ntop)]
                for key, value
                in self.__get_topsorted__(hashtags, ntop)}
