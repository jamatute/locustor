
custor

## Description

Tool to execute locust and produce reports.

Wrapper to use over *locust*. You can create your Locustor model and use his own method to execute over integration deployment easily.

## Installation

You can use `pip`

```bash
pip install https://github.com/jamatute/locustor
```

Or clone the repository and install it

```bash
git clone https://github.com/jamatute/locustor
cd locustor
pip install -r requirements.txt
python3 setup.py install
```

## Usage

You can run `locustor` with two modes: `run` and `compare`.

### Run

When executed with `run`, `locustor` will execute the tests, output the
results as csv and json files in your directory selected.

## Configuration

**Locustor** *(host, locust_file,  work_dir, num_clients,  hatch_rate, run_time)*

host= Host to test
locust_file= Locust file location
work_dir= Directory where to leave the result
num_clients=Num client tests(int)
hatch_rate=Hatch rate test(int)
run_time = Test execution time ej:'60s'


## Example

    locustor = Locustor(host=args.host, 
									locust_file=os.path.dirname(os.path.abspath(__file__)) + '/locustfile.py',
                        			work_dir='performance_result',
                        			num_clients=10,
                        			hatch_rate=50,
                        			run_time='60s')
    
    locustor.run()




