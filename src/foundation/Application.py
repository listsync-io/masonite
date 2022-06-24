from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING, Callable, Iterator, List, Tuple, Type

from ..container import Container
from ..environment import env
from ..facades import Config

if TYPE_CHECKING:
    from ..providers import Provider

ResponseHandler = Callable[[str, List[Tuple]], None]


class Application(Container):
    def __init__(self, base_path: str = None):
        self.base_path: str = base_path
        self.storage_path: str = None
        self.providers: list = []

    def register_providers(self, *providers: Type["Provider"]) -> "Application":
        for provider_class in providers:
            provider = provider_class(self)
            provider.register()
        return self

    def use_storage_path(self, path: str) -> None:
        self.storage_path = path

    def get_storage_path(self) -> str:
        return self.storage_path

    def add_providers(self, *providers: Type["Provider"]) -> "Application":
        for provider_class in providers:
            provider = provider_class(self)
            provider.register()
            self.providers.append(provider)

        return self

    def get_providers(self) -> List["Provider"]:
        return self.providers

    def is_debug(self) -> bool:
        """Check if debug mode is enabled."""
        # @removed:5.0.0
        if Config.has("application.debug"):
            return bool(Config.get("application.debug"))
        else:
            return env("APP_DEBUG", True)

    def is_dev(self) -> bool:
        """Check if app is running in development mode."""
        return not self.is_running_tests() and os.getenv("APP_ENV") in [
            "development",
            "local",
        ]

    def is_production(self) -> bool:
        """Check if app is running in production mode."""
        return os.getenv("APP_ENV") == "production"

    def is_running_tests(self) -> bool:
        """Check if app is running tests."""

        return "pytest" in sys.modules

    def is_running_in_console(self) -> bool:
        """Check if application is running in console. This is useful to only run some providers
        logic when used in console. We can differenciate if the application is being served or
        if an application command is ran in console."""
        if len(sys.argv) > 1:
            return sys.argv[1] != "serve"
        return True

    def environment(self) -> str:
        """Helper to get current environment."""
        if self.is_running_tests():
            return "testing"
        else:
            return os.getenv("APP_ENV")
