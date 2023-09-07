import streamlit as st
import pandas as pd
import os
import time
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(page_title="Valuation", page_icon="🤑", layout="wide")


if st.button("🏡Home"):
    switch_page("Home")
csv_path = os.path.join(os.getcwd())

# functions
def industry():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv(os.path.join(csv_path,"snp100.csv"), names=col_names, skiprows=[33, 54, 79])

    return list(data["Industry"].unique())

industry = industry()


def stocks():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv(os.path.join(csv_path,"snp100.csv"), names=col_names, skiprows=[33, 54, 79])

    return list(data["Stock"])

stocks = stocks()

def stocks_in_industry(i):
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv(os.path.join(csv_path,"snp100.csv"), names=col_names, skiprows=[33, 54, 79])
    res = data[data["Industry"] == i]

    return list(res["Stock"])

amount = st.number_input("How much would you like to invest?")
st.write("You entered", "£",amount)

if st.button("Create Portfolio"):
    with st.spinner(text='In progress'):
                time.sleep(3)
                st.success('Done')
    portfolio = ["Advanced Micro Devices", "Apple", "Berkshire Hathaway", "Boeing Company", "Broadcom Limited",\
        "Caterpillar", "Cisco Systems", "Eli Lily and Company", "FedEx Corporation", "Netflix", "Oracle Corporation",\
            "Visa Inc", "Walmart Inc"]
    st.write("What do you think of these?")
    st.write(", ".join(map(str, portfolio)))


if st.button("Optimize Portfolio"):
    with st.spinner(text='In progress'):
                time.sleep(3)
                st.success('Done')
    main_col1, main_col2 = st.columns(2, gap="small")

    with main_col1:
        cols = ["Stock", "Amount"]
        data = pd.read_csv(os.path.join(csv_path,"raw_data","DeepDow_weights3.csv"), index_col=0, names=cols)

        for index, row in enumerate(data):
            st.write(round((data[row] * amount / 100)), 2)

    with main_col2:
        col1, col2 = st.columns(2)
        col1.metric(label="Return", value="+35.44%")
        col2.metric(label="Drawdown", value="-1.37%")

        style_metric_cards()

        col3, col4 = st.columns(2)
        col3.metric(label="Volatility", value="12.28%")
        col4.metric(label="Sharpe Ratio", value=3.43)
        style_metric_cards()

    st.image("images/DeepDow_portfolio3.jpg")
