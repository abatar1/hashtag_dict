import codecs


def readlines():
    f = codecs.open('in.txt', 'r', 'utf-8')
    return [_ for _ in f.read().splitlines()]
