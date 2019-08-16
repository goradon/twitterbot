import random
import time
import tweepy
from config import CONFIG

CONSUMER_KEY = CONFIG["CONSUMER_KEY"]
CONSUMER_SECRET = CONFIG["CONSUMER_SECRET"]
ACCESS_TOKEN = CONFIG["ACCESS_TOKEN"]
ACCESS_SECRET = CONFIG["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
# ↑↑↑   インスタンス作成    ↑↑↑


'''
search_results = api.search(q="長期投資", count=10)

for result in search_results:
    tweet_id = result.id
    user_id = result.user._json['id']  
    try:
        api.create_favorite(tweet_id)
        api.retweet(tweet_id)          
        api.create_friendship(user_id) 
    except Exception as e:
        print(e)
        
'''



q_list = ["フォロバ","相互フォロー"]
count  = 50
#x = 0

for q in q_list:
    k = random.randint(5, 20)
    time.sleep(k)
    search_results = api.search(q=q, count=count)
    for result in search_results:
        #x = x + 1
        m = random.randint(5, 20)     #radom k
        #if x == 14:
        time.sleep(m)              #k秒停止
           #x = 0
        tweet_id = result.id            #元はstatusだった
        user_id  = result.user._json['id']
        try:
            #api.create_favorite(tweet_id)
            #api.retweet(tweet_id)
            api.create_friendship(user_id)
        except Exception as e:
            print(e)