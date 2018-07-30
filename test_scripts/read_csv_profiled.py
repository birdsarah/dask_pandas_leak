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
    print('before:', process.memory_info().rss // 1e6, 'MB')
    for i in range(8):
        pd.read_csv(test_data, engine='c')
    time.sleep(2)
    print('after:', process.memory_info().rss // 1e6, 'MB')

if __name__ == '__main__':
    main()
