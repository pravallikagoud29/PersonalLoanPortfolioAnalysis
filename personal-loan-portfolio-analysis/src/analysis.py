"""
analysis.py
------------
Modular helper functions for the Personal Loan Portfolio Analysis project.

This module keeps the reusable data-cleaning, analysis and visualisation
functions in one place so the Jupyter notebook stays clean and readable.

The functions are written in a beginner-friendly style: each one has a short
docstring, clear variable names and comments explaining the important steps.
"""

from __future__ import annotations

import os
import warnings
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Use a clean, readable style for all charts.
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110
plt.rcParams["savefig.dpi"] = 110
plt.rcParams["figure.autolayout"] = True

# Directory where generated charts are saved.
VIZ_DIR = os.path.join(os.path.dirname(__file__), "..", "visualizations")

# Education level labels used across charts and insights.
EDUCATION_LABELS = {
    1: "Undergraduate",
    2: "Graduate",
    3: "Advanced / Professional",
}


# ---------------------------------------------------------------------------
# 1. Loading
# ---------------------------------------------------------------------------
def load_data(path: str) -> pd.DataFrame:
    """Load the personal-loan CSV file into a pandas DataFrame.

    The path defaults to data/personal_loan_data.csv relative to this file,
    but any CSV with the same columns can be supplied.
    """
    df = pd.read_csv(path)
    print(f"Dataset loaded: {df.shape[0]} rows x {df.shape[1]} columns")
    return df


# ---------------------------------------------------------------------------
# 2. Cleaning
# ---------------------------------------------------------------------------
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform basic data cleaning and return a cleaned copy.

    Steps:
      * Remove duplicate rows.
      * Fix data types.
      * Handle impossible values (e.g. negative experience).
      * Drop the ID column (not useful for analysis).
      * Map education codes to readable labels in a new column.

    The number of rows/columns before and after cleaning is printed so the
    effect of cleaning is transparent.
    """
    print(f"Before cleaning: {df.shape[0]} rows x {df.shape[1]} columns")

    df_clean = df.copy()

    # Remove exact duplicate rows, if any.
    duplicates = df_clean.duplicated().sum()
    if duplicates:
        print(f"  - Removed {duplicates} duplicate row(s)")
        df_clean = df_clean.drop_duplicates()

    # Fix data types for categorical / binary columns.
    binary_cols = [
        "Personal Loan", "Securities Account", "CD Account",
        "Online", "CreditCard",
    ]
    for col in binary_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(int)

    # Experience cannot be negative. Replace negative values with 0.
    if "Experience" in df_clean.columns:
        neg_exp = (df_clean["Experience"] < 0).sum()
        if neg_exp:
            print(f"  - Fixed {neg_exp} negative experience value(s)")
            df_clean.loc[df_clean["Experience"] < 0, "Experience"] = 0

    # Drop the ID column — it is just a row identifier.
    if "ID" in df_clean.columns:
        df_clean = df_clean.drop(columns=["ID"])

    # Add a readable education label column for easier plotting.
    if "Education" in df_clean.columns:
        df_clean["EducationLabel"] = df_clean["Education"].map(EDUCATION_LABELS)

    print(f"After cleaning:  {df_clean.shape[0]} rows x {df_clean.shape[1]} columns")
    return df_clean


# ---------------------------------------------------------------------------
# 3. Missing-value analysis
# ---------------------------------------------------------------------------
def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return a table showing missing-value count and percentage per column."""
    missing = df.isnull().sum()
    report = pd.DataFrame(
        {
            "Missing Count": missing,
            "Missing %": (missing / len(df) * 100).round(2),
        }
    )
    report = report[report["Missing Count"] > 0].sort_values("Missing Count", ascending=False)
    if report.empty:
        print("No missing values found in the dataset.")
    return report


# ---------------------------------------------------------------------------
# 4. Customer segmentation helpers
# ---------------------------------------------------------------------------
def add_income_group(df: pd.DataFrame) -> pd.DataFrame:
    """Add an IncomeGroup column using data-driven tertiles (low / medium / high).

    Using tertiles (3 equal-frequency groups) instead of arbitrary numbers keeps
    the thresholds tied to the actual distribution of the data.
    """
    df = df.copy()
    df["IncomeGroup"] = pd.qcut(
        df["Income"], q=3, labels=["Low income", "Medium income", "High income"]
    )
    return df


def add_age_group(df: pd.DataFrame) -> pd.DataFrame:
    """Add an AgeGroup column using sensible age brackets."""
    df = df.copy()
    bins = [0, 30, 40, 50, 60, 100]
    labels = ["Under 30", "30-40", "40-50", "50-60", "Over 60"]
    df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)
    return df


