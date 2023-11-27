import time
from typing import Iterable

from config import Config, CONFIG
from types import Account, Notifier
import datetime as dt


def server_loop(account: Account, newer_than: dt.datetime, notifiers: Iterable[Notifier], config: Config = CONFIG) -> None:
    last_checked = newer_than

    while True:
        bookings = account.fetch_bookings(last_checked)
        last_checked = dt.datetime.now()

        for notifier in notifiers:
            notifier.notify(bookings)

        time.sleep(config.check_interval())
