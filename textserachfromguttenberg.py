import nltk
nltk.download('gutenberg')
from nltk.corpus import gutenberg
from nltk.text import Text

corpus=gutenberg.words("melville-moby_dick.txt")
text=Text(corpus)
text.concordance("monstrous")

