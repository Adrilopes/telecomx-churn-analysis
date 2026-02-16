import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove prefixes from normalized JSON structure
    prefixos = ["customer.", "phone.", "internet.", "account."]
    df.columns = df.columns.str.replace("|".join(prefixos), "", regex=True)

    # Standardize column names (snake_case)
    df.columns = (
    df.columns
        .str.strip()
        .str.replace(".", "_", regex=False)
        .str.lower()
    )

    df = df.rename(columns={"customerid": "customer_id", "d": "customer_id"})

    # Handle empty churn values (column is now 'churn')
    if "churn" in df.columns:
        df["churn"] = df["churn"].replace("", pd.NA)
        df = df[df["churn"].isin(["Yes", "No"])]

    # Converting 'charges_total' to numeric and removing invalid rows
    if "charges_total" in df.columns:
        df["charges_total"] = pd.to_numeric(df["charges_total"], errors="coerce")
        df = df.dropna(subset=["charges_total"])

    # Convert binary Yes/No columns to 1/0
    mapa_binario = {"Yes": 1, "No": 0}

    colunas_yes_no = [
        "churn", "partner", "dependents", "phoneservice",
        "paperlessbilling", "onlinebackup", "deviceprotection",
        "techsupport", "streamingtv", "streamingmovies", 'multiplelines'
    ]

    for col in colunas_yes_no:
        if col in df.columns:
            df[col] = df[col].map(mapa_binario).astype("Int64")

    return df