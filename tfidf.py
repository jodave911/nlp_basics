from nltk import *
from nltk.corpus import *
import math

def preproces(text):
    stemmer=PorterStemmer()
    stop_words=set(stopwords.words("english"))
    text=word_tokenize(text)
    return [stemmer.stem(word.lower()) for word in text if word.lower() not in stop_words]

def cal(document, corpus):
    corpus=[preproces(doc) for doc in corpus]
    document=preproces(document)
    tfidf={}
    print(document)
    for word in document:
        tf=document.count(word)/len(document)
        nowords_indocs= sum(1 for doc in corpus if word in doc)
        #print(nowords_indocs)
        idf= math.log10(len(corpus) / nowords_indocs)
        tfidf[word]=tf*idf
    return tfidf

corpus=["This is first sentences",
        "This is a second ",
        "This is the Third sentences",
        "Forth sentences"]
document="This is second sentences"
tfidf=cal(document, corpus)
print(tfidf)


