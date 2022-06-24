class ExceptionHandler:
    def __init__(self, application, driver_config=None):
        self.application = application
        self.drivers = {}
        self.driver_config = driver_config or {}
        self.options = {}

    def set_options(self, options):
        self.options = options
        return self

    def add_driver(self, name, driver):
        self.drivers.update({name: driver})

    def set_configuration(self, config):
        self.driver_config = config
        return self

    def get_driver(self, name=None):
        if name is None:
            return self.drivers[self.driver_config.get("default")]
        return self.drivers[name]

    def get_config_options(self, driver=None):
        if driver is None:
            return self.driver_config[self.driver_config.get("default")]

        return self.driver_config.get(driver, {})

    def handle(self, exception):
        self.application.make("event").fire(
            f"masonite.exception.{exception.__class__.__name__}", exception
        )

        # add headers to response if any
        if hasattr(exception, "get_headers"):
            headers = exception.get_headers()
            response.with_headers(headers)

        # if an exception handler is registered for this exception, use it instead
        # add headers to response if any
        if hasattr(exception, "get_headers"):
            headers = exception.get_headers()
            response.with_headers(headers)

        if self.application.has(f"{exception.__class__.__name__}Handler"):
            return self.application.make(
                f"{exception.__class__.__name__}Handler"
            ).handle(exception)

        raise exception

        # handle exception in production
        # if not self.application.is_debug():
        #     pass
