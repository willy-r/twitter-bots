import os
import sys
import logging
import functools

import tweepy

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def add_logging(before: str = None, after: str = None):
    """Add generic logging with before and after messages to a func."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if before is not None:
                LOGGER.info(before)
            result = func(*args, **kwargs)
            if after is not None:
                LOGGER.info(after)
            return result
        return wrapper
    return decorator


def create_api() -> tweepy.API:
    """Connects to Twitter account and returns an API object."""
    # Credentials to authenticate on API's Twitter.
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception:
        LOGGER.error('Error creating API', exc_info=True)
        sys.exit()

    LOGGER.info('API successfully created!')
    return api
