# -*- coding: utf-8 -*-
def getLastTweetId(api):
    timeline = api.home_timeline()
    return max([tweet.id for tweet in timeline])


def findDogPark(api, lastTweetId=None):
    if lastTweetId is None:
        lastTweetId = getLastTweetId(api)

    return api.search(q='#dogpark', since_id=lastTweetId)
