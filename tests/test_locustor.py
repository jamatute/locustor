import io
import os
import errno
import shutil
import tempfile
import unittest
import pytest
import testinfra
from mock import patch

from locustor.locustor import Locustor

test_url = 'https://www.google.com'
test_locustfile = os.path.dirname(os.path.abspath(__file__))+'/test_data/locustfile.py'
test_user_case = [1]


class TestLocustor(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.NamedTemporaryFile().name
        self.locustor = Locustor(test_url,
                                 locust_file=test_locustfile,
                                 work_dir=self.tmp_dir)

    def tearDown(self):
        try:
            shutil.rmtree(self.tmp_dir)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

    def test_locustor_has_url(self):
        self.assertEqual(self.locustor.host, test_url)

    def test_locustor_has_default_locustfile(self):
        self.locustor = Locustor(test_url)
        self.assertIn('locustor/locustor/generic_locustfile.py', self.locustor.locust_file)

    def test_locustor_can_set_locustfile(self):
        self.assertEqual(self.locustor.locust_file, test_locustfile)

    def test_locustor_has_default_work_directory(self):
        self.locustor = Locustor(test_url)
        self.assertEqual(self.locustor.work_dir, os.path.expanduser(
            '~/.local/share/locustor'))

    def test_locustor_can_set_work_dir(self):
        self.assertEqual(self.locustor.work_dir, self.tmp_dir)

    def test_locustor_run_method_ok(self):
        self.locustor.inform_name = 'test'
        self.locustor.run_time = '1s'
        self.locustor.run()
        self.assertTrue(os.path.exists('{}/test_distribution.csv'.format(self.locustor.work_dir)))
        self.assertTrue(os.path.exists('{}/test_requests.csv'.format(self.locustor.work_dir)))
        self.assertTrue(os.path.exists('{}/test_result.json'.format(self.locustor.work_dir)))

    def test_locustor_run_method_ko(self):
        self.locustor.locust_file = None
        with self.assertRaises(SystemExit) as cm:
            self.locustor.run()

        self.assertEqual(cm.exception.code, 1)

    @patch('locustor.locustor.Locustor.get_json')
    def test_locustor_get_result(self, mock_get_json):
        self.locustor.fail_ratio = 1.0
        mock_get_json.return_value = {"fail_ratio": 0.0}
        self.assertTrue(self.locustor.get_result())
        mock_get_json.return_value = {"fail_ratio": 10.0}
        self.assertFalse(self.locustor.get_result())

    def test_locustor_get_json(self):
        self.locustor.work_dir = 'test_data/test_case_3'
        self.locustor.inform_name = 'inform_name-test_ok'
        json = self.locustor.get_json()
        self.assertIsInstance(json, dict)
        self.assertTrue(json)
