"""Tweet pi time bot."""

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
        result = func(*args, **kwargs)
        LOGGER.info('Waiting until pi time again...')
        return result
    return wrapper


@with_logging
def tweet_pi_time(api):
    """Tweet the pi time."""
    try:
        api.update_status('It’s pi time!')
    except Exception:
        LOGGER.error('Error on updating status', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    # Tweet every day at 03:14 (pi time!).
    schedule.every().day.at('03:14').do(tweet_pi_time, api=api)
    while True:
        schedule.run_pending()
        time.sleep(1)
