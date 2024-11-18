import pandas as pd
import numpy as np

#file_path=r'C:\Users\Pragya Jain\OneDrive\Attachments\Desktop\data_quality_check\data-quality-checks\dataset.csv'
file_path=r'https://raw.githubusercontent.com/pragya0209jain/data-quality-checks/refs/heads/addingPythonScript/dataset.csv'
data = pd.read_csv(file_path)

# Function to generate a Data Quality Summary Report
def data_quality_summary(data):
    # Initialize report dictionary
    report = {}

    # 1. Missing Values Summary
    missing_values = data.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    report['Missing Values Summary'] = missing_values

    # 2. Duplicates Summary
    duplicate_rows = data.duplicated().sum()
    report['Duplicate Rows'] = duplicate_rows

    # 3. Outlier Detection (IQR method)
    outlier_summary = {}
    for column in data.select_dtypes(include=[np.number]).columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((data[column] < lower_bound) | (data[column] > upper_bound)).sum()
        outlier_summary[column] = outliers
    report['Outlier Summary'] = outlier_summary

    # 4. Create the final report output
    report_str = "\n--- Data Quality Summary Report ---\n"

    # Missing Values
    report_str += "\nMissing Values Summary:\n"
    if len(missing_values) > 0:
        report_str += missing_values.to_string()
    else:
        report_str += "No missing values found.\n"

    # Duplicates
    report_str += f"\nTotal Duplicate Rows: {duplicate_rows}\n"

    # Outliers
    report_str += "\nOutlier Summary (using IQR method):\n"
    if len(outlier_summary) > 0:
        for column, outliers in outlier_summary.items():
            report_str += f"{column}: {outliers} outliers\n"
    else:
        report_str += "No outliers detected.\n"

    # Returning the summary report
    return report_str

# Generate the Data Quality Summary Report
summary_report = data_quality_summary(data)

# Output the summary report to the console
print(summary_report)

# Optionally, save the summary report to a file
with open("data_quality_summary_report.txt", "w") as f:
    f.write(summary_report)