"""
#
#
#
# - mac os local
# - Python 3.5.0
# *******************************************************************
# *You always should remove someone who is not following you.       *
# *The human always should be in love with each other NOT one-sided *
# *******************************************************************
#
#
"""
import time
import tweepy
import sys



"""
#
#
#自分の環境に合わせてください
#Your environment
#
#
"""
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 


"""
#
#
#自分をフォローしているユーザーを取得する
#Someone who is follow me
#
#
"""
index = 0
follower_list = []
for follower in tweepy.Cursor(api.followers).items():
    print( follower.screen_name )
    follower_list.append( follower.screen_name )
    #time.sleep(5)

    if index == 205:
        break

    index += 1

"""
#
#
#自分がフォローしているユーザーを取得する
#Someone who is I am follow them 
#
#
"""
index = 0
friends_list = []
for friends in tweepy.Cursor(api.friends).items():
    print( friends.screen_name )
    friends_list.append( friends.screen_name )
    #time.sleep(5)

    if index == 100:
        break

    index += 1

"""
#
#
#
#自分はフォローしてるのに、あっちは自分をフォローしてないユーザーを取得
#Get list someone who is not following me even though I following
#
"""
def intersect_list(lst1, lst2):

    lst1 = lst1.copy()
    for element in lst2:
        #time.sleep(5)
        try:
            lst1.remove(element)
        except ValueError:
            continue
        else:
            print(element)
            print("love each other")
    return lst1


"""
#
#
#
#自分をフォローしてないユーザー削除
#remove someone who is not following me
#
"""
#print( intersect_list(friends_list, follower_list) )
not_following_me_list = intersect_list(friends_list, follower_list)

for you_unfollowing in not_following_me_list:
    time.sleep(10)
    api.destroy_friendship(you_unfollowing)