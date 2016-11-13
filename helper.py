# -*- coding: utf-8 -*-
import time
import tweepy


def printAndSleep(t, msg):
    print(msg)
    time.sleep(t)


def withRateLimit(func):
    while True:
        try:
            return func()
        except tweepy.RateLimitError:
            printAndSleep(15*60, 'Sleeping 15 minutes.')
