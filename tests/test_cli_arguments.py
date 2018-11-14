import logging
import unittest
from locustor.cli_arguments import load_logger, load_parser


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


class TestLogger(TestArgparse):
    def setUp(self):
        self.parser = load_parser()
        self.args = self.parser.parse_args(['run', 'https://github.com'])
        self.log = load_logger(self.args)

    def test_logger_exist(self):
        self.assertEqual(str(type(self.log)), "<class 'logging.Logger'>")

    @unittest.skip("reason for skipping")
    def test_verbose(self):
        self.args = self.parser.parse_args(['run', 'https://github.com'])
        logger = load_logger(self.args)
        self.assertEqual(logger.getEffectiveLevel(), 30)

    @unittest.skip("reason for skipping")
    def test_verbose_info(self):
        self.args = self.parser.parse_args(['run', 'https://github.com', '-v=1', '-q=False'])
        logger = load_logger(self.args)
        self.assertEqual(logger.getEffectiveLevel(), 20)

    @unittest.skip("reason for skipping")
    def test_verbose_debug(self):
        self.args = self.parser.parse_args(['run', 'https://github.com', '-v=2', '-q=False'])
        logger = load_logger(self.args)
        self.assertEqual(logger.getEffectiveLevel(), 10)

    @unittest.skip("reason for skipping")
    def test_verbose_error(self):
        self.args = self.parser.parse_args(['run', 'https://github.com', 'True'])
        logger = load_logger(self.args)
        self.assertEqual(logger.getEffectiveLevel(), 40)
