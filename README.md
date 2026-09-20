### INF601 - Advanced Programming in Python
### Ray Bednara
### Mini Project 3


# Golf Swing Trajectory Charts

Pull golf swing and trajectory data with kagglehub and chart it with matplotlib.

## Description

This project uses `kagglehub` to load the `golf_trajectory.csv` dataset from
[jamieb122/golf-swing-and-trajectory-data](https://www.kaggle.com/datasets/jamieb122/golf-swing-and-trajectory-data)
(832 recorded shots, 24 swing/ball-flight measurements) into a pandas DataFrame.
Five charts are generated from that data and saved as PNG files into a `charts/`
directory, which is created automatically if it doesn't exist:

* Club Speed vs. Ball Speed
* Launch Angle vs. Carry Distance
* Attack Angle vs. Backspin
* Spin Rate vs. Apex Height
* Distribution of Total Distance

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
    * Print the shape and a preview of the data to the console
    * Save one chart per relationship to `charts/`

## Help

If `kagglehub` fails to load the dataset, check your internet connection. Some
rows in the raw data are missing values or contain infinite/garbage readings
(e.g. `Smash Factor`); each chart drops rows with missing or non-finite values
for the columns it plots.

## Authors

Ray Bednara
ray.bednara@gmail.com

## Version History

* 0.1
    * Initial release: kagglehub pull of golf swing trajectory data and five
      matplotlib charts saved to `charts/`

## License

## AI Usage

I used Claude Code to write `golf.py`: loading the golf trajectory dataset with
kagglehub, choosing which columns to chart, and generating the matplotlib
charts saved to `charts/`.
