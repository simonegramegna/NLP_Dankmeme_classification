import nltk
import re
print ("*** some examples of usage of the method re.search ***")
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
matchedtokens1 = [w for w in wordlist if re.search('ed$', w)]
matchedtokens2 = [w for w in wordlist if re.search('^..j..t..$', w)]
matchedtokens3 = [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
print (matchedtokens1)
print (matchedtokens2)
print (matchedtokens3)

