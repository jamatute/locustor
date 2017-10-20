import unittest
from locustor.__init__ import main


class TestMainProgram(unittest.TestCase):
    def test_call_without_arguments_gives_help_message(self):
        main()
