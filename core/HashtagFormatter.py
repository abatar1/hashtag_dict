# coding=utf-8
import re


def formatword(word):
    pstring = u'[^A-Za-z0-9А-Яа-я{0}]'.format('#' if ishashtag(word) else '')
    return re.sub(pstring, '', word).lower()

def formattweets(tweets):
    for tweet in tweets:
        result = []
        for colloc in tweet.split():
            for word in re.split(u'[.,:;?!]', colloc):
                fword = formatword(word)
                if fword: result.append(fword)
        yield result

def ishashtag(word):
    return True if word.startswith('#') and len(word) - 1 > 1 else False
