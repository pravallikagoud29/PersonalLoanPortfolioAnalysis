# Personal Loan Portfolio Analysis

## Project Overview

This project performs an **Exploratory Data Analysis (EDA)** on the personal-loan
customer dataset of **Apex Credit Union**. The goal is to understand the
demographics and loan characteristics of customers who accepted a personal loan,
identify important trends and patterns, and produce actionable business insights.

The project is built as a beginner-friendly Data Science internship portfolio
piece using **Python, Pandas, NumPy, Matplotlib, and Seaborn** in a Jupyter
Notebook. No machine learning is used in the main analysis.

---

## Business Problem

Apex Credit Union ran a personal-loan campaign and wants to know:

- What kind of customers are most likely to accept a personal loan?
- Which demographic and financial factors are associated with loan acceptance?
- Which customer segments should the bank target in future campaigns?

Answering these questions helps the bank design better marketing strategies,
improve loan conversion rates, and reduce the cost of targeting unlikely
customers.

---

## Objectives

1. Explore customer demographics (age, education, family size).
2. Analyze income and spending distributions.
3. Study the relationship between income, education, and loan acceptance.
4. Examine how existing banking products relate to loan acceptance.
5. Identify high-value customer segments for future marketing.
6. Generate clear, data-backed business insights.

---

## Dataset Description

The dataset is stored in `data/personal_loan_data.csv` and contains **500
customer records** with the following columns:

| Column | Description |
|---|---|
| ID | Unique customer identifier |
| Age | Customer's age in years |
| Experience | Work experience in years |
| Income | Annual income in thousands of dollars |
| ZIP Code | Customer's ZIP code |
| Family | Family size (1–4) |
| CCAvg | Average monthly credit card spending ($000s) |
| Education | Education level (1 = Undergraduate, 2 = Graduate, 3 = Advanced/Professional) |
| Mortgage | Mortgage value ($000s); 0 if none |
| Personal Loan | Whether the customer accepted a personal loan (0 = No, 1 = Yes) |
| Securities Account | Has a securities account (0/1) |
| CD Account | Has a CD account (0/1) |
| Online | Uses online banking (0/1) |
| CreditCard | Has a credit card issued by the bank (0/1) |

> **Note:** A realistic sample dataset of 500 records is included. If you have
> the official internship dataset, simply replace `data/personal_loan_data.csv`
> with your file (keeping the same column names) and the project will work
> without any code changes.

---

## Technologies Used

- **Python 3** — programming language
- **Pandas** — data manipulation and analysis
- **NumPy** — numerical computing
- **Matplotlib** — data visualization
- **Seaborn** — statistical data visualization
- **Jupyter Notebook** — interactive analysis environment

---

## Project Structure

