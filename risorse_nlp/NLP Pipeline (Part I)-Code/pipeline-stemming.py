import nltk
from nltk.tokenize import word_tokenize
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
print ("Raw Text", raw)
print ("TOKENS:", tokens)
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
porstems=[porter.stem(t) for t in tokens]
lanstems=[lancaster.stem(t) for t in tokens]
print ("Porter stems:", porstems)
print ("Lancaster stems:", lanstems)

