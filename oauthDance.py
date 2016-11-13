# -*- coding: utf-8 -*-
import tweepy


def performOauthDance(auth):
    print('Please visit:', auth.get_authorization_url())
    verifier = input('Verification token:')
    try:
        auth.get_access_token(verifier)
        print('\n'.join([
            'Authentication data is:',
            'ACCESS_TOKEN=%s' % auth.access_token,
            'ACCESS_TOKEN_SECRET=%s' % auth.access_token_secret]))
    except tweepy.TweepError:
        print('Failed to authenticate correctly.')
