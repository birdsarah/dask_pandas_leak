from concurrent.futures import ThreadPoolExecutor
import os
from pathlib import Path
import psutil
import pandas as pd


project_dir = Path(os.path.abspath(__file__)).parents[1]
test_data = os.path.join(project_dir, 'test_data', 'large_random.csv')

# prep
process = psutil.Process()

# example with read_csv, this leaks memory
print('before:', process.memory_info().rss // 1e6, 'MB')
with ThreadPoolExecutor() as e:
    future = e.submit(pd.read_csv, test_data)
print('after:', process.memory_info().rss // 1e6, 'MB')
