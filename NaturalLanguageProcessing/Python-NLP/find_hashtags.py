import csv, nltk
import collections

unique_words = collections.defaultdict(set)
hash_tags =  collections.defaultdict(set)
#Method to iterate the input and store hashtags and unique words
def get_words_as_set(tweet_string,handle):
	tweet_words = nltk.tokenize.word_tokenize(tweet_string)
	count = 0
	for word in tweet_words:
		unique_words[handle].add(word)
		if(word == '#'):
			hash_tags[handle].add("#"+tweet_words[count+1])
		count = count+1
# Method to print the output in given format				
def print_output():
	for key in unique_words.keys():
		print(key+":")
		value_set = unique_words[key]
		print("* unique tokens: "+", ".join(value_set))
		if key in hash_tags:
			print("* hashtags: "+", ".join(hash_tags[key])+"\n")
		else:
			print("* hashtags: "+"\n")
with open ('tweets.csv', 'rb') as infile:
    reader = csv.reader(infile,quotechar='"')
    line_count = 0
    for row in reader:
		if(line_count>0):	#Ignoring header since it exists
			get_words_as_set(row[3],row[1])
		line_count += 1
    print_output()
