# -*- coding: utf-8 -*-
def tweetIsRetweet(status):
    if status.retweeted:
        print('Retweet:', status.id)
    return status.retweeted


def tweetIsReply(status):
    isReply = status.in_reply_to_status_id is not None
    if isReply:
        print('Reply:', status.id)
    return isReply


def tweetIsQuote(status):
    if status.is_quote_status:
        print('Quote:', status.id)
    return status.is_quote_status


def tweetIsByMe(api, status):
    isByMe = status.user.id == api.me().id
    if isByMe:
        print('By me:', status.id)
    return isByMe


def ignoreTweet(api, status):
    return tweetIsRetweet(status) \
        or tweetIsReply(status) \
        or tweetIsQuote(status) \
        or tweetIsByMe(api, status)
