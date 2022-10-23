import tweepy
from datetime import datetime
import random
from demo import usernameList, api

print(len(usernameList))
# .env pending
# api_key = "eaLFxqln7SellQfGri9cccKla"
# api_key_secret = "3p0BmQMeoDtbfEqvrcKEvDhiACHYi865Z17y7aVprVssjqOBCE"
#
# access_token = "1578359033920032768-gKXvw97loCpJBz5lfz1lDKlcbUOJAK"
# access_token_secret = "9CJ8MiX4i4LlwRgwrDMKbBZlXVhANSHGJ35dAdB13R3L2"


# authentication
# auth = tweepy.OAuthHandler(api_key, api_key_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
# api.wait_on_rate_limit= True
# api.wait_on_rate_limit_notify= True

randomlist = random.sample(range(0, len(usernameList)), 5000)
totalavgsum= 0

userAvg = []
validUsers =0

for i in randomlist:
    userID= usernameList[i]
    tweets = api.user_timeline(screen_name=userID,
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts = False,)
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

    if len(ret) == 0:
        continue

    sum = 0

    for hashtweets in ret.items():
        c= hashtweets[1]
        repeated_hash= 0
        if len(c) > 0:
            a= hashtweets[1][0]
            b= hashtweets[1][-1]
            # print(a.created_at)
            diff = a.created_at - b.created_at
            if diff.total_seconds() > 0:
                repeated_hash+= 1
            # print(diff.total_seconds())
            sum += diff.total_seconds()
            # print(sum)

    if repeated_hash > 0:
        validUsers += 1
        avg = sum / repeated_hash
        totalavgsum += avg
        userAvg.append(avg)

avg = totalavgsum/validUsers
print(avg)
print(userAvg)
print(validUsers)




