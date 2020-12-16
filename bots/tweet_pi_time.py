import time

import schedule

from config import create_api, add_logging, LOGGER


@add_logging(before='Waiting until next run...')
def tweet_pi_time(api):
    """Tweet the pi time."""
    try:
        api.update_status('It’s pi time!')
    except Exception:
        LOGGER.error('Error on updating status', exc_info=True)


if __name__ == '__main__':
    api = create_api()
    schedule.every().wednesday.at('03:14').do(tweet_pi_time, api=api)
    while True:
        schedule.run_pending()
        time.sleep(1)
