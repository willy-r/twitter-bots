# twitter-bots

My first project working with [tweepy](https://www.tweepy.org/), and was very satisfying! Is very easy to use and the possibilities are huge. Now I understand why 15% of the Twitter users are bots. And I want to be part of this too!

---

## Installation

- You will need the credentials for authentication on API's Twitter, you can check [this](https://realpython.com/twitter-bot-python-tweepy/#creating-twitter-api-authentication-credentials) to know how to get the credentials.

- If you will only uses the bots locally, just ignore the files `Procfile` and `runtime.txt`, they are for deploy on Heroku only.

- But if you want to deploy on Heroku, [here](https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39) is a tutorial for this.

### Clone

- Clone this repo to your local machine using `https://github.com/willy-r/twitter-bots.git`

### Setup

- Go to `twitter-bots` directory:

```shell
$ cd twitter-bots
```

- I highly recommend you to setup a virtual environment first:

```shell
$ python3 -m venv env
```

- With your credentials, you need to configurate this enviroment variables:	

```shell
$ export ACCESS_TOKEN='your_access_token'
$ export ACCESS_TOKEN_SECRET='your_access_token_secret
'
$ export CONSUMER_KEY='your_consumer_key'
$ export CONSUMER_SECRET='your_consumer_secret'
```

- Now activate the virtual environment and install the dependencies:

```shell
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

---

## Usage

Go to `bots/` directory and use:

> change `bot_name.py` with the bot name you want. To stop the bot use `CTRL + C`.

```shell
(env) $ python3 bot_name.py
```

---

## Current Bots

To add more just follow the code on this bots:

Bot name | Description
---- | -----------
[`bots/fav\_mention.py`](bots/fav\_mentions.py) | Automatically favorites a tweet when mentioned.
[`bots/tweet\_pi\_time.py`](bots/tweet\_pi\_time.py) | Tweets the pi time of a day.

---

## Support

Reach out to me at one of the following places!

- Twitter at <a href="https://twitter.com/lliw_r?s=09" target="_blank">`@lliw_r`</a>

---
