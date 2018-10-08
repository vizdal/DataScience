from nltk.tbl.demo import postag

postag(num_sents=None, train=0.7665)
# It is observed that HMM gave 36.84% accuracy on test dataset.
# Where as the brill tagger provides 92.53% on the test dataset.
# So in this case brill provides more accuracy.
# In Case of CRF Tagger it was observed that the accuracy was 0.947582213387(94.75%) which is higher that brill tagger. So CRF gives the best result.

# Top 3 Rules

# NN->VB if Pos:-NONE-@[-2] & Pos:TO@[-1]
# VBP->VB if Pos:MD@[-3,-2,-1]
# POS->VBZ if Pos:PRP@[-2,-1]

#Time Taken By Brill Tagger : 55.41 seconds

