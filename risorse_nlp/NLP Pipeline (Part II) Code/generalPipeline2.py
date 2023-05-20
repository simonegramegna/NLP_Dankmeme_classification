import cleaning
import nltk
import re
import string
from nltk import sent_tokenize
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# load text
text=inaugural.raw("2009-obama.txt")
print ("Punctuation: ",string.punctuation)
# splitting text into tokens & cleaning#
# cleaning =  removing all undesirable content (e.g. puntcuation)
# here you need to use your strategy for tokenization & cleaning

#tokens=cleaning.wordsnopunct(text)
tokens=cleaning.wordmatch(text)
print ("# tokens: ", len(tokens))
print ("tokens: ", sorted(tokens))

# a little bit of cleaning --> remove specific tokens
waste = cleaning.onlypunct(text)
cleaned_tokens = [t for t in tokens if not t in waste]
print ("# cleaned tokens: ", len(cleaned_tokens))
print ("CLEANED tokens: ", sorted(cleaned_tokens))

# filter out stopwords

stop_words = stopwords.words('english')
nostop_tokens = [t for t in cleaned_tokens if not t in stop_words]

# normalization

words = [word.lower() for word in nostop_tokens]

# stemming / lemmatization
# we apply stemming

porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]

print ("# final stemmed tokens: ", len(stemmed))
print ("FINAL STEMMED tokens: ", sorted(stemmed))

print ("# vocabulary: ", len(set(stemmed)))
print ("Vocabulary: ", sorted(set(stemmed)))
