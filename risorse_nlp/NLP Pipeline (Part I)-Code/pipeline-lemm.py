import nltk
from nltk.tokenize import word_tokenize
raw = """DENNIS: Listen, strange women lying in ponds distributing swords
is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)

wnl = nltk.WordNetLemmatizer()
wnlemmas=[wnl.lemmatize(t) for t in tokens]
print ("WordNet Lemmas:", wnlemmas)
print ("Lemmatizing 'arguing' with WN lemmatizer:")
print(wnl.lemmatize("arguing", pos=u'a'))
print(wnl.lemmatize("arguing", pos=u'v'))
print ("Lemmatizing 'lying' with WN lemmatizer:")
print(wnl.lemmatize("lying", pos=u'v'))
