from pathlib import Path
import os
import numpy as np
import pandas as pd

project_dir = Path('/home/bird/Dev/birdsarah/dask_pandas_leak')
outfile = os.path.join(project_dir, 'test_data', 'large_random.csv')

pd.DataFrame(np.random.random((100000, 50))).to_csv(outfile)
