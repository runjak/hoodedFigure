def tweetIsRetweet(status):
    return status.retweet is not None


def tweetIsReply(status):
    return status.in_reply_to_status_id is not None


def tweetIsQuote(status):
    return status.is_quote_status


def tweetIsByMe(api, status):
    return status.user.id == api.me().id


def ignoreTweet(api, status):
    return tweetIsRetweet(status) \
        or IsReply(status) \
        or tweetIsQuote(status) \
        or tweetIsByMe(api, status)
