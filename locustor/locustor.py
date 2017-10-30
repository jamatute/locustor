import os
import csv
import sys
import math
import time
import subprocess
from tabulate import tabulate


class Locustor():
    def __init__(self, url, locust_file='locustfile.py',
                 work_dir=os.path.expanduser('~/.local/share/locustor'),
                 user_cases=[10, 50, 70, 100, 500]):
        self.url = url
        self.locust_file = locust_file
        self.work_dir = work_dir
        self.user_cases = user_cases

    def run(self):
        for num_users in self.user_cases:
            cmd_str = 'locust --no-web -f {} -c {} -r {} -n {} ' + \
                             '--csv={}/{}.csv --host={}'
            cmd_str = cmd_str.format(self.locust_file, num_users,
                                     math.ceil(num_users/10), num_users*10,
                                     self.work_dir, num_users, self.url)
            rc = subprocess.call(cmd_str, stderr=open(os.devnull, 'wb'),
                                 shell=True)

            if rc != 0:
                print('Error running {} users in {}'.format(num_users,
                                                            self.url))
                sys.exit(1)
            time.sleep(30)


    def print_results(url, user_cases):
        print('# Test results for {}'.format(url))
        for num_users in user_cases:
            with open('{}.csv_requests.csv'.format(num_users), 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
                print('\n## Test case of {} users'.format(num_users))
                print(tabulate(data[1:], headers=data[0]))
