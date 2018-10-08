#import the toolkit and tags
from nltk.corpus import treebank
#import HMM module 
from nltk.tag import hmm

# Traindata - pretagged
train_data = treebank.tagged_sents()[0:3001]
# Test data - pretagged 
test_data = treebank.tagged_sents()[3001:]

print train_data[0]

# Setup a trainer with default(None) values
# And train with the data
trainer = hmm.HiddenMarkovModelTrainer()
tagger = trainer.train_supervised(train_data)

print tagger
# Prints the basic data about the tagger

print tagger.tag("Today is a good day.".split())
# day is classifies as NNP ( proper noun ) but it is a common noun.
print tagger.tag("Joe met Joanne in New Delhi.".split())

print tagger.tag("Chicago is the birthplace of Marry".split())
#preposition 'of' (IN) is tagged as proper noun(NNP)
print tagger.evaluate(test_data)
