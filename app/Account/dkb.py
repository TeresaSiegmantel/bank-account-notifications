import datetime as dt
from typing import Iterable

from dkb_robo import DKBRobo

from app.common_types import Account, Booking, AccountNotFoundException
from app.config import CONFIG

dkb_config = CONFIG.get_subconfig("dkb")


class DkbAccount(Account):
    def fetch_bookings(self, newer_than: dt.datetime) -> Iterable[Booking]:
        username = dkb_config.get("usernmae")
        password = dkb_config.get("password")
        iban = dkb_config.get("iban")
        fetched_bookings = None
        with DKBRobo(dkb_user=username, dkb_password=password) as robo:
            accounts = robo.account_dic.values()
            target_account = None
            for account in accounts:
                if account["iban"] == iban:
                    target_account = account
            if target_account is None:
                raise AccountNotFoundException("dkb")

            transactions = robo.get_transactions(target_account['link'])
