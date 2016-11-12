import os
import time
import tweepy

import oauthDance
import messages
import predicates
import search


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

    lastTweetId = None
    while True:
        try:
            results = search.findDogPark(api, lastTweetId)
            for status in results:
                if predicates.ignoreTweet(api, status):
                    continue
                replyData = messages.replyDictFromTweet(status)
                if replyData is not None:
                    reply = api.update_status(**replyData)
                    lastTweetId = reply.id
                    print('Sent message with id %s. Sleeping 30s.' %
                          lastTweetId)
                    time.sleep(30)
            print('Sleeping a minute after search finished.')
            time.sleep(60)
        except tweepy.RateLimitError:
            print('Sleeping 15 minutes.')
            time.sleep(15 * 60)
