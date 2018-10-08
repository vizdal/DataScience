from nltk import FreqDist
from nltk.corpus import treebank
from nltk import chunk, tag
treebank_words = []
data = treebank.tagged_sents()
treebank_words = sum(data,[])
#for lis_data in data:
#	for (word, tag) in lis_data:
#		treebank_words.append()
#print (treebank_words)
chunkd_data=chunk.ne_chunk(treebank_words)
ne_list = chunkd_data.subtrees(filter=lambda t: t.label() in
["ORGANIZATION", "PERSON",
"LOCATION","DATE","TIME",
"MONEY","PERCENT",
"FACILITY","GPE"])
chunkd_trees = [tree for tree in ne_list]
word_fd = FreqDist([' '.join(word for word,pos in tree.leaves()) for tree in chunkd_trees]) 
print word_fd
print "Three most common named entities are: "
#print word_fd.most_common(3);
print ",".join(word for word,pos in word_fd.most_common(3))




