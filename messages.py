# -*- coding: utf-8 -*-
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
    "so others may also survive @%s!",
    "Hi @%s! City council discourages the term #dogpark for security reasons.",
    "You are not a dog, @%s! Please don't think of the #dogpark.",
    "@%s in the #dogpark all dogs have 8 legs. Scary.",
    "Please return to safety @%s! Don't linger in the #dogpark.",
    "Hey @%s… I got notice that the #dogpark "
    "will get fortified with spikes and lava soon.",
    "Beware @%s. Today the #dogpark is full of deer. "
    "Dangerous with their sharp claws and many heads.",
    "There is a time and place for everything @%s. "
    "But it's not the #dogpark. An acid pit is much saver.",
]


def replyDictFromTweet(status):
        msg = random.choice(sentences) % status.user.screen_name
        if len(msg) > 140:
            print('Cannot send message:', msg)
            return None
        statusParams = {
            'status': msg,
            'in_reply_to_status_id': status.id
        }
        if status.place:
            statusParams['place_id'] = status.place.id
        return statusParams
