from nltk import *

text = "This is for testing Apple Joshua, went quick"
tokens=word_tokenize(text)

validcase=[token for token in tokens if token.isalpha()]

pos=pos_tag(validcase)
for token, pos in pos:
    print(token, pos)