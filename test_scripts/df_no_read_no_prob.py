import pandas as pd
import numpy as np
import time
import psutil
from concurrent.futures import ThreadPoolExecutor


def main():
    process = psutil.Process()
    e = ThreadPoolExecutor(1)

    def f(_):
        return pd.DataFrame(np.random.random((1000000, 50)))

    print('before:', process.memory_info().rss // 1e6, 'MB')
    list(e.map(f, range(1)))
    print('after:', process.memory_info().rss // 1e6, 'MB')


if __name__ == '__main__':
    main()
