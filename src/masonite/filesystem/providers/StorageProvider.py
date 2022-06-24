from ...configuration import config
from ...providers import Provider
from ..drivers import AmazonS3Driver, LocalDriver
from ..Storage import Storage


class StorageProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        storage = Storage(self.application).set_configuration(
            config("filesystem.disks")
        )
        storage.add_driver("file", LocalDriver(self.application))
        storage.add_driver("s3", AmazonS3Driver(self.application))
        self.application.bind("storage", storage)

    def boot(self):
        pass
