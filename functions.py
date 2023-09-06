import pandas as pd

def industry():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names)

    return list(data["Industry"].unique())


def hello():
    return "hello"


# def stocks_in_industry(stocks):
#     for stocks in industry:

#     return
