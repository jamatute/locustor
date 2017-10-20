import unittest
from locustor.cli_arguments import load_logger, load_parser
# from locustor.cli_arguments import load_logger, load_parser, load_config


class TestArgparse(unittest.TestCase):
    def setUp(self):
        self.parser = load_parser()

    def test_default_quiet_false(self):
        self.args = self.parser.parse_args(['run', 'https://github.com'])
        self.assertFalse(self.args.quiet)

    def test_default_verbose_false(self):
        self.args = self.parser.parse_args(['run', 'https://github.com'])
        self.assertFalse(self.args.verbose)

    def test_run_tescase_exists(self):
        self.args = self.parser.parse_args(['run', 'https://github.com'])
        self.assertEqual(self.args.subcommand, 'run')
        self.assertEqual(self.args.user_cases, ['10', '100', '1000'])

    def test_run_tescase_must_have_url(self):
        with self.assertRaises(SystemExit):
            self.args = self.parser.parse_args(['run'])

    def test_run_tescase_with_specific_usercase(self):
        self.args = self.parser.parse_args(['run', '-u', ['5', '25'],
                                            'https://github.com'])
        self.assertEqual(self.args.user_cases, ['5', '25'])

    # def test_compare_tescase_exists(self):
    #     self.args = self.parser.parse_args(['compare', 'https://github.com'])
    #     self.assertEqual(self.args.subcommand, 'compare')


# class TestLogger(TestArgparse):
#     def setUp(self):
#         self.args = self.parser.parse_args(['run', 'https://github.com'])
#         self.log = load_logger(self.args)
