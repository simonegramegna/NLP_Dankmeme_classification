  
### character sets ###
import nltk
print ("*** encoding=latin2*** ")
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line)
print ("\n") 

print ("*** problems with non-ASCII chars without option encoding=latin2")

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
f = open(path)
for line in f:
    line = line.strip()
    print(line)
print ("\n")

