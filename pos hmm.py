from nltk import *
from nltk.corpus import *

tagged_sen = brown.tagged_sents(categories='news')
train_size = int(len(tagged_sen)*.9)
train_sen=tagged_sen[:train_size]
hmm_tagger = HiddenMarkovModelTagger.train(train_sen)

sen = "Today is is a beautiful day"
token = word_tokenize(sen)
tagged = hmm_tagger.tag(token)
for i in tagged:
    print(i)