```
personal-loan-portfolio-analysis/
│
├── data/
│   └── personal_loan_data.csv          # Dataset (sample or official)
│
├── notebooks/
│   └── Personal_Loan_Portfolio_Analysis.ipynb   # Main analysis notebook
│
├── src/
│   ├── analysis.py                     # Reusable helper functions
│   └── generate_data.py                # Script to generate sample data
│
├── visualizations/                     # Saved chart images (generated)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Cleaning

The following cleaning steps were performed:

1. **Missing values** — checked and handled (none found in the sample dataset).
2. **Duplicate rows** — removed if present.
3. **Data types** — binary columns converted to integer type.
4. **Invalid values** — negative experience values set to 0.
5. **ID column** — dropped (not useful for analysis).
6. **Education labels** — added a readable label column for easier plotting.

The number of rows and columns before and after cleaning is displayed in the
notebook so the effect of cleaning is transparent.

---

## Exploratory Data Analysis

The notebook covers the following analysis sections:

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
14. Executive Summary

---

## Visualizations

The project includes the following charts, all created with Matplotlib and
Seaborn:

1. Age distribution
2. Income distribution
3. CCAvg (credit card spending) distribution
4. Mortgage distribution
5. Education distribution
6. Family-size distribution
7. Personal Loan acceptance count
8. Income vs Personal Loan (box plot + income group bar chart)
9. Education vs Personal Loan
10. Age vs Personal Loan (box plot + age group bar chart)
11. Family size vs Personal Loan
12. CD Account vs Personal Loan
13. Securities Account vs Personal Loan
14. Online banking vs Personal Loan
15. Credit card usage vs Personal Loan
16. Correlation heatmap

Every chart has a meaningful title, proper axis labels, readable legends, and
an appropriate figure size. Charts are also saved as PNG files in the
`visualizations/` folder.

---

## Key Insights

1. **Income is the strongest driver** of personal-loan acceptance. High-income
   customers accept at a significantly higher rate than low-income customers.
2. **Education is positively related** to loan acceptance — advanced/professional
   customers accept more often than undergraduates.
3. **CD account holders** are far more likely to accept a personal loan than
   non-holders.
4. **Securities account holders** also show higher acceptance rates.
5. A **high-value segment** (high income + graduate/advanced education) accepts
   loans at a rate well above average.
6. **Family size** has a modest positive effect — larger families accept slightly
   more often.
7. **Age** has a weak relationship with acceptance; the 30–50 band is slightly
   more receptive.
8. **Online banking users** are reachable through digital marketing channels.
9. **Mortgage holders** show slightly higher acceptance, likely because they
   are already comfortable with bank credit.
10. The **high-value segment** is the prime target for future campaigns.

> Every insight above is calculated from the dataset in the notebook — no
> conclusions are invented.

---

## Business Recommendations

1. **Target the high-value segment** (high income + higher education) first.
2. **Cross-sell to existing deposit customers** (CD account holders).
3. **Use online banking channels** to deliver loan offers efficiently.
4. **Design income-tiered offers** rather than one-size-fits-all loans.
5. **Future improvement:** build a simple machine-learning model to predict
   loan acceptance (optional, beyond the scope of this EDA).

---

## How to Run the Project

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. (Optional) Regenerate the sample dataset

If you want to regenerate the sample data (or change the number of records),
run:

```bash
python src/generate_data.py
```

### 3. Open the Jupyter Notebook

```bash
jupyter notebook notebooks/Personal_Loan_Portfolio_Analysis.ipynb
```

Then run the cells from top to bottom. All charts and insights will be
generated automatically.

### 4. Using your own dataset

Replace `data/personal_loan_data.csv` with your own CSV file that has the same
column names. The notebook and analysis code will work without any changes.

---

## Future Improvements

- **Machine learning model:** Train a logistic regression or decision tree
  model to predict which customers are most likely to accept a personal loan.
  *(Optional — clearly marked as a future step, not part of the current EDA.)*
- **Interactive dashboard:** Build a simple Streamlit or Dash dashboard to let
  business users explore the data interactively.
- **More data:** Incorporate additional features such as loan amount, interest
  rate, and repayment history for deeper analysis.
- **Time-series analysis:** If campaign data over time is available, analyze
  how acceptance rates change across different campaign periods.

---

## How I Explain This Project in an Interview

> "This project is an exploratory data analysis of a personal-loan dataset
> for Apex Credit Union. The bank wanted to understand which customers are most
> likely to accept a personal loan so they can target future campaigns more
> effectively.
>
> I used Python with Pandas, NumPy, Matplotlib, and Seaborn inside a Jupyter
> Notebook. I started by loading and cleaning the data — checking for missing
> values, duplicates, and invalid values like negative experience. Then I
> performed univariate analysis to understand individual variables like age,
> income, and education, followed by bivariate analysis to see how each
> variable relates to loan acceptance.
>
> I also created customer segments based on income, age, education, and family
> size using data-driven thresholds, and built a correlation heatmap to find
> the strongest relationships.
>
> The key insights were that income is the strongest driver of loan acceptance,
> customers with higher education and existing CD or securities accounts are
> more likely to accept loans, and a high-value segment combining high income
> with higher education accepts loans well above the average rate.
>
> These insights can help Apex Credit Union target the right customers, design
> income-tiered loan offers, and use online banking channels to deliver
> campaigns more efficiently."
