from ..cache import Cache
from ..cache.drivers import FileDriver, MemcacheDriver, RedisDriver
from ..configuration import config
from .Provider import Provider


class CacheProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        cache = Cache(self.application).set_configuration(config("cache.stores"))
        cache.add_driver("file", FileDriver(self.application))
        cache.add_driver("redis", RedisDriver(self.application))
        cache.add_driver("memcache", MemcacheDriver(self.application))
        self.application.bind("cache", cache)

    def boot(self):
        pass
