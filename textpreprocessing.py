from nltk import *
from nltk.corpus import *

text = "This is a sample text for use in usage, cas What is your name?"
token=word_tokenize(text)
print(token)

lower_case = [token.lower() for token in token if token.isalpha()]
print(lower_case)

eng_words= set(words.words())
valid_case = [token for token in lower_case if token in eng_words]
print (valid_case)

stop_words= set(stopwords.words())
filtered_case = [token for token in valid_case if token not in stop_words]
print(filtered_case)

stemmer=PorterStemmer()
stemmer_case = [stemmer.stem(token) for token in filtered_case]
print(stemmer_case)

