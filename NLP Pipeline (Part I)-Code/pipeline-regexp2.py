import nltk
import re
word = 'supercalifragilisticexpialidocious'
vowels=re.findall(r'[aeiou]', word)
print(vowels)
print(len(vowels))

### only matched word
from nltk.corpus import gutenberg
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print (moby.findall(r"<a> (<.*>) <man>"))

# three-word phrases ending with the word bro
from nltk.corpus import nps_chat
chat = nltk.Text(nps_chat.words())
seq2=chat.findall(r"<.*> <.*> <bro>")
print (seq2)
### sequences of three or more words starting with the letter l [3]
seq3=chat.findall(r"<l.*>{3,}")
print (seq3)


