import sys
import json


def lines(fp):
    return str(len(fp.readlines()))

###########################################################################################################
def tweetParse(tweet_file):
    tweets = []
    
    for tweet in tweet_file.readlines():
        line= json.loads(tweet)
        if line.has_key("text"):
            tweets.append(str(line["text"].encode("utf-8")).replace('\n',''))

    return tweets
           
             
            
def Calculate_frequency(tweet):
    terms = {}
    i = 0
    for t in tweet:
        for w in t.split(' '):            
            if w not in terms.keys():
                terms[w] = float(1)
            elif w.encode('utf-8', "ignore")in terms.keys(): 
                terms[w] = float(terms[w] + 1)
            i = i + 1

    for term in terms:
        terms[term] = (float(terms[term])/i)  
        print "%s %.3f"%(term,terms[term])

########################################################################################################
    
def main():
    tweet_file = open(sys.argv[1])


    #tweetParse(tweet_file)
    Calculate_frequency(tweetParse(tweet_file))
    
    
if __name__ == '__main__':
    main()
