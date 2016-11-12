import os
import random
import tweepy

import oauthDance
import predicates
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
        if predicates.ignoreTweet(api, result):
            continue
        print(result.text, result.source_url)
        print(dir(result.user), result.user.id)
        statusParams = {
            'status': random.choice(messages.sentences),
            'in_reply_to_status_id': result.id
        }
        if result.place:
            statusParams['place_id'] = result.place.id
        print('DEBUG', statusParams)
        # api.update_status(**statusParams)
        break
