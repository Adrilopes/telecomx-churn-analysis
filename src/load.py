from extract import extract_data
from transform import transform_data

def load_data():
    df = extract_data()
    df = transform_data(df)

    df.to_csv("data/processed/churn_tratado.csv", index=False)

    print("Dataset processado salvo com sucesso.")

if __name__ == "__main__":
    load_data()