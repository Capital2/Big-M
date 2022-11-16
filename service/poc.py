import pandas as pd

def simplex(df: pd.DataFrame) -> pd.DataFrame:
    print("run simplex")
    return df


def main():
    df = pd.read_csv("data.csv")
    print(df)
    simplex(df)


if __name__ == "__main__":
    main()