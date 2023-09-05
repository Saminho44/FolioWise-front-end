import streamlit as st
import pandas as pd

from streamlit_extras.metric_cards import style_metric_cards
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


st.write("Let's optimize your stocks!")
st.write("Do you have any stocks in mind or would you like to select according to industries?")

# Initialize selection in session_state if not already initialized
if "selection" not in st.session_state:
    st.session_state.selection = []

tab1, tab2 = st.tabs(["Stocks", "Industry"])

with tab1:
    selected_stocks = st.multiselect("Select stocks:", stocks, placeholder="Select a stock")

    if st.button("Add to List"):
        st.session_state.selection.extend(selected_stocks)

    st.header("Selected Options:")
    st.write("You selected:")
    st.write(", ".join(map(str, st.session_state.selection)))



with tab2:
    selected_industry = st.selectbox("Select an industry:", industry, placeholder="Select an industry")
    if selected_industry:
        inner_options = stocks_in_industry(selected_industry)
        selected_stocks = st.multiselect("Select stocks within the industry:", inner_options, placeholder="Select a stock")
        if st.button("Add to list"):
            for stock in selected_stocks:
                if stock not in st.session_state.selection:
                    st.session_state.selection.append(stock)


        select_another_industry = st.radio("Select stocks from another industry?", ("No", "Yes"))

        while select_another_industry == "Yes":
            selected_industry_2 = st.selectbox("Select another industry:", industry)
            if selected_industry_2:
                inner_options_2 = stocks_in_industry(selected_industry_2)
                selected_stocks_2 = st.multiselect("Select stocks within the other industry:", inner_options_2,\
                                                                                    placeholder="Select a stock")

                if st.button("Add More to List"):
                    for stock in selected_stocks_2:
                        if stock not in st.session_state.selection:
                            st.session_state.selection.append(stock)

            if st.button("End Loop"):
                break


        st.header("Selected Options:")
        st.write("You selected:")
        st.write(", ".join(map(str, st.session_state.selection)))

# font_css = """
# <style>
# button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
#   font-size: 24px;
# }
# </style>
# """

# st.write(font_css, unsafe_allow_html=True)


if st.button("Clear List"):
    st.session_state.selection = []


st.header("Portfolio Amount")
amount = st.number_input("How much would you like to invest?")
st.write("You entered", "£",amount)




col1, col2, col3 = st.columns(3)
col1.metric(label="Return", value=1000, delta=300)
col2.metric(label="Risk", value=200, delta=-20)
col3.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
style_metric_cards()
