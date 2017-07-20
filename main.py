from core import HashtagCounter as hcm
from core import OutputFormatter as formatter
from core import FileHelper as fhelper

tweets = fhelper.readlines()
hcounter = hcm.HashtagCounter(tweets)
hashtags = hcounter.get_hashtags()

for k, _ in formatter.get_topsorted(hashtags):
    print('%s' % k)

hashtags_with_words = hcounter.get_hashtags_inf()
for k, v in formatter.get_topsorted(hashtags_with_words):
    print('%s : %s' % (k, ', '.join([w[0] for w in formatter.get_topsorted(v.words)])))
