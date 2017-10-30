import os
import errno
import shutil
import tempfile
import unittest
from locustor.locustor import Locustor

test_url = 'https://www.google.com'
test_locustfile = 'tests/test_data/locustfile.py'
test_user_case = [1]


class TestLocustor(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp('tests/test_data')
        self.locustor = Locustor(test_url,
                                 locust_file=test_locustfile,
                                 work_dir=self.tmp_dir,
                                 user_cases=test_user_case)

    def tearDown(self):
        try:
            #shutil.rmtree(self.tmp_dir)
            pass
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

    def test_locustor_run_method(self):
        self.locustor.run()
