import os
import errno
import shutil
import tempfile
import unittest
import pytest
import testinfra
from locustor.locustor import Locustor

test_url = 'https://www.google.com'
test_locustfile = 'tests/test_data/locustfile.py'
test_user_case = [1]


class TestLocustor(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(dir='tests/test_data')
        self.locustor = Locustor(test_url,
                                 locust_file=test_locustfile,
                                 work_dir=self.tmp_dir,
                                 user_cases=test_user_case)

    def tearDown(self):
        try:
            shutil.rmtree(self.tmp_dir)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

    def test_locustor_has_url(self):
        self.assertEqual(self.locustor.url, test_url)

    def test_locustor_has_default_locustfile(self):
        self.locustor = Locustor(test_url)
        self.assertEqual(self.locustor.locust_file, 'locustfile.py')

    def test_locustor_can_set_locustfile(self):
        self.assertEqual(self.locustor.locust_file, test_locustfile)

    def test_locustor_has_default_work_directory(self):
        self.locustor = Locustor(test_url)
        self.assertEqual(self.locustor.work_dir, os.path.expanduser(
            '~/.local/share/locustor'))

    def test_locustor_can_set_work_dir(self):
        self.assertEqual(self.locustor.work_dir, self.tmp_dir)

    def test_locustor_has_default_user_cases(self):
        self.locustor = Locustor(test_url)
        self.assertEqual(self.locustor.user_cases, [10, 50, 70, 100, 500])

    def test_locustor_can_set_user_case(self):
        self.assertEqual(self.locustor.user_cases, test_user_case)

    @pytest.mark.skip(reason="Too long to test")
    def test_locustor_run_method(self):
        self.host = testinfra.get_host("local://localhost")
        self.locustor.run()
        file = self.host.file(
            os.path.join(self.tmp_dir, '1.csv_distribution.csv'))
        self.assertTrue(file.exists)
        self.assertTrue(file.contains(
            '"Name","# requests","50%","66%","75%","80%","90%'))

        file = self.host.file(
            os.path.join(self.tmp_dir, '1.csv_requests.csv'))
        self.assertTrue(file.exists)
        self.assertTrue(file.contains(
            '"Method","Name","# requests","# failures","Medi'))

class TestLocustorLoad(TestLocustor):
    def setUp(self):

    def test_load_data_default_to_new(self):
        self.locustor.work_dir = 'tests/test_data'
        self.load()
        self.assertEqual(self.data['new']['1']['distribution'](1)(1), 10)
        self.assertEqual(self.data['new']['1']['summary'](1)(2), 10)

    def test_load_data_in_old_register(self):
        self.locustor.work_dir = 'tests/test_data'
        self.load('old')
        self.assertEqual(self.data['old']['1']['distribution'](1)(1), 10)
        self.assertEqual(self.data['old']['1']['summary'](1)(2), 10)

    def test_load_data_from_different_directory(self):
        self.locustor.work_dir = 'tests/test_data'
        self.load('old', load_dir='tests/tests_data/test_case_2')
        self.assertEqual(self.data['new']['1']['distribution'](1)(1), 20)
        self.assertEqual(self.data['new']['1']['summary'](1)(2), 20)
