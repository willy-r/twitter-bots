import time

import schedule

from config import create_api, add_logging, LOGGER


@add_logging(
    before='Retrieving mentions...',
    after='Waiting for new mentions...',
)
def check_mentions(api) -> None:
    """Checks for new mentions and favorite this mentions."""
    # Retrieve the last 20 mentions.
    mentions = api.mentions_timeline()
    for tweet in mentions:
        if not tweet.favorited:
            try:
                tweet.favorite()
                LOGGER.info(f'Tweet from {tweet.user.name} favorited!')
            except Exception:
                LOGGER.error('Error on fav', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    # Check for mentions in every 1 minute.
    schedule.every().minute.do(check_mentions, api=api)
    while True:
        schedule.run_pending()
        time.sleep(1)
