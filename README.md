### INF601 - Advanced Programming in Python
### Ray Bednara
### Mini Project 3


# Golf Swing Trajectory Charts

Pull golf swing and trajectory data with kagglehub and chart it with matplotlib.

## Description

This project uses `kagglehub` to load the `golf_trajectory.csv` dataset from
[jamieb122/golf-swing-and-trajectory-data](https://www.kaggle.com/datasets/jamieb122/golf-swing-and-trajectory-data)
(832 recorded shots, 24 swing/ball-flight measurements) into a pandas DataFrame.
The data is narrowed down to two columns, `Face to Path (deg)` and
`Launch Direction (deg)`, dropping any shot missing either value, and a scatter
chart of the two is saved as a PNG into a `charts/` directory (created
automatically if it doesn't exist).

## Getting Started

### Dependencies

* Windows 10/11
* Python 3.13
* Internet connection (kagglehub downloads the dataset on first run)
* Install required libraries with:
```
pip install -r requirements.txt
```

### Installing

* Clone or download this repository
* No file/folder modifications are needed; the `charts/` output directory is
  created automatically when the program runs

### Executing program

* Run the script from the project root:
```
python golf.py
```
* The script will:
    * Download the golf trajectory dataset via kagglehub
    * Print the `Face to Path (deg)` / `Launch Direction (deg)` data to the console
    * Save a Face to Path vs. Launch Direction scatter chart to `charts/`

## Help

If `kagglehub` fails to load the dataset, check your internet connection. Some
rows in the raw data are missing `Face to Path (deg)` or `Launch Direction (deg)`
readings; those rows are dropped before charting.

`df[columns]` narrows the full 24-column dataset down to just those two
columns, and `.dropna()` then removes any row where either value is missing
(by default it drops a row if *any* of its columns are `NaN`). This guarantees
every row that reaches the chart has a real value for both axes.

## Authors

Ray Bednara
ray.bednara@gmail.com

## AI Usage

I used Claude Code to write `golf.py`: loading the golf trajectory dataset with
kagglehub, narrowing it down to the Face to Path and Launch Direction columns,
and generating the matplotlib scatter chart saved to `charts/`. I also asked it
to explain what `.dropna()` does, which allows the chart to be fully accurate in that only columns with both datapoints exists.
