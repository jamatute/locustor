from locustor.locustor import Locustor

locustor = Locustor(host='http://www.google.es',
                    work_dir='../test_json',
                    num_clients=10,
                    hatch_rate=50,
                    run_time='5s')

locustor.run()
locustor.get_json()
print('Result:{}'.format(locustor.get_result()))
