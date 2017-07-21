import codecs
from core import HashtagTop as ht


def readlines():
    f = codecs.open('in.txt', 'r', 'utf-8')
    return [_ for _ in f.read().splitlines()]

def main():
    tweets = readlines()
    htop = ht.HashtagTop(tweets)

    print( htop.gettop_hashtags())
    print(htop.gettop_words())


if __name__ == '__main__':
    main()