import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Valuation", page_icon="🤑", layout="wide")


if st.button("🏡Home"):
    switch_page("Home")

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

if st.button("Create Portfolio"):
    st.write("The model will be inserted here; prints list of stocks")


if st.button("Optimize Portfolio"):
    st.write("A table with weights will be ouputted")


"""
Visualisation such as below
"""

col1, col2, col3 = st.columns(3)
col1.metric(label="Return", value=1000, delta=300)
col2.metric(label="Risk", value=200, delta=-20)
col3.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
style_metric_cards()
