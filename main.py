import operator
import codecs
from core import HashtagCounter as hcm


def readlines():
    f = codecs.open('in.txt', 'r', 'utf-8')
    return [_ for _ in f.read().splitlines()]

def get_topsorted(input, ntop=10):
    return sorted(input.iteritems(), key=operator.itemgetter(1), reverse=True)[:ntop]

def main():
    tweets = readlines()
    hcounter = hcm.HashtagCounter(tweets)

    hashtags = hcounter.get_hashtags()
    for k, v in get_topsorted(hashtags):
        print('%s' % k),

    print('')
    hashtags_with_words = hcounter.get_hashtags_inf()
    for k, v in get_topsorted(hashtags_with_words):
        print('%s:[%s]' % (k, ', '.join([w[0] for w in get_topsorted(v.words)])))


if __name__ == '__main__':
    main()