import pytest
import time

import datetime as dt

import fetcher


@pytest.fixture(autouse=True)
def interrupt_on_sleep(monkeypatch) -> None:
    """Calling sleep will raise an Error in order to make `server_loop` not
    run forever.

    We could also implement `server_loop` differently, but for this project, I'd
    like to keep the non-test code straight forward. It's a trait off."""

    def _sleep(_duration) -> None:
        raise InterruptedError

    monkeypatch.setattr(time, "sleep", _sleep)


MOCK_NOW = dt.datetime(2022, 11, 5, 12, 00, 00)


@pytest.fixture(autouse=True)
def mock_datetime_now(monkeypatch) -> None:
    class MockDatetime:
        @staticmethod
        def now() -> dt.datetime:
            pass

    monkeypatch.setattr(dt, "datetime", MockDatetime)


def test_server_loop_calls_notifiers_with_unmodified_bookings(
    mock_account, mock_notifier, mock_config
) -> None:
    with pytest.raises(InterruptedError):
        fetcher.server_loop(mock_account, MOCK_NOW, [mock_notifier], mock_config)
        mock_account.fetch_bookings.assert_called_once()
        mock_notifier.notify.assert_called_once_with(
            mock_account.fetch_bookings(MOCK_NOW)
        )
        mock_config.check_interval.assert_called_once()
