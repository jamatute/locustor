import os

from locustor.locustor import Locustor

locustor = Locustor(host='http://example:8080/example',
                    work_dir=os.path.expanduser('csv'),
                    num_clients=10,
                    hatch_rate=50,
                    run_time='10s')

locustor.run()