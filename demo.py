import tweepy
api_key = "eaLFxqln7SellQfGri9cccKla"
api_key_secret = "3p0BmQMeoDtbfEqvrcKEvDhiACHYi865Z17y7aVprVssjqOBCE"

access_token = "1578359033920032768-gKXvw97loCpJBz5lfz1lDKlcbUOJAK"
access_token_secret = "9CJ8MiX4i4LlwRgwrDMKbBZlXVhANSHGJ35dAdB13R3L2"
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.wait_on_rate_limit= True
api.wait_on_rate_limit_notify= True

india_woeid=23424848
trend_result=api.get_place_trends(india_woeid)
query = []
try:
    for trend in trend_result[0]["trends"]:
        query.append(trend["name"])
except:
    print("Errorrrrrrrrrrrr")


usernameList=[]

for q in query:
    tweets = tweepy.Cursor(api.search_tweets,
                           q, lang="en").items(200)
    list_tweets = [tweet for tweet in tweets]
    for tweet in list_tweets:
        usernameList.append(tweet.user.screen_name)



print(usernameList)
print(len(usernameList))