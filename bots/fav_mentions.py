"""Fav mentions bot."""

import time
import logging
import functools

import schedule

from twitter_auth import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def with_logging(func):
    """Add generic logging to func."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        LOGGER.info('Retrieving mentions...')
        result = func(*args, **kwargs)
        LOGGER.info('Waiting...')
        return result
    return wrapper


@with_logging
def check_mentions(api):
    """Checks for new mentions and favorite this mentions."""
    mentions = api.mentions_timeline()
    for tweet in mentions:
        if not tweet.favorited:
            try:
                tweet.favorite()
                LOGGER.info(f'{tweet.id} from {tweet.user.name} favorited!')
            except Exception:
                LOGGER.error('Error on fav', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    # Check for mentions in every 1 minute.
    schedule.every().minute.do(check_mentions, api=api)
    while True:
        schedule.run_pending()
        time.sleep(1)
