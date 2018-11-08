import os

from locustor.locustor import Locustor

locustor = Locustor(host='http://pre-saigon-int.lowi.es:8080/bundle',
                    locust_file='../locustlowi/locustfile.py',
                    work_dir=os.path.expanduser('csv'),
                    num_clients=10,
                    hatch_rate=50,
                    run_time='60s')

locustor.run()