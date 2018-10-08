# Import the toolkit and tags
from nltk.corpus import treebank
# Import CRF module
from nltk.tag import crf

# Train data - pretagged
train_data = treebank.tagged_sents()[0:3001]
#Train data - pretagged
test_data = treebank.tagged_sents()[3001:]

# Setup a trainer with default(None) values
# Train with the data

tagger = crf.CRFTagger();
tagger.train(train_data,'model.crf.tagger')

print tagger
#prints the basic data about the tagger

print tagger.evaluate(test_data)
#Evaluation result : 0.947582213387
#HMM Tagger Result : 0.368443772933
#It can be noticied that CRF Tagger gives a much better result when compared to HMM Tagger
