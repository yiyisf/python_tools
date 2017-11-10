import twitter

api = twitter.Api(consumer_key='***',
                  consumer_secret='***',
                  access_token_key='***',
                  access_token_secret='***')

# print(api.VerifyCredentials()) #用户信息

# users = api.GetFriends() #获取关注用户
# print([u.name for u in users])

user = "@yiyi119120"
try:
    statuses = api.GetUserTimeline(screen_name=user, count=30, include_rts=False)
    for s in statuses:
        print(s.text)
except twitter.TwitterError as e:
    print("error: {0}".format(e.message[0]['message']))
