 
### character sets ###

import nltk
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')

print ("*** unicode escape ***")
### UTF-8 encoding ###
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))
print ("\n")

### ITALIANO ###
print ("*** ITALIANO ASCII***")
f = open('c:/uniba/didattica/corpora/docUTF-8.txt')
for line in f:
    line = line.strip()
    print(line)
print ("\n")

print ("*** ITALIANO ASCII***")
f = open('c:/uniba/didattica/corpora/docUTF-8.txt',encoding='UTF-8')
for line in f:
    line = line.strip()
    print(line)
print ("\n")

