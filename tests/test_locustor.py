import unittest
from taskban.reports import KanbanReport, Report


class TestReport(unittest.TestCase):
    def setUp(self):
        self.report = Report('1d')
