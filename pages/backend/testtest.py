import streamlit as st
import pandas as pd


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


# Initialize selection in session_state if not already initialized
if "selection" not in st.session_state:
    st.session_state.selection = []

st.write("Let's optimize your stocks")
st.write("Do you have any stocks in mind or would you like to select according to industries?")

# col1, col2 = st.columns(2)

# with col1:
#     button1 = st.button("Stocks")

# with col2:
#     button2 = st.button("Industry")

button1 = st.button("Stocks")


if button1:
    selected_stocks = st.multiselect("Select stocks:", stocks)

    if st.button("Add to List"):
        st.session_state.selection.extend(selected_stocks)

button2 = st.button("Industry")




if button2:
    selected_stocks = st.multiselect("Select stocks:", stocks)

    if st.button("Add to List"):
        st.session_state.selection.extend(selected_stocks)


if st.button("Final List"):
    st.session_state.selection.extend(selected_stocks)
