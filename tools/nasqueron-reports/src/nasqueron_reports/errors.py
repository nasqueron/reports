#   -------------------------------------------------------------
#   Nasqueron Reports :: Errors
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Errors raised by reports
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


class NasqueronReportError(Exception):
    """Base exception for all report-related errors."""

    pass


class NasqueronReportConfigError(NasqueronReportError):
    pass


class NasqueronReportDatabaseError(NasqueronReportError):
    pass


class NasqueronReportQueryError(NasqueronReportError):
    """Raised when an SQL query file does not match the expected patterns."""

    def __init__(self, message=None, query=None):
        super(NasqueronReportQueryError, self).__init__(message)
        self.query = query
