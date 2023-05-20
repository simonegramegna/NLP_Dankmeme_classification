import nltk

def printfreq(fdist,vocabulary):
    print ("[", end=' ')
    for w in sorted(vocabulary):
        print(w + ':', fdist.freq(w), end=' ')
    print ("]", end=' ')

def printcount(fdist,vocabulary):
    print ("[", end=' ')
    for w in sorted(vocabulary):
        print(w + ':', fdist[w], end=' ')
    print ("]", end=' ')

def printdict(dictionary):
    for key in dictionary.keys():
        print ("\nKEY:", key, end=' ')
        print ("value:", dictionary[key])
    
#print the frequency distribution over a vocabulary


