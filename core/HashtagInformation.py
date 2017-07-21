from collections import Counter


class HashtagInformation(object):
    @property
    def words(self):
        return dict(self.__words)

    @property
    def occurrence(self):
        return self.__occurrence

    def __init__(self, occurrence, words):
        self.__occurrence = occurrence
        self.__words = Counter(words)

    def __lt__(self, other):
        return self.__occurrence < other.__occurrence

    def add(self, newwords):
        words_upd = dict(self.__words)
        for word in newwords:
            if word in self.__words:
                words_upd[word] += 1
            else:
                words_upd[word] = 1
        return HashtagInformation(self.__occurrence + 1, words_upd)
