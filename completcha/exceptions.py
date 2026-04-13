class SolverApiError(Exception):
    pass


class MissingApiKey(Exception):
    pass


class ProgrammerError(Exception):
    pass


class ServerError(Exception):
    pass


class MaxRetriesServerExceeded(Exception):
    pass


class DeprecatedLibrary(Exception):
    pass
