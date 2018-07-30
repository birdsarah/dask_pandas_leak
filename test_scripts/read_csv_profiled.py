import time
from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import psutil
import gc

from pd_read_csv import read_csv
import pandas as pd

project_dir = Path('/home/bird/Dev/birdsarah/dask_pandas_leak')
test_data = os.path.join(project_dir, 'test_data', 'large_random.csv')


def main():
    process = psutil.Process()
    e = ThreadPoolExecutor(max_workers=8)
    print('before:', process.memory_info().rss // 1e6, 'MB')
    list(e.map(pd.read_csv, [test_data] * 8))
    time.sleep(2)
    gc.collect()
    print('after:', process.memory_info().rss // 1e6, 'MB')

if __name__ == '__main__':
    main()
