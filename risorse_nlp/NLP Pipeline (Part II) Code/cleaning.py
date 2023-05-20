import nltk
import re
import string
from nltk.tokenize import sent_tokenize, word_tokenize



# split the input on anything other than a word character
def onlywords(text):
    cleaned_tokens = re.split(r'\W+', text)
    return cleaned_tokens

# split on whitespace and then remove punct
def wordsnopunct(text):
    tokens=text.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    return stripped

def wordmatch(text):
    cleaned_tokens = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", text)
    return cleaned_tokens

def NLTKTokenize(text):
    nltk_words = word_tokenize(text)
    return nltk_words

def NLTKregtokenize(text):
    pattern = r'''(?x)     # set flag to allow verbose regexps
    (?:[A-Z]\.)+       # abbreviations, e.g. U.S.A.
   | \w+(?:-\w+)*       # words with optional internal hyphens
   | \$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
   | \.\.\.             # ellipsis
   | [][.,;"'?():-_`]   # these are separate tokens; includes ], [
 '''
    tokens=nltk.regexp_tokenize(text, pattern)
    return tokens

def onlypunct(text):
    waste=re.findall(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]+", text)
    return waste
    
