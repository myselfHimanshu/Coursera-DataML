import sys
import json

sentimentData= sys.argv[1]
twitterData= sys.argv[2]

################################################################################################################
def tweet_dict(twitterData):
	twitter_list=[]
	twitterFile=open(twitterData)
	for line in twitterFile.readlines():
		twitter_list.append(json.loads(line))
		
	return twitter_list	
	
def sentiment_dict(sentimentData):
	scores={}
	afinnFile=open(sentimentData)
	for line in afinnFile:
 		term, score  = line.split("\t")  
  		scores[term] = float(score)  
  	
  	return scores	

######################################################################################################################
def main():
	tweets         = tweet_dict(twitterData)
	sentiments = sentiment_dict(sentimentData)
	
	state_dict=dict()
	
	for i in range(len(tweets)):
		if all(k in tweets[i].keys() for k in ('text','place')):
			if not (tweets[i]['place']==None):
				tweet_word=tweets[i]['text'].split()
				tweet_state=tweets[i]['place']['country_code']
				sent_score=0
				
				for word in tweet_word:
					if word.encode('utf-8') in sentiments.keys():
						sent_score+=float(sentiments[word])
					else:
						sent_score=sent_score
				
				if tweet_state.encode('utf-8') in state_dict.keys():
					state_dict[tweet_state].append(sent_score)
				else:
					state_dict[tweet_state]=[]
					state_dict[tweet_state].append(sent_score)
	
	state_list=[]
	max_score=0
	happiest_state=""
	for state in state_dict.keys():
		state_score=0
		state_list=state_dict[state]
		for score in state_list:
			state_score+=float(score)
		
		state_score=state_score/len(state)
		
		if happiest_state == "" or state_score>max_score:
			max_score=state_score
			happiest_state = state
			
	
	print happiest_state		
	
	
if __name__ == '__main__':
	main()	
		
									
				
	
	
	
	
	
	
