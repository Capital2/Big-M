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
    # x = float('inf') +5
    # y = float('inf') +100000000

    # if y > x:
    #     print("yap")
    # else:
    #     print("9ad 9ad")