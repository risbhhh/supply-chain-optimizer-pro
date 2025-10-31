import pandas as pd

def load_sales(path='data/sample_sales.csv'):
    return pd.read_csv(path, parse_dates=['date'])

if __name__ == '__main__':
    df = load_sales()
    print(df.head())
