import decimal
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal, Iterable
import datetime as dt


@dataclass
class Booking:
    # we only need a few data points
    direction: Literal["in", "out"]
    amount: decimal.Decimal
    # TODO: there should be a better name for that
    transfer_entity: str
    date: dt.datetime


class Account(ABC):
    @abstractmethod
    def fetch_bookings(self, newer_than: dt.datetime) -> Iterable[Booking]:
        raise NotImplementedError


class Notifier(ABC):
    @abstractmethod
    def notify(self, bookings: Iterable[Booking]) -> None:
        raise NotImplementedError
