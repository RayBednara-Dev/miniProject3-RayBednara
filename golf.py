# INF601 - Advanced Programming in Python
# Ray Bednara
# Mini Project 3

import kagglehub
import pandas as pd
from kagglehub import KaggleDatasetAdapter

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "jamieb122/golf-swing-and-trajectory-data",
    "golf_trajectory.csv",
)

columns = ["Club Path (deg)", "Club Face (deg)", "Launch Direction (deg)", "Sidespin (rpm)"]
complete_df = df[columns].dropna()
print(complete_df)
