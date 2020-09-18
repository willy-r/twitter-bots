"""Tweet pi time bot."""

import time
import logging
from datetime import datetime, timedelta

from twitter_auth import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def tweet_pi_time(api):
    """Tweets pi time."""
    try:
        api.update_status('It’s pi time!')
    except Exception:
        LOGGER.error('Error on updating status', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    while True:
        now = datetime.now()
        pi_time = now.replace(hour=3, minute=14, second=0, microsecond=0)
        if now >= pi_time:
            pi_time += timedelta(days=1)
        # Sleep at 3:14 of the day (pi time!).
        time.sleep((pi_time - now).total_seconds())

        tweet_pi_time(api)
        LOGGER.info('Waiting until pi time again...')
