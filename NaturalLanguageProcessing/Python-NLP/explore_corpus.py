#!/usr/bin/python

from nltk.corpus import gutenberg
from nltk import FreqDist
list_of_words = gutenberg.words("austen-persuasion.txt")
fd = FreqDist(list_of_words)

print "Total number of tokens: "+ str(fd.N())#Total tokens: 98171
print "Number of unique tokens: "+ str(fd.B())#Unique Tokens: 6132

print "Top 10 tokens:"
for token,freq in fd.most_common(10):#to is the 3rd most occuring word in the list
	print token + "\t" + str(freq)

