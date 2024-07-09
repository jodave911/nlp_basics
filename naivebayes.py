from nltk import *
from nltk.corpus import *
from sklearn.model_selection import train_test_split

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalpha()]
    return dict(FreqDist(tokens))

pos_reviews = [(movie_reviews.raw(fileid), 'positive') for fileid in movie_reviews.fileids('pos')]
neg_reviews = [(movie_reviews.raw(fileid), 'negative') for fileid in movie_reviews.fileids('neg')]
tot_rev = pos_reviews + neg_reviews

processed_data = [(preprocess(text), category) for (text, category) in tot_rev]
train_data, val_data = train_test_split(processed_data, test_size=0.2, random_state=42)
classifier = NaiveBayesClassifier.train(train_data)
new_text = ["The movie was amazing", "the movie was terrible", "The movie was awful"]

for text in new_text:
    features = preprocess(text)
    predicted_category = classifier.classify(features)
    print("The predicted category for ", text,  "is ", predicted_category)