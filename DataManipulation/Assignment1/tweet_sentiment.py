import sys
import json

'''
def hw():
	 print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))
	
'''
############################################################################	
def tweetParser(tweet_file):
	twitter_list=[]
	for line in tweet_file.readlines():
		parsed_line= json.loads(line)
		if parsed_line.has_key("text"):
			twitter_list.append(str(parsed_line["text"].encode("utf-8")))
	
	return twitter_list		
		

def Calculate(tweet,scores):
	for tw in tweet:
		score=0.0
		for word in tw.split(' '):
			if word  in scores.keys():
				score+=float(scores[word])
		
		print float(score)			 	

############################################################################

def main():
	sent_file = open(sys.argv[1])
    	tweet_file = open(sys.argv[2])
    	
    	#########################################################################
    	scores = {}                                                            # initialize an empty dictionary
	for line in sent_file:
  		term, score  = line.split("\t")                    # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = float(score)                        # Convert the score to an integer.

	# print scores.items()                                       # Print every (term, score) pair in the dictionary
	#tweetParse(tweet_file)
	Calculate(tweetParser(tweet_file),scores)
	
	#########################################################################
'''    	
    	hw()
    	lines(sent_file)
    	lines(tweet_file)
'''

if __name__ == '__main__':
	main()
