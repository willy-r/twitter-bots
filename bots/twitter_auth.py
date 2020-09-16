"""Twitter authentication module."""

import os
import logging

import tweepy


LOGGER = logging.getLogger()

# Credentials to authenticate on API's Twitter.
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')


def create_api():
    """Connects to Twitter account and returns an api object."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as err:
        LOGGER.error('Error creating API', exc_info=True)
        raise err
    LOGGER.info('API successfully created!')
    return api
