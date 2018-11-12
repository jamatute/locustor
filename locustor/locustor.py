import datetime
import json
import os
import sys
import subprocess
import time


class Locustor:
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
                 locust_file=os.path.dirname(os.path.abspath(__file__)) + '/generic_locustfile.py',
                 work_dir=os.path.expanduser('~/.local/share/locustor'),
                 num_clients=10,
                 hatch_rate=10,
                 run_time='60s'):

        self.host = host
        self.locust_file = locust_file
        self.work_dir = work_dir
        self.num_clients = num_clients
        self.run_time = run_time
        self.hatch_rate = hatch_rate
        self.inform_name = 'inform_name-{}'.format(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
        self.fail_ratio = 1.0

    def _check_csv_file(self):
        if not os.path.exists(self.work_dir):
            os.makedirs(self.work_dir)

    def run(self):
        cmd_str = 'locust ' \
                  '--no-web ' \
                  '-f {locust_file} ' \
                  '-c {num_clients} ' \
                  '-r {hatch_rate} ' \
                  '-t {run_time} ' \
                  '--json={work_dir}/{inform_name} ' \
                  '--csv={work_dir}/{inform_name} ' \
                  '--host={host}'.format(locust_file=self.locust_file,
                                         num_clients=self.num_clients,
                                         hatch_rate=self.hatch_rate,
                                         run_time=self.run_time,
                                         work_dir=self.work_dir,
                                         inform_name=self.inform_name,
                                         host=self.host)

        self._check_csv_file()

        print('Sentence: {}'.format(cmd_str))

        rc = subprocess.call(cmd_str,
                             stderr=subprocess.STDOUT,
                             shell=True)
        if rc != 0:
            print('Error running in {}'.format(self.host))
            sys.exit(1)
        time.sleep(30)

    def get_json(self):
        file = open('{work_dir}/{inform_name}_result.json'.format(work_dir=self.work_dir, inform_name=self.inform_name),
                    'r')
        inform = json.loads(file.read())
        return inform

    def get_result(self):
        inform = self.get_json()
        return inform.get('fail_ratio') < self.fail_ratio or False
