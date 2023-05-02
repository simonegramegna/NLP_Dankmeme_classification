# load text
# we take the gutemberg corpus
import cleaning
import nltk
import re
import string
from nltk import sent_tokenize
from nltk.corpus import inaugural


# load text
text=inaugural.raw("2009-obama.txt")

# splitting text into tokens & cleaning#
# cleaning =  removing all undesirable content (e.g. puntcuation)
# here you need to use your strategy for tokenization & cleaning

print ("PUNCTUATION: ", string.punctuation)

#1: only words with regex
cleaned_tokens1=cleaning.onlywords(text)
print ("STRATEGY 1 split the input on anything other than a word character:", sorted(cleaned_tokens1))
print ("# tokens: ", len(cleaned_tokens1))

#2: split on whitespace + remove punct

cleaned_tokens2=cleaning.wordsnopunct(text)
print ("STRATEGY 2 # split on whitespace and then remove punct:", sorted(cleaned_tokens2))
print ("# tokens: ", len(cleaned_tokens2))

diff1 = [t for t in cleaned_tokens1 if t not in cleaned_tokens2]
print ("tokens in 1 but not in 2: ", sorted(diff1))
diff2 = [t for t in cleaned_tokens2 if t not in cleaned_tokens1]
print ("tokens in 2 but not in 1", sorted(diff2))

#3 matching a specific regex

cleaned_tokens3=cleaning.wordmatch(text)
print ("matching specific regex:", sorted(cleaned_tokens3))
print ("# tokens: ", len(cleaned_tokens3))
diff31 = [t for t in cleaned_tokens3 if t not in cleaned_tokens1]
print ("tokens in 3 but not in 1: ", sorted(diff31))
diff13 = [t for t in cleaned_tokens1 if t not in cleaned_tokens3]
print ("tokens in 1 but not in 3", sorted(diff13))

#4: NLTK tokenizer
tokens4=cleaning.NLTKTokenize(text)
print ("NLTK Tokenizer:", sorted(tokens4))
print ("# tokens: ", len(tokens4))
diff42 = [t for t in tokens4 if t not in cleaned_tokens2]
print ("tokens in 4 but not in 2", sorted(diff42))

#5: NLTK tokenizer
tokens5=cleaning.NLTKregtokenize(text)
print ("NLTK regex Tokenizer:", sorted(tokens5))
print ("# tokens: ", len(tokens5))
diff54 = [t for t in tokens5 if t not in tokens4]
print ("tokens in 5 but not in 4", sorted(diff54))

