import streamlit as st
import pandas as pd

from streamlit_extras.switch_page_button import switch_page


if st.button("Home"):
    switch_page("app")

# functions
def industry():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])

    return list(data["Industry"].unique())

industry = industry()


def stocks():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])

    return list(data["Stock"])

stocks = stocks()

def stocks_in_industry(i):
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])
    res = data[data["Industry"] == i]

    return list(res["Stock"])

amount = st.number_input("How much would you like to invest?")
st.write("You entered", "£",amount)
st.write("You can invest them in these stocks")
