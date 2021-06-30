import pandas as pd
import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


# Read train and test files
data = pd.read_csv(Path("./data/dataset.csv"), index_col=0)
print(data.describe())
print(data.columns)

# sns.pairplot(train_df);