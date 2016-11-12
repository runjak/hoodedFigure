import os
import tweepy

import oauthDance
import messages

auth = tweepy.OAuthHandler(
    os.getenv('CONSUMER_KEY'),
    os.getenv('CONSUMER_SECRET'))


access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

if not access_token or not access_token_secret:
    oauthDance.performOauthDance(auth)
else:
    auth.set_access_token(
        os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))

    api = tweepy.API(auth)

    results = api.search(q='#dogpark')

    for result in results:
        print(result.text)
