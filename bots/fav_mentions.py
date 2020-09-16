"""Fav mentions bot."""

import time
import logging

from twitter_auth import create_api


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def check_mentions(api):
    """Checks for new mentions and favorite this mentions."""
    LOGGER.info('Retrieving mentions...')

    mentions = api.mentions_timeline(count=5)
    for tweet in mentions:
        if not tweet.favorited:
            try:
                tweet.favorite()
                LOGGER.info(f'{tweet.id} from {tweet.user.name} favorited!')
            except Exception:
                LOGGER.error('Error on fav', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    while True:
        check_mentions(api)
        LOGGER.info('Waiting...')
        # Check for mentions in every 1 minute.
        time.sleep(60)
