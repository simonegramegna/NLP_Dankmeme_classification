import nltk
import re

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
patterns=hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")
print (patterns)


