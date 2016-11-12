import os
import tweepy

import oauthDance

auth = tweepy.OAuthHandler(
    os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))


access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

if not access_token or not access_token_secret:
    oauthDance.performOauthDance(auth)
else:
    auth.set_access_token(
        os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

    print('AUTH URL:', auth.get_authorization_url())

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
