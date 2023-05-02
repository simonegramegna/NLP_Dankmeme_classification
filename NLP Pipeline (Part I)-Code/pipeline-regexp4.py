import nltk
import re

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
first_att=hobbies_learned.findall(r"<\w*> <as> <\w*>")
print (first_att)
second_att=hobbies_learned.findall(r"<[A-Z].*> <as> <\w*>")
print (second_att)
