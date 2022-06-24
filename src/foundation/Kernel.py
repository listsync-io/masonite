import os
from typing import TYPE_CHECKING

from cleo import Application as CommandApplication

if TYPE_CHECKING:
    from .Application import Application

from .. import __version__
from ..commands import CommandCapsule, DownCommand, KeyCommand, MakeProviderCommand, UpCommand
from ..environment import LoadEnvironment
from ..loader import Loader


class Kernel:
    def __init__(self, app: "Application"):
        self.application = app

    def register(self) -> None:
        """Register core Masonite features in the project."""
        self.load_environment()
        self.register_framework()
        self.register_commands()

    def load_environment(self) -> None:
        """Load environment variables into the application."""
        LoadEnvironment()

    def register_framework(self) -> None:
        self.application.use_storage_path(
            os.path.join(self.application.base_path, "storage")
        )
        self.application.bind("loader", Loader())

    def register_commands(self) -> None:
        self.application.bind(
            "commands",
            CommandCapsule(CommandApplication("Masonite", __version__)).add(
                KeyCommand(),
                MakeProviderCommand(self.application),
                DownCommand(),
                UpCommand(),
            ),
        )

