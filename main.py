import os
import time
import tweepy

import helper
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

    def performMain(memo=dict()):
        lastTweetId = memo['lastTweetId'] if 'lastTweetId' in memo else None
        print('Searching results after', lastTweetId)
        results = search.findDogPark(api, lastTweetId)

        def mkHandleTweet(status):

            def handleTweet():
                replyData = messages.replyDictFromTweet(status)
                if replyData is not None:
                    reply = api.update_status(**replyData)
                    memo['lastTweetId'] = reply.id
                    helper.printAndSleep(
                        30, 'Sent message with id %s. Sleeping 30s.' %
                        memo['lastTweetId'])
            return handleTweet

        for status in results:
            print('Considering result', status.id)
            if predicates.ignoreTweet(api, status):
                continue
            helper.withRateLimit(mkHandleTweet(status))

    while True:
        helper.withRateLimit(performMain)
        helper.printAndSleep(60, 'Sleeping a minute between searches.')
