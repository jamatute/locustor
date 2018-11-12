from locustor.locustor import Locustor

locustor = Locustor(host='http://pre-saigon-int.lowi.es:8080/bundle',
                    work_dir='../test_json',
                    num_clients=10,
                    hatch_rate=50,
                    run_time='5s')

locustor.run()
locustor.get_json()
locustor.get_result()
