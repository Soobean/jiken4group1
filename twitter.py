import tweepy
import os
import sys

consumer_key = "###########################"
consumer_secret = "################################################"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

access_token = "##############################################"
access_token_secret = "###########################################"

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

if(api.verify_credentials):
    print('We successfully logged in')
sys.stdout = open('ouput.txt','w')
keyword ="min_faves:1000 lang:ja"
search = []



#wfile = open(os.getcwd()+"/twitter.txt",mode='w')
#data = {}
#i = 0
#for tweet in search:
#    data['text'] = tweet.text
#    wfile.write(data['text'] + '\n')
#    i += 1



cursor = tweepy.Cursor(api.search,q = keyword,count=100,include_entities=True,)
#for status in cursor() .items(1000):
#    process_status(status)
for i,tweet in enumerate(cursor.items()):
    #print(tweet.favorite_count)
    #print(tweet.retweet_count)
    print("|")
    print("{}: {}".format(i,tweet.text))

#wfile.close()
