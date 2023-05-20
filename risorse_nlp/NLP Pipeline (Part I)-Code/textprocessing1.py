from nltk.corpus import PlaintextCorpusReader
corpus_root = 'c:/uniba/didattica/corpora/txt'
newcorpus = PlaintextCorpusReader(corpus_root, '.*')
print (newcorpus.raw())

### processing only one document ###

raw = open('c:/uniba/didattica/corpora/txt/doc1.txt').read()
print (raw)
   
