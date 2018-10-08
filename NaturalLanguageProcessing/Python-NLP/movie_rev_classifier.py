from nltk import FreqDist, NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.classify import accuracy
import random

documents = [(list(movie_reviews.words(fileid)),category)
	      for category in movie_reviews.categories()
	      for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

def document_features(document):
	document_words = set(document)
	features={}
	for word in word_features:
		features['contains({})'.format(word)] = (word in document_words)
	return features
featuresets = [(document_features(d),c) for (d,c) in documents]
train_set, test_set = featuresets[100:],featuresets[:100]
classifier = NaiveBayesClassifier.train(train_set)

print accuracy(classifier,test_set)


#accuracies
#run1 0.72
#run2 0.6
#run3 0.69
#run4 0.64
#run4 0.69

#The variation in accuracy is because of the document that is chosen as the root
#Every time the root document is chosen randomly. In naive bayes model each conditional probability depends on the root. Hence there is a difference. 
