import builtins

from ..configuration import config
from ..dumps import Dumper
from ..exceptions import DumpExceptionHandler
from ..exceptions.ExceptionHandler import ExceptionHandler
from .Provider import Provider


class ExceptionProvider(Provider):
    def __init__(self, application):
        self.application = application
        
    def register(self):
        exception_handler = ExceptionHandler(self.application)
        self.application.bind("exception_handler", exception_handler)

        # dumper
        dumper = Dumper(self.application)
        self.application.bind("dumper", dumper)
        builtins.dd = dumper.dd
        builtins.dump = dumper.dump
        builtins.clear_dumps = dumper.clear
        self.application.bind(
            "DumpExceptionHandler", DumpExceptionHandler(self.application)
        )

    def boot(self):
        pass
