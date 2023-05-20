import nltk
import re
raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
... though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
... well without--Maybe it's always pepper that makes people hot-tempered,'..."""
tokens=raw.split()
print ("tokens - simple split:", tokens)
### same result with a regex
### splitting on any whitespace
tokens=re.split(r'\s+',raw)
print ("tokens - simple split with regex:", tokens)
### with \W+ we match all characters other than letters, digits or underscore.
### We can use \W in a simple regular expression to split the input on anything other than a word character
tokens=re.split(r'\W+', raw)
print ("tokens - \W+ split:", tokens)



