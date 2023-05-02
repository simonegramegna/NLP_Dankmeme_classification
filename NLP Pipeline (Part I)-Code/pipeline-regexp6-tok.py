import nltk
import re
raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
... though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
... well without--Maybe it's always pepper that makes people hot-tempered,'..."""

### matching the words instead of the spaces.
tokens=re.findall(r'\w+|\S\w*', raw)
print ("tokens - findall:", tokens)

