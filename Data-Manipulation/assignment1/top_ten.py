import sys
import json

####################################################################################################
def tweet_dict(twitterData):
	twitter_list=[]
	for line in twitterData.readlines():
		twitter_list.append(json.loads(line))
		
	return twitter_list

#######################################################################################################

def top_ten_tags(tweetFile):
	tweets=filter(lambda t: 'delete' not in t.keys() and not len(t['entities']['hashtags']) is 0,tweet_dict(tweetFile))
	hash_scores={}
	
	for t in tweets:
		for h in t['entities']['hashtags']:
			key=h['text']
			hash_scores[key]=hash_scores[key] + 1.0 if key in hash_scores.keys() else 1.0
	sorted_scores=sorted(hash_scores.items(),key=lambda x:x[1])[:10]
	
	for k,v in sorted_scores:
		print "%s %s" %(k,v)		



############################################################################################################
def main():
	tweetFile= open(sys.argv[1])
	
	top_ten_tags(tweetFile)
	
if __name__=='__main__':
	main()
