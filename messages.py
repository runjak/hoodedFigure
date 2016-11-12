import random


sentences = [
    "Going into the #dogpark is not allowed, @%s.",
    "That's my favourite #dogpark @%s -  no one is allowed to go into it!",
    "That #dogpark you mention is forbidden! Please don't, @%s",
    "The #dogpark should be secured with electrified barbwire. "
    "Don't you agree, @%s?",
    "Just make sure NOT TO ENTER the #dogpark @%s.",
    "Why would you mention such nasty things like a #dogpark @%s?",
    "Remember to share your #dogpark experience "
    "so others may also survive @%s!"
]


def replyDictFromTweet(status):
        msg = random.choice(sentences) % status.user.screen_name
        if len(msg) > 140:
            return None
        statusParams = {
            'status': msg,
            'in_reply_to_status_id': status.id
        }
        if status.place:
            statusParams['place_id'] = status.place.id
        return statusParams
