from concurrent.futures import ThreadPoolExecutor
import os
import time
from pathlib import Path
import psutil
import pandas as pd


project_dir = Path(os.path.abspath(__file__)).parents[1]
test_data = os.path.join(project_dir, 'test_data', 'large_random.csv')

# prep
process = psutil.Process()
e = ThreadPoolExecutor(8)

# example with read_csv, this leaks memory
print('before:', process.memory_info().rss // 1e6, 'MB')
list(e.map(pd.read_csv, [test_data] * 8))
time.sleep(1)
print('after:', process.memory_info().rss // 1e6, 'MB')
