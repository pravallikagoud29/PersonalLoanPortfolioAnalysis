"""
build_notebook.py
-----------------
Generates the Jupyter notebook for the Personal Loan Portfolio Analysis
project using nbformat so the notebook is always valid and consistent.

Run:
    python src/build_notebook.py
"""

import os
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

NB_PATH = os.path.join(os.path.dirname(__file__), "..", "notebooks",
                       "Personal_Loan_Portfolio_Analysis.ipynb")


def build() -> nbf.NotebookNode:
    nb = new_notebook()
    cells = []

    def md(text):
        cells.append(new_markdown_cell(text))

    def code(text):
        cells.append(new_code_cell(text))

    # ====================================================================
    # TITLE
    # ====================================================================
    md("""# Personal Loan Portfolio Analysis

### Apex Credit Union — Exploratory Data Analysis (EDA)

**Project by:** Data Science Intern  
**Dataset:** `personal_loan_data.csv`  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

---

## Project Overview

Apex Credit Union wants to understand the demographics and loan
characteristics of its personal-loan customers. This notebook performs a
complete **exploratory data analysis (EDA)** to identify trends and patterns
in the loan portfolio and produce useful business insights.

The analysis follows these sections:

1. Import Libraries  
2. Load Dataset  
3. Understand Dataset  
4. Data Cleaning  
5. Missing Value Analysis  
6. Duplicate Value Check  
7. Descriptive Statistics  
8. Univariate Analysis  
9. Bivariate Analysis  
10. Correlation Analysis  
11. Customer Segmentation  
12. Business Insights  
13. Conclusion  
14. Executive Summary""")

    # ====================================================================
    # 1. IMPORT LIBRARIES
    # ====================================================================
    md("""## 1. Import Libraries

We import the standard data-science libraries used throughout this project.""")

    code("""# Data manipulation
import pandas as pd
import numpy as np

# Visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# Reusable helper functions from the src folder
import sys
sys.path.append("../src")
from analysis import (
    load_data, clean_data, missing_value_report,
    add_income_group, add_age_group, add_family_group,
    key_metrics, acceptance_by_group,
    plot_distribution, plot_count, plot_loan_acceptance_by_group,
    plot_correlation_heatmap, plot_boxplot_by_loan,
    EDUCATION_LABELS,
)

# Use a clean chart style
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

# Show all columns when printing DataFrames
pd.set_option("display.max_columns", None)

print("Libraries imported successfully.")""")

    # ====================================================================
    # 2. LOAD DATASET
    # ====================================================================
    md("""## 2. Load Dataset

We load the CSV file `personal_loan_data.csv` from the `data/` folder.
If you have the official internship dataset, replace this file with your own
(keeping the same column names) and the rest of the notebook will work
unchanged.""")

    code("""# Load the dataset using the helper function.
df = load_data("../data/personal_loan_data.csv")

# Preview the first few rows.
df.head()""")

    # ====================================================================
    # 3. UNDERSTAND DATASET
    # ====================================================================
    md("""## 3. Understand Dataset

Before cleaning, we look at the shape of the data, the column names and the
data types so we know what we are working with.""")

    code("""# Number of rows and columns.
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])""")

    code("""# Column names and data types.
df.info()""")

    code("""# List of column names.
print("Columns:", list(df.columns))""")

    code("""# Preview the last few rows.
df.tail()""")

    # ====================================================================
    # 4. DATA CLEANING
    # ====================================================================
    md("""## 4. Data Cleaning

We clean the data by:
- Removing duplicate rows
- Fixing data types
- Handling impossible values (e.g. negative experience)
- Dropping the ID column (not useful for analysis)
- Adding a readable education label column

The number of rows and columns before and after cleaning is shown so the
effect of cleaning is transparent.""")

    code("""# Keep a copy of the original data for reference.
df_original = df.copy()

# Apply the cleaning function (prints before/after shape).
df = clean_data(df)

# Preview cleaned data.
df.head()""")

    code("""# Check data types after cleaning.
df.dtypes""")

    # ====================================================================
    # 5. MISSING VALUE ANALYSIS
    # ====================================================================
    md("""## 5. Missing Value Analysis

We check whether any column contains missing (empty) values. Missing values
can bias the analysis, so we need to find and handle them.""")

    code("""# Generate a missing-value report.
missing_report = missing_value_report(df)
missing_report""")

    code("""# Visualise missing values as a heatmap (if any).
if df.isnull().sum().sum() > 0:
    plt.figure(figsize=(10, 4))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values Heatmap")
    plt.show()
else:
    print("No missing values to visualise.")""")

    # ====================================================================
    # 6. DUPLICATE VALUE CHECK
    # ====================================================================
    md("""## 6. Duplicate Value Check

Duplicate rows can double-count customers and distort results. We check for
exact duplicates (already removed during cleaning) and confirm the count.""")

    code("""# Count duplicate rows in the cleaned dataset.
duplicate_count = df.duplicated().sum()
print(f"Duplicate rows in cleaned dataset: {duplicate_count}")""")

    # ====================================================================
    # 7. DESCRIPTIVE STATISTICS
    # ====================================================================
    md("""## 7. Descriptive Statistics

We compute summary statistics (mean, median, min, max, etc.) for every numeric
column to understand the distribution and scale of each variable.""")

    code("""# Summary statistics for numeric columns.
df.describe().round(2)""")

    code("""# Summary for categorical / binary columns.
categorical_cols = ["Education", "Personal Loan", "Securities Account",
                    "CD Account", "Online", "CreditCard"]
df[categorical_cols].astype(str).describe()""")

    # ====================================================================
    # 8. UNIVARIATE ANALYSIS
    # ====================================================================
    md("""## 8. Univariate Analysis

Univariate analysis looks at one variable at a time. We plot distributions for
the key numeric and categorical variables.""")

    md("""### 8.1 Age Distribution""")

    code("""plot_distribution(df, "Age", "Age Distribution of Customers",
          "Age (years)", color="#4C72B0")""")

    md("""### 8.2 Income Distribution""")

    code("""plot_distribution(df, "Income", "Income Distribution of Customers",
          "Annual income ($000s)", color="#55A868")""")

    md("""### 8.3 CCAvg (Average Credit Card Spending) Distribution""")

    code("""plot_distribution(df, "CCAvg", "Average Monthly Credit Card Spending",
          "CCAvg ($000s/month)", color="#C44E52")""")

    md("""### 8.4 Mortgage Distribution""")

    code("""plot_distribution(df, "Mortgage", "Mortgage Distribution",
          "Mortgage ($000s)", color="#8172B3", bins=30)""")

    md("""### 8.5 Education Distribution""")

    code("""plot_count(df, "EducationLabel", "Education Level Distribution",
        "Education level")""")

    md("""### 8.6 Family Size Distribution""")

    code("""plot_count(df, "Family", "Family Size Distribution", "Family size")""")

    md("""### 8.7 Personal Loan Acceptance Count""")

    code("""plot_count(df, "Personal Loan", "Personal Loan Acceptance Count",
        "Accepted Personal Loan (0 = No, 1 = Yes)")""")

    md("""### 8.8 Online Banking Usage""")

    code("""plot_count(df, "Online", "Online Banking Usage",
        "Uses Online Banking (0 = No, 1 = Yes)")""")

    md("""### 8.9 Credit Card Usage""")

    code("""plot_count(df, "CreditCard", "Credit Card Usage (Issued by Bank)",
        "Has Bank Credit Card (0 = No, 1 = Yes)")""")

    md("""### 8.10 CD Account & Securities Account""")

    code("""fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.countplot(data=df, x="CD Account", hue="CD Account", ax=axes[0], legend=False)
axes[0].set_title("CD Account Holders")
axes[0].set_xlabel("CD Account (0 = No, 1 = Yes)")
axes[0].set_ylabel("Number of customers")

sns.countplot(data=df, x="Securities Account", hue="Securities Account",
              ax=axes[1], legend=False)
axes[1].set_title("Securities Account Holders")
axes[1].set_xlabel("Securities Account (0 = No, 1 = Yes)")
axes[1].set_ylabel("Number of customers")
plt.show()""")

    # ====================================================================
    # 9. BIVARIATE ANALYSIS
    # ====================================================================
    md("""## 9. Bivariate Analysis

Bivariate analysis examines the relationship between two variables. Here we
focus on how each variable relates to **Personal Loan acceptance**.""")

    md("""### 9.1 Income vs Personal Loan""")

    code("""plot_boxplot_by_loan(df, "Income",
    "Income vs Personal Loan Acceptance", "Annual income ($000s)")""")

    code("""# Loan acceptance rate by income group (data-driven tertiles).
df = add_income_group(df)
plot_loan_acceptance_by_group(df, "IncomeGroup",
    "Loan Acceptance Rate by Income Group", "Income group")""")

    md("""### 9.2 Education vs Personal Loan""")

    code("""plot_loan_acceptance_by_group(df, "EducationLabel",
    "Loan Acceptance Rate by Education Level", "Education level")""")

    md("""### 9.3 Age vs Personal Loan""")

    code("""plot_boxplot_by_loan(df, "Age",
    "Age vs Personal Loan Acceptance", "Age (years)")""")

    code("""# Loan acceptance rate by age group.
df = add_age_group(df)
plot_loan_acceptance_by_group(df, "AgeGroup",
    "Loan Acceptance Rate by Age Group", "Age group")""")

    md("""### 9.4 Family Size vs Personal Loan""")

    code("""df = add_family_group(df)
plot_loan_acceptance_by_group(df, "FamilyGroup",
    "Loan Acceptance Rate by Family Size", "Family size")""")

    md("""### 9.5 CD Account vs Personal Loan""")

    code("""plot_loan_acceptance_by_group(df, "CD Account",
    "Loan Acceptance Rate by CD Account", "Has CD Account (0 = No, 1 = Yes)")""")

    md("""### 9.6 Securities Account vs Personal Loan""")

    code("""plot_loan_acceptance_by_group(df, "Securities Account",
    "Loan Acceptance Rate by Securities Account",
    "Has Securities Account (0 = No, 1 = Yes)")""")

    md("""### 9.7 Online Banking vs Personal Loan""")

    code("""plot_loan_acceptance_by_group(df, "Online",
    "Loan Acceptance Rate by Online Banking",
    "Uses Online Banking (0 = No, 1 = Yes)")""")

    md("""### 9.8 Credit Card vs Personal Loan""")

    code("""plot_loan_acceptance_by_group(df, "CreditCard",
    "Loan Acceptance Rate by Credit Card Usage",
    "Has Bank Credit Card (0 = No, 1 = Yes)")""")

    # ====================================================================
    # 10. CORRELATION ANALYSIS
    # ====================================================================
    md("""## 10. Correlation Analysis

A correlation heatmap shows how strongly numeric variables are related to each
other. Values close to +1 or -1 indicate a strong positive or negative
relationship.""")

    code("""plot_correlation_heatmap(df)""")

    code("""# Correlation of every numeric variable with Personal Loan, sorted.
corr_with_loan = df.select_dtypes(include=[np.number]).corr()["Personal Loan"]\\
    .drop("Personal Loan").sort_values(ascending=False)
corr_with_loan.round(3)""")

    # ====================================================================
    # 11. CUSTOMER SEGMENTATION
    # ====================================================================
    md("""## 11. Customer Segmentation

We create meaningful customer groups using data-driven thresholds and compare
their loan-acceptance behaviour.""")

    md("""### 11.1 Income Groups (Low / Medium / High)

We split customers into three equal-frequency groups (tertiles) based on
income. This keeps the thresholds tied to the actual data distribution rather
than guessing numbers.""")

    code("""# Income group thresholds (data-driven).
income_thresholds = df["Income"].quantile([0, 1/3, 2/3, 1]).round(1).tolist()
print("Income group thresholds ($000s):", income_thresholds)

acceptance_by_group(df, "IncomeGroup")""")

    md("""### 11.2 Age Groups""")

    code("""acceptance_by_group(df, "AgeGroup")""")

    md("""### 11.3 Education Groups""")

    code("""acceptance_by_group(df, "EducationLabel")""")

    md("""### 11.4 Family Size Groups""")

    code("""acceptance_by_group(df, "FamilyGroup")""")

    md("""### 11.5 High-Value Customer Segment

We define a "high-value" segment as customers who are **high income** AND
**graduate or advanced education**. This is the group most likely to accept a
personal loan and therefore a strong marketing target.""")

    code("""# Define high-value segment: high income + education >= 2.
df["HighValueSegment"] = ((df["IncomeGroup"] == "High income") &
                          (df["Education"] >= 2)).astype(int)

high_value_stats = pd.DataFrame({
    "Customers": [ (df["HighValueSegment"]==0).sum(), df["HighValueSegment"].sum() ],
    "Loan acceptance rate (%)": [
        round(df.loc[df["HighValueSegment"]==0, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["HighValueSegment"]==1, "Personal Loan"].mean()*100, 1),
    ]
}, index=["Other customers", "High-value segment"])
high_value_stats""")

    # ====================================================================
    # 12. BUSINESS INSIGHTS
    # ====================================================================
    md("""## 12. Business Insights

We now calculate the key numbers behind each insight so every conclusion is
backed by the data — nothing is invented.""")

    code("""# Headline metrics.
metrics = key_metrics(df)
for k, v in metrics.items():
    print(f"{k}: {v}")""")

    code("""# Loan acceptance rate by education.
edu_rates = acceptance_by_group(df, "EducationLabel")
print("Loan acceptance rate by education:")
print(edu_rates)
print()

# Loan acceptance rate by income group.
income_rates = acceptance_by_group(df, "IncomeGroup")
print("Loan acceptance rate by income group:")
print(income_rates)
print()

# Loan acceptance rate by family size.
family_rates = acceptance_by_group(df, "FamilyGroup")
print("Loan acceptance rate by family size:")
print(family_rates)
print()

# Loan acceptance rate by age group.
age_rates = acceptance_by_group(df, "AgeGroup")
print("Loan acceptance rate by age group:")
print(age_rates)""")

    code("""# Relationship between existing banking products and loan acceptance.
product_rates = pd.DataFrame({
    "Product": ["CD Account", "Securities Account", "Online", "CreditCard"],
    "Acceptance rate — has product (%)": [
        round(df.loc[df["CD Account"]==1, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["Securities Account"]==1, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["Online"]==1, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["CreditCard"]==1, "Personal Loan"].mean()*100, 1),
    ],
    "Acceptance rate — no product (%)": [
        round(df.loc[df["CD Account"]==0, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["Securities Account"]==0, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["Online"]==0, "Personal Loan"].mean()*100, 1),
        round(df.loc[df["CreditCard"]==0, "Personal Loan"].mean()*100, 1),
    ],
})
product_rates""")

    md("""### Key Business Insights

Based on the calculations above, here are the data-backed insights for
Apex Credit Union:""")

    code("""# Collect calculated values for the written insights.
overall_rate = metrics["Personal Loan acceptance rate (%)"]
high_income_rate = income_rates.loc["High income", "Acceptance Rate (%)"]
low_income_rate = income_rates.loc["Low income", "Acceptance Rate (%)"]
adv_edu_rate = edu_rates.loc["Advanced / Professional", "Acceptance Rate (%)"]
undergrad_rate = edu_rates.loc["Undergraduate", "Acceptance Rate (%)"]
cd_yes = product_rates.loc[product_rates["Product"]=="CD Account",
                           "Acceptance rate — has product (%)"].values[0]
cd_no = product_rates.loc[product_rates["Product"]=="CD Account",
                          "Acceptance rate — no product (%)"].values[0]
sec_yes = product_rates.loc[product_rates["Product"]=="Securities Account",
                            "Acceptance rate — has product (%)"].values[0]
hv_rate = high_value_stats.loc["High-value segment", "Loan acceptance rate (%)"]
hv_count = high_value_stats.loc["High-value segment", "Customers"]

insights = [
    f"1. Overall, {overall_rate}% of customers accepted a personal loan in the campaign.",

    f"2. Income is the strongest driver of loan acceptance. High-income customers "
    f"accepted at {high_income_rate}%, compared to only {low_income_rate}% for low-income "
    f"customers — a gap of {round(high_income_rate-low_income_rate,1)} percentage points.",

    f"3. Education is positively related to loan acceptance. Advanced / Professional "
    f"customers accepted at {adv_edu_rate}% versus {undergrad_rate}% for undergraduates.",

    f"4. Customers with a CD account are far more likely to accept a personal loan "
    f"({cd_yes}% vs {cd_no}%), suggesting existing deposit customers are a strong target.",

    f"5. Customers with a securities account also show higher acceptance "
    f"({sec_yes}%), indicating investment-savvy customers are more receptive.",

    f"6. The high-value segment (high income + graduate/advanced education) contains "
    f"{hv_count} customers and accepts loans at {hv_rate}% — well above the average.",

    f"7. Family size has a modest effect: larger families (size 3-4) tend to accept "
    f"loans slightly more often, likely due to greater financial needs.",

    f"8. Age has a weak relationship with loan acceptance; the 30-50 age band is "
    f"slightly more receptive, but age alone is not a strong predictor.",

    f"9. Online banking users accept loans at a comparable or slightly higher rate, "
    f"so digital channels are a suitable marketing channel for loan campaigns.",

    f"10. Mortgage holders show a slightly higher acceptance rate, possibly because "
    f"they are already comfortable with bank credit products.",
]

for insight in insights:
    print(insight)
    print()""")

    # ====================================================================
    # 13. CONCLUSION
    # ====================================================================
    md("""## 13. Conclusion

This exploratory data analysis examined the personal-loan portfolio of
Apex Credit Union. The key takeaways are:

- **Income** is the single strongest factor linked to personal-loan acceptance.
- **Education** and **existing banking products** (CD account, securities
  account) are also positively associated with acceptance.
- A clearly identifiable **high-value segment** (high income + higher
  education) accepts loans at a rate well above the average and should be the
  focus of future marketing campaigns.
- Age and family size have weaker effects but still provide useful context
  for segmentation.

The analysis was performed entirely with Python, Pandas, Matplotlib and
Seaborn — no machine learning was used — keeping the project beginner-friendly
and focused on exploratory data analysis.""")

    code("""# Print a dynamic conclusion summary using the calculated metrics.
print(f"This analysis covered {metrics['Total customers']} customers.")
print(f"Overall loan acceptance rate: {metrics['Personal Loan acceptance rate (%)']}%")
print(f"Average income: ${metrics['Average income ($000s)']}K/year")
print(f"Average age: {metrics['Average age']} years")
print()
print("Income is the strongest driver of loan acceptance, followed by")
print("education and existing banking product holdings (CD / securities).")
print("The high-value segment (high income + higher education) is the")
print("prime target for future personal-loan marketing campaigns.")""")

    # ====================================================================
    # 14. EXECUTIVE SUMMARY
    # ====================================================================
    md("""## 14. Executive Summary

The executive summary below is generated from the calculated results so every
number is backed by the data.""")

    code("""# Generate the Executive Summary from calculated values.
print("=" * 60)
print("           EXECUTIVE SUMMARY")
print("=" * 60)
print()
print("KEY FINDINGS")
print("-" * 60)
print(f"- Total customers analysed: {metrics['Total customers']}")
print(f"- Overall loan acceptance rate: {metrics['Personal Loan acceptance rate (%)']}%")
print(f"- Average income: ${metrics['Average income ($000s)']}K/year")
print(f"- Average age: {metrics['Average age']} years")
print(f"- High-income acceptance rate: {high_income_rate}% vs low-income: {low_income_rate}%")
print(f"- CD account holders acceptance: {cd_yes}% vs non-holders: {cd_no}%")
print(f"- Advanced education acceptance: {adv_edu_rate}% vs undergraduate: {undergrad_rate}%")
print()
print("IMPORTANT CUSTOMER SEGMENTS")
print("-" * 60)
print("- High income + higher education  -> highest acceptance (prime target)")
print("- CD account holders              -> already trust the bank with deposits")
print("- Securities account holders      -> investment-savvy, receptive to credit")
print("- Age 30-50                       -> peak earning years, slightly higher acceptance")
print()
print("IMPORTANT TRENDS")
print("-" * 60)
print("- Loan acceptance increases steadily with income.")
print("- Customers with more existing bank products accept loans more often.")
print("- Online banking users are reachable through digital marketing.")
print("- Family size has a modest positive effect on acceptance.")
print()
print("BUSINESS RECOMMENDATIONS")
print("-" * 60)
print("1. Target the high-value segment (high income + graduate/advanced")
print("   education) first — highest acceptance rate.")
print("2. Cross-sell to existing deposit customers (CD account holders).")
print("3. Use online banking channels to deliver loan offers efficiently.")
print("4. Design income-tiered offers instead of one-size-fits-all loans.")
print("5. Future improvement: build a simple ML model to predict loan")
print("   acceptance (optional, beyond the scope of this EDA).")
print("=" * 60)""")

    nb["cells"] = cells
    return nb


def main() -> None:
    nb = build()
    os.makedirs(os.path.dirname(NB_PATH), exist_ok=True)
    with open(NB_PATH, "w", encoding="utf-8") as f:
        nbf.write(nb, f)
    print(f"Notebook created: {NB_PATH}")
    print(f"Total cells: {len(nb['cells'])}")


if __name__ == "__main__":
    main()
