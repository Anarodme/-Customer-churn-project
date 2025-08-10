import pandas as pd

def extract():
    df = pd.read_csv("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    return df

def transform(df):
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()
    df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})
    df = df.drop(columns=['customerID'])
    return df

def load(df):
    df.to_csv("data/processed/customer_churn_clean.csv", index=False)

if __name__ == "__main__":
    df_raw = extract()
    df_clean = transform(df_raw)
    load(df_clean)
    print("ETL finalizado.")
