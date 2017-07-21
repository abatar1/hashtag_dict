# coding=utf-8
import re
import HashtagInformation as him
import HashtagFormatter as hfm


class HashtagCounter(object):
    @property
    def tweets(self):
        return self.__tweets

    def __init__(self, tweets):
        self.__tweets = list(hfm.formattweets(tweets))

    def get_hashtags(self):
        hashtags = {}
        for tweet in self.__tweets:
            for word in tweet:
                if hfm.ishashtag(word):
                    if word in hashtags:
                        hashtags[word] += 1
                    else:
                        hashtags[word] = 1
        return hashtags

    def get_hashtags_inf(self):
        hashtags = {}
        for words in self.__tweets:
            curr_hashtags = [word for word in words if hfm.ishashtag(word)]
            not_hashtags = [word for word in words if not hfm.ishashtag(word)]
            for hashtag in curr_hashtags:
                if hashtag in hashtags:
                    hashtags[hashtag] = hashtags[hashtag].add(not_hashtags)
                else:
                    hashtags[hashtag] = him.HashtagInformation(1, not_hashtags)
        return hashtags
