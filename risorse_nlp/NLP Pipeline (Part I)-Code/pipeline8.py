import nltk
from nltk.corpus import brown
wordsxsent=len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())
print ("Avg. words per sentence: ", wordsxsent)

text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = nltk.sent_tokenize(text)
print ((sents[79:89]))
       
