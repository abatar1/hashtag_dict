# coding=utf-8
import operator
import re


def get_topsorted(input, ntop=10):
    return sorted(input.iteritems(), key=operator.itemgetter(1), reverse=True)[:ntop]

def format_tweets(tweets):
    return [re.sub(u'[^A-Za-z0-9А-Яа-я #]+', '', tweet).lower() for tweet in tweets]
