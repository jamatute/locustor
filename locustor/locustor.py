import csv
import sys
import math
import time
import subprocess
from tabulate import tabulate

url = 'http://www.fake-activate.com'
user_cases = [10, 50, 70, 100, 500]

class Locustor():

    def run_test(url, user_cases):
        for num_users in user_cases:
            rc = subprocess.call(
                'locust --no-web -c {} -r {} -n {} --csv={}.csv --host={}'.format(
                    num_users, math.ceil(num_users/10), num_users*10,
                    num_users, url), shell=True)
            if rc != 0:
                print('Error running {} users in {}'.format(num_users, url))
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
