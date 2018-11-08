import datetime
import os
import csv
import sys
import math
import time
import subprocess
from tabulate import tabulate


class Locustor():
    """
        host: Host to load test in the following format: http://10.21.32.33

        locust_file: Python module file to import, e.g. '../other.py'.  Default: generic_locustfile

        num_clients: Number of concurrent Locust users. Only used together with --no-web

        hatch_rate: The rate per second in which clients are spawned. Only used together with --no-web

        run_time: Stop after the specified amount of time, e.g. (300s, 20m, 3h, 1h30m, etc.).

        work_dir: Destination to csv file

        inform_name: File name of csv inform

    """
    def __init__(self,
                 host,
                 locust_file='locustfile.py',
                 work_dir=os.path.expanduser('~/.local/share/locustor'),
                 num_clients=10,
                 hatch_rate=10,
                 run_time='60s',
                 inform_name='locust-inform'):

        self.host = host
        self.locust_file = locust_file
        self.work_dir = work_dir
        self.num_clients = num_clients
        self.run_time = run_time
        self.hatch_rate = hatch_rate
        self.inform_name = '+'.join(inform_name, datetime.datetime.now)

    def run(self):
        cmd_str = 'locust ' \
                  '--no-web ' \
                  '-f {locust_file} ' \
                  '-c {num_clients}' \
                  '-r {hatch_rate} ' \
                  '-t {run_time} ' + \
                  '--csv={work_dir}/{inform_name}.csv ' \
                  '--host={host}'.format(locust_file=self.locust_file,
                                 num_clients = self.num_clients,
                                 hatch_rate = self.hatch_rate,
                                 run_time = self.run_time,
                                 work_dir = self.work_dir,
                                 inform_name = self.inform_name,
                                 host=self.host)

        rc = subprocess.call(cmd_str, stderr=open(os.devnull, 'wb'),
                             shell=True)
        if rc != 0:
            print('Error running in {}'.format(self.host))
            sys.exit(1)
        time.sleep(30)

    def load(self, load_name='new', load_dir=None):
        if load_dir is None:
            load_dir = self.work_dir

        csv_files = [f for f in os.listdir(self.work_dir)
                     if os.path.isfile(os.path.join(self.work_dir, f)) and
                     os.path.splitext(f)[-1] == '.csv']

        for csv_file in csv_files:
            if 'distribution' in csv_file:
                csv_file_type = 'distribution'
            elif 'requests' in csv_file:
                csv_file_type = 'summary'

            # use_case =

            # with open(csv_file, 'r') as f:
            #     self.data = csv.reader(f)
            #     data = list(reader)
            #     print('\n## Test case of {} users'.format(num_users))
            #     print(tabulate(data[1:], headers=data[0]))

    def show(self):
        print('# Test results for {}'.format(self.url))
        for num_users in self.user_cases:
            with open('{}.csv_requests.csv'.format(num_users), 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
                print('\n## Test case of {} users'.format(num_users))
                print(tabulate(data[1:], headers=data[0]))
