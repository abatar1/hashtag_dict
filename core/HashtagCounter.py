import HashtagInformation as him
import OutputFormatter as ofm


class HashtagCounter(object):
    @property
    def tweets(self):
        return self.__tweets

    def __init__(self, tweets):
        self.__tweets = ofm.format_tweets(tweets)

    def get_hashtags(self):
        hashtags = {}
        for tweet in self.__tweets:
            for word in tweet.split():
                if self.ishashtag(word):
                    if word in hashtags:
                        hashtags[word] += 1
                    else:
                        hashtags[word] = 1
        return hashtags

    def get_hashtags_inf(self):
        hashtags = {}

        for word in self.__tweets:
            words = word.split()
            curr_hashtags = [word for word in words if self.ishashtag(word)]
            not_hashtags = [word for word in words if not self.ishashtag(word)]
            for hashtag in curr_hashtags:
                if hashtag in hashtags:
                    hashtags[hashtag] = hashtags[hashtag].add(not_hashtags)
                else:
                    hashtags[hashtag] = him.HashtagInformation(1, not_hashtags)
        return hashtags

    @staticmethod
    def ishashtag(word):
        return True if ('#' in word and len(word) > 1) else False
