#   -------------------------------------------------------------
#   Nasqueron Reports :: Reports
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Underlying types to represent a report
#   License:        BSD-2-Clause
#   -------------------------------------------------------------


class RawReport:
    """The report fetched from the datasource"""
    def __init__(self, headers=None, rows=None):
        self.headers = headers
        self.rows = rows


class Report:
    """The report with access to raw report and formatted version"""
    def __init__(self, raw=None, formatted=None):
        if raw is None:
            self.raw = RawReport()
        else:
            self.raw = raw

        self.formatted = formatted
