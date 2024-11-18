# Data Quality Checks

This repository contains a Python script designed to perform basic data quality checks on a CSV dataset. It helps in identifying and summarizing issues such as missing values, duplicate rows, and outliers in the dataset.

## Features

- **Missing Values Check**: Detects and counts missing values for each column in the dataset.
- **Duplicate Rows Check**: Identifies and counts duplicate rows in the dataset.
- **Outliers Detection**: Highlights potential outliers in numerical columns using the Interquartile Range (IQR) method.
- **Summary Report**: Generates a comprehensive "Data Quality Summary Report" combining the results of all checks.

## Dataset

The dataset is sourced directly from this repository on GitHub. The script is designed to fetch the dataset using its URL, ensuring ease of use and no dependency on local files.

## Requirements

- Python 3.8 or above
- Required Python libraries:
  - `pandas`
  - `numpy`

## Installation

1. Clone this repository:
   bash
   ```
   git clone https://github.com/your-username/data-quality-checks.git
   cd data-quality-checks
   ```
2. Install the required dependencies:
bash
```
pip install -r requirements.txt
```
3. Run the script:
```
python data_quality_checks.py
```
