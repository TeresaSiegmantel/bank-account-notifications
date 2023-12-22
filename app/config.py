from typing import Final, cast

import yaml


class Config:
    def __init__(self, values: dict[str, object]):
        # TODO: validation
        self._values = values

    def get(self, name: str) -> object:
        return self._values[name]

    def check_interval(self) -> float:
        # TODO: this should be configured as an interval, e.g. 1h30m
        return cast(float, self.get("check_interval"))

    def get_subconfig(self, section: str) -> "Config":
        return Config(cast(dict[str, object], self.get(section)))


DEFAULT_CONFIG_LOCATION: Final[str] = "~/.bank_account_notifications"


def load_config_from_default_location() -> Config:
    return Config(yaml.safe_load(DEFAULT_CONFIG_LOCATION))


CONFIG = load_config_from_default_location()
