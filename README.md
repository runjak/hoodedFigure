hoodedfigure
=====

This is a small toy project for a Twitter bot
that uses the [tweepy](https://tweepy.readthedocs.io) library
to interact with twitter.

I'm a fan of [welcome to nightvale](http://www.welcometonightvale.com/),
where there is a dogpark that is only used by hooded figures.
The hooded figures do not want people mentioning the dogpark - or thinking of it.
They especially do not want dogs in the dogpark.

This bot aids this strive for dogpark related content by reminding
other twitter users that they should be careful around the subject.
To do so it mentions them with a random selection from a set of predefined [messages](https://github.com/runjak/hoodedfigure/blob/master/messages.py#L4).

Local setup
-----

If you want to get a local copy of this bot working
feel free to follow these steps:
1. Install `REQUIREMENTS` via `pip` so that your python setup
   has the required libraries.
2. Use [apps.twitter.com](https://apps.twitter.com) to create a new app.
3. Use a command like
   ```bash
   env CONSUMER_KEY=… \
       CONSUMER_SECRET=… \
       python3.5 main.py
   ```
   to start the bot while passing the CONSUMER_KEY and CONSUMER_SECRET
   of your app to it so that it can help you with the Oauth dance for a user.
   * If `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET` are not provided the bot
   will print a URL to `stdout`.
   * Visit this URL with a browser logged in as the user you want to authenticate.
   * Take the resulting code to the bot and enter it via `stdin`.
   * The bot will print the `ACCESS_TOKEN` and `ACCESS_TOKEN_SECRET` values to use.
4. After having an authenticated user, use a command like:
   ```bash
   env CONSUMER_KEY=… \
       CONSUMER_SECRET=… \
       ACCESS_TOKEN=… \
       ACCESS_TOKEN_SECRET=… \
       python3.5 main.py
   ```
   to start the bot so that it performs its intended task.

Docker setup
-----

The bot is also available as a docker container named [runjak/hoodedfigure](https://hub.docker.com/r/runjak/hoodedfigure).
This image is an automatic build where `runjak/hoodedfigure:latest`
follows the `master` branch.
You can use the image with a command like this:
```
docker run \
    -e CONSUMER_KEY=… \
    -e CONSUMER_SECRET=… \
    -e ACCESS_TOKEN=… \
    -e ACCESS_TOKEN_SECRET=… \
    -it runjak/hoodedfigure:latest
```
