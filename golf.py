# INF601 - Advanced Programming in Python
# Ray Bednara
# Mini Project 3

import kagglehub
from kagglehub import KaggleDatasetAdapter

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "jamieb122/golf-swing-and-trajectory-data",
    "golf_trajectory.csv",
)

print("First 5 records:", df.head())
