import datetime as dt
from decimal import Decimal
from typing import Iterable
from unittest.mock import Mock

import pytest

from app.config import Config
from app.common_types import Account, Booking, Notifier


class MockAccount(Account):
    @staticmethod
    def _fetch_bookings(_newer_than: dt.datetime) -> Iterable[Booking]:
        return [
            Booking(
                direction="out",
                amount=Decimal("7.17"),
                transfer_entity="Paypal",
                date=dt.datetime(1991, 9, 9, 4, 31, 44),
            ),
            Booking(
                direction="in",
                amount=Decimal("1337"),
                transfer_entity="Work GmbH",
                date=dt.datetime(1998, 9, 9, 7, 22, 55),
            ),
            Booking(
                direction="out",
                amount=Decimal("1336"),
                transfer_entity="Landlord",
                date=dt.datetime(1666, 9, 2, 15, 11, 59),
            ),
        ]

    fetch_bookings = Mock(wraps=_fetch_bookings)


@pytest.fixture
def mock_account() -> Account:
    return MockAccount()


class MockNotifier(Notifier):
    @staticmethod
    def _notify(_bookings: Iterable[Booking]) -> None:
        pass

    notify = Mock(side_effect=_notify)


@pytest.fixture
def mock_notifier() -> Notifier:
    return MockNotifier()


class MockConfig(Config):
    @staticmethod
    def _get(name: str) -> object:
        return name

    get = Mock(wraps=_get)

    @staticmethod
    def _check_interval() -> float:
        return 1738576890543456

    check_interval = Mock(wraps=_check_interval)


@pytest.fixture
def mock_config() -> Config:
    return MockConfig({})
