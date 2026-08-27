"""
generate_data.py
----------------
Creates a realistic sample personal-loan customer dataset and saves it as
`data/personal_loan_data.csv`.

This script is only needed to produce the demonstration dataset. If you have
the official internship dataset, simply replace the CSV file in the `data/`
folder with your own `personal_loan_data.csv` (keeping the same column names)
and the rest of the project will work without any changes.

Run:
    python src/generate_data.py
"""

import os
import numpy as np
import pandas as pd

# Fix the random seed so the generated dataset is reproducible.
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Number of customer records to generate.
N_CUSTOMERS = 500


def generate_dataset(n_customers: int = N_CUSTOMERS) -> pd.DataFrame:
    """Generate a realistic personal-loan customer dataset.

    The relationships between variables are designed to mimic a real bank's
    loan campaign data. Higher income, higher education and existing banking
    products increase the chance of accepting a personal loan.
    """

    # ---- ID -----------------------------------------------------------
    customer_id = np.arange(1, n_customers + 1)

    # ---- Age ----------------------------------------------------------
    # Most customers are between 25 and 65 years old.
    age = np.random.normal(loc=45, scale=11, size=n_customers).round().astype(int)
    age = np.clip(age, 23, 67)

    # ---- Experience ---------------------------------------------------
    # Experience generally follows age minus ~22 (start of working life).
    experience = (age - 22) - np.random.randint(0, 5, size=n_customers)
    experience = np.clip(experience, 0, None).astype(int)

    # ---- Income (in thousands of dollars per year) --------------------
    # Income is right-skewed, so we use a log-normal distribution.
    income = np.random.lognormal(mean=4.3, sigma=0.35, size=n_customers).round(1)
    income = np.clip(income, 8, 220)

    # ---- ZIP Code -----------------------------------------------------
    # Random 5-digit ZIP codes for demonstration purposes.
    zip_code = np.random.randint(10000, 99999, size=n_customers)

    # ---- Family size --------------------------------------------------
    family = np.random.choice([1, 2, 3, 4], size=n_customers, p=[0.25, 0.30, 0.28, 0.17])

    # ---- CCAvg: average credit-card spending per month ($000s) --------
    # Higher income customers tend to spend more on credit cards.
    ccavg = (income * 0.04 + np.random.normal(0, 0.6, size=n_customers)).round(1)
    ccavg = np.clip(ccavg, 0, 10)

    # ---- Education (1 = Undergraduate, 2 = Graduate, 3 = Advanced) ----
    education = np.random.choice([1, 2, 3], size=n_customers, p=[0.42, 0.30, 0.28])

    # ---- Mortgage (in $000s) ------------------------------------------
    # Most customers have no mortgage; a smaller group has a meaningful value.
    has_mortgage = np.random.choice([0, 1], size=n_customers, p=[0.70, 0.30])
    mortgage_value = np.random.lognormal(mean=4.6, sigma=0.5, size=n_customers).round(0)
    mortgage = np.where(has_mortgage, mortgage_value, 0).astype(int)
    mortgage = np.clip(mortgage, 0, 600)

    # ---- Securities Account -------------------------------------------
    securities_account = np.random.choice([0, 1], size=n_customers, p=[0.90, 0.10])

    # ---- CD Account ---------------------------------------------------
    cd_account = np.random.choice([0, 1], size=n_customers, p=[0.94, 0.06])

    # ---- Online banking -----------------------------------------------
    online = np.random.choice([0, 1], size=n_customers, p=[0.40, 0.60])

    # ---- Credit Card (issued by the bank) -----------------------------
    credit_card = np.random.choice([0, 1], size=n_customers, p=[0.70, 0.30])

    # ---- Personal Loan acceptance -------------------------------------
    # Probability of accepting a loan depends on income, education, CCAvg,
    # CD account and securities account. This creates realistic patterns
    # that the EDA can later discover.
    logit = (
        -3.8
        + 0.025 * (income - 50)
        + 0.35 * (education - 1)
        + 0.20 * ccavg
        + 0.80 * cd_account
        + 0.50 * securities_account
        + 0.30 * (family - 2)
        - 0.01 * (age - 45)
    )
    prob_accept = 1 / (1 + np.exp(-logit))
    personal_loan = (np.random.rand(n_customers) < prob_accept).astype(int)

    # Assemble the DataFrame.
    df = pd.DataFrame(
        {
            "ID": customer_id,
            "Age": age,
            "Experience": experience,
            "Income": income,
            "ZIP Code": zip_code,
            "Family": family,
            "CCAvg": ccavg,
            "Education": education,
            "Mortgage": mortgage,
            "Personal Loan": personal_loan,
            "Securities Account": securities_account,
            "CD Account": cd_account,
            "Online": online,
            "CreditCard": credit_card,
        }
    )

    return df


def main() -> None:
    """Generate the dataset and save it to the data folder."""
    df = generate_dataset()

    # Path to the data folder (relative to this script).
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(data_dir, exist_ok=True)

    output_path = os.path.join(data_dir, "personal_loan_data.csv")
    df.to_csv(output_path, index=False)

    print(f"Dataset created successfully: {output_path}")
    print(f"Rows: {df.shape[0]}  Columns: {df.shape[1]}")
    print(f"Personal Loan acceptance rate: {df['Personal Loan'].mean():.1%}")


if __name__ == "__main__":
    main()