def add_family_group(df: pd.DataFrame) -> pd.DataFrame:
    """Add a readable FamilyGroup column (Small / Medium / Large)."""
    df = df.copy()
    df["FamilyGroup"] = df["Family"].map({1: "Single", 2: "Small", 3: "Medium", 4: "Large"})
    return df


# ---------------------------------------------------------------------------
# 5. Key metric calculations
# ---------------------------------------------------------------------------
def key_metrics(df: pd.DataFrame) -> dict:
    """Calculate the headline numbers used in the insights section."""
    metrics = {
        "Total customers": len(df),
        "Average age": round(df["Age"].mean(), 1),
        "Average income ($000s)": round(df["Income"].mean(), 1),
        "Average CCAvg ($000s/mo)": round(df["CCAvg"].mean(), 2),
        "Average mortgage ($000s)": round(df["Mortgage"].mean(), 1),
        "Personal Loan acceptance rate (%)": round(df["Personal Loan"].mean() * 100, 1),
    }
    return metrics


def acceptance_by_group(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """Compute loan acceptance rate (%) and count for each level of a grouping column."""
    grouped = df.groupby(group_col, observed=True)["Personal Loan"].agg(["mean", "count"])
    grouped["Acceptance Rate (%)"] = (grouped["mean"] * 100).round(1)
    grouped = grouped.rename(columns={"count": "Customers"}).drop(columns=["mean"])
    return grouped[["Customers", "Acceptance Rate (%)"]]


# ---------------------------------------------------------------------------
# 6. Visualisation helpers
# ---------------------------------------------------------------------------
def save_figure(fig: plt.Figure, filename: str) -> None:
    """Save a figure to the visualizations folder and close it."""
    os.makedirs(VIZ_DIR, exist_ok=True)
    path = os.path.join(VIZ_DIR, filename)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {path}")


def plot_distribution(df: pd.DataFrame, column: str, title: str, xlabel: str,
                      color: str = "#4C72B0", bins: int = 30, save: bool = True) -> None:
    """Plot a histogram with a kernel-density estimate for a numeric column."""
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df[column], bins=bins, kde=True, color=color, ax=ax)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel("Number of customers", fontsize=11)
    plt.show()
    if save:
        save_figure(fig, f"{column.lower().replace(' ', '_')}_distribution.png")


def plot_count(df: pd.DataFrame, column: str, title: str, xlabel: str,
               palette: str = "Set2", save: bool = True) -> None:
    """Plot a count (bar) chart for a categorical column."""
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.countplot(data=df, x=column, hue=column, palette=palette, ax=ax, legend=False)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel("Number of customers", fontsize=11)
    plt.show()
    if save:
        save_figure(fig, f"{column.lower().replace(' ', '_')}_count.png")


def plot_loan_acceptance_by_group(df: pd.DataFrame, group_col: str, title: str,
                                  xlabel: str, save: bool = True) -> None:
    """Bar chart of personal-loan acceptance rate by a grouping column."""
    rates = acceptance_by_group(df, group_col).reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(data=rates, x=group_col, y="Acceptance Rate (%)",
                hue=group_col, palette="viridis", ax=ax, legend=False)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel("Loan acceptance rate (%)", fontsize=11)
    for i, row in rates.iterrows():
        ax.text(i, row["Acceptance Rate (%)"] + 0.5, f"{row['Acceptance Rate (%)']:.1f}%",
                ha="center", fontsize=10)
    plt.show()
    if save:
        save_name = group_col.lower().replace(" ", "_") + "_vs_loan.png"
        save_figure(fig, save_name)


def plot_correlation_heatmap(df: pd.DataFrame, save: bool = True) -> None:
    """Plot a correlation heatmap for all numeric columns."""
    numeric_df = df.select_dtypes(include=[np.number])
    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(11, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
                square=True, linewidths=0.5, ax=ax, cbar_kws={"shrink": 0.8})
    ax.set_title("Correlation Heatmap of Numeric Features",
                 fontsize=14, fontweight="bold")
    plt.show()
    if save:
        save_figure(fig, "correlation_heatmap.png")


def plot_boxplot_by_loan(df: pd.DataFrame, column: str, title: str,
                         ylabel: str, save: bool = True) -> None:
    """Box plot of a numeric column split by Personal Loan acceptance."""
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.boxplot(data=df, x="Personal Loan", y=column, hue="Personal Loan",
                palette="Set2", ax=ax, legend=False)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Accepted Personal Loan (0 = No, 1 = Yes)", fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    plt.show()
    if save:
        save_figure(fig, f"{column.lower()}_vs_loan_box.png")
