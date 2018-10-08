#!/usr/bin/python
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords #imported auxiliary corpus provided with NLTK

data = "All work and no play makes jack a dull boy. All work and no play makes jack a dull boy."

stopWords = set(stopwords.words('english')); #set of english startwords
words = word_tokenize(data.lower())
wordsFiltered = []

for w in words:
	if w not in stopWords:
		wordsFiltered.append(w)

print len(stopWords)
print stopWords
print wordsFiltered

