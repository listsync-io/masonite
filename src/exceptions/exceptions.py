class AmbiguousError(Exception):
    pass

class ContainerError(Exception):
    pass

class DumpException(Exception):
    pass

class InvalidConfigurationLocation(Exception):
    pass

class InvalidConfigurationSetup(Exception):
    pass

class LoaderNotFound(Exception):
    pass

class RequiredContainerBindingNotFound(Exception):
    pass

class MissingContainerBindingNotFound(Exception):
    pass

class StrictContainerException(Exception):
    pass

class DriverNotFound(Exception):
    pass

class ModelNotFound(Exception):
    pass

class HTTP404(Exception):
    pass

class ConnectionNotRegistered(Exception):
    pass

class QueryException(Exception):
    pass

class MigrationNotFound(Exception):
    pass

class ConfigurationNotFound(Exception):
    pass

class InvalidUrlConfiguration(Exception):
    pass

class MultipleRecordsFound(Exception):
    pass
