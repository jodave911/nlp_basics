from nltk import *
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

text="Josh works for Twitter in California."
tokens=word_tokenize(text)

tagged=pos_tag(tokens)
entities=ne_chunk(tagged)

for entity in entities:
    if hasattr(entity,'label'):
        print(entity)


