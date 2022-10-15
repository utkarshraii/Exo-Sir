import tweepy
import json

# import configparser
# import pandas as pd

# read configs
# config = configparser.ConfigParser()
# config.read('config.ini')

api_key = "eaLFxqln7SellQfGri9cccKla"
api_key_secret = "3p0BmQMeoDtbfEqvrcKEvDhiACHYi865Z17y7aVprVssjqOBCE"

access_token = "1578359033920032768-gKXvw97loCpJBz5lfz1lDKlcbUOJAK"
access_token_secret = "9CJ8MiX4i4LlwRgwrDMKbBZlXVhANSHGJ35dAdB13R3L2"

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

userID= "kamaalrkhan"

tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
# print()

# json_object = json.loads(tweets)
# print(json.dumps(json_object, indent= 1))
# print(json.dumps(json_object, indent = 3))

ret= {}

for tweet in tweets:
    # print(tweet.entities['hashtags'])
    for l in tweet.entities['hashtags']:
        word= l['text']
        if word in ret:
            ret[word] += [tweet]
        else:
            ret[word] = []
        # print(word)

print(ret['Arjun'])

# print(tweet.entities['hashtags'] for tweet in tweets)




# # user tweets
# user = 'veritasium'
# limit=10
#
# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=20, tweet_mode='extended').items(limit)
#
# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
#
# # create DataFrame
# # columns = ['User', 'Tweet']
# data = []
#
# for tweet in tweets:
#     data.append([tweet.user.screen_name, tweet.full_text])
#
# print(tweets)
#
# # df = pd.DataFrame(data, columns=columns)
#
# # print(df)


# # the ID of the status
# id = 1272771459249844224
#
# # fetching the status
# user = api.get_status(id)
#
# # fetching the created_at attribute
# created_at = status.created_at

# print("The status was created at : " + str(created_at))