import time

from .Provider import Provider


class FrameworkProvider(Provider):
    def __init__(self, application):
        self.application = application

    def boot(self):
        self.application.bind("start_time", time.time())
