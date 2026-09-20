# INF601 - Advanced Programming in Python
# Ray Bednara
# Mini Project 3

import os

import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
from kagglehub import KaggleDatasetAdapter

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

CHARTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "jamieb122/golf-swing-and-trajectory-data",
    "golf_trajectory.csv",
)

columns = ["Face to Path (deg)", "Launch Direction (deg)"]
complete_df = df[columns].dropna()
print(complete_df)

os.makedirs(CHARTS_DIR, exist_ok=True)

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(
    complete_df["Face to Path (deg)"],
    complete_df["Launch Direction (deg)"],
    color="tab:blue",
    alpha=0.5,
    s=20,
)
ax.set_title("Face to Path vs. Launch Direction")
ax.set_xlabel("Face to Path (deg)")
ax.set_ylabel("Launch Direction (deg)")
ax.grid(True, alpha=0.3)
fig.tight_layout()

out_path = os.path.join(CHARTS_DIR, "face_to_path_launch_direction.png")
fig.savefig(out_path)
plt.close(fig)
print(f"Saved {out_path}")
