# -*- coding: utf-8 -*-
import tweepy


def performOauthDance(auth):
    print('Please visit:', auth.get_authorization_url())
    verifier = input('Verification token:')
    try:
        auth.get_access_token(verifier)
        print('Authentication data is:',
              'ACCESS_TOKEN=', auth.access_token,
              'ACCESS_TOKEN_SECRET=', auth.access_token_secret)
    except tweepy.TweepError:
        print('Failed to authenticate correctly.')
