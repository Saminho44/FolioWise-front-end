import streamlit as st
import pandas as pd

# functions
def industry():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])

    return list(data["Industry"].unique())

def stocks():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])

    return list(data["Stock"])

def stocks_in_industry(i):
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names, skiprows=[33, 54, 79])
    res = data[data["Industry"] == i]

    return list(res["Stock"])

amount = st.number_input("How much would you like to invest?")
st.write("You entered", "£", amount)

# Create a dictionary to store options for the outer and inner select boxes
options = {
    "Industry": industry(),
    "Stocks": stocks(),
}

st.write("How would you like to invest this?")
selected_category = st.selectbox("Select a category:", options)

# Initialize selection in session_state if not already initialized
if "selection" not in st.session_state:
    st.session_state.selection = []

if selected_category == "Industry":
    selected_industry = st.selectbox("Select an industry:", options["Industry"])
    if selected_industry:
        inner_options = stocks_in_industry(selected_industry)
        selected_stocks = st.multiselect("Select stocks within the industry:", inner_options)
        if st.button("Add to List"):
            for stock in selected_stocks:
                if stock not in st.session_state.selection:
                    st.session_state.selection.append(stock)
        st.write(f"You selected the industry: {selected_industry}")
        st.write("You selected the stocks:", ", ".join(map(str, selected_stocks)))

        select_another_industry = st.radio("Select stocks from another industry?", ("No", "Yes"))

        while select_another_industry == "Yes":
            selected_industry_2 = st.selectbox("Select another industry:", options["Industry"])
            if selected_industry_2:
                inner_options_2 = stocks_in_industry(selected_industry_2)
                selected_stocks_2 = st.multiselect("Select stocks within the other industry:", inner_options_2)

                if st.button("Add More to List"):
                    for stock in selected_stocks_2:
                        if stock not in st.session_state.selection:
                            st.session_state.selection.append(stock)

                st.write(f"You selected the other industry: {selected_industry_2}")
                st.write(f"You selected the other stocks: {selected_stocks_2}")

            if st.button("End Loop"):
                break

    st.write("Your final stock selection is:", ", ".join(map(str, st.session_state.selection)))

if selected_category == "Stocks":
    selected_stocks = st.multiselect("Select stocks:", options["Stocks"])
    if st.button("Add to List"):
        for stock in selected_stocks:
            if stock not in st.session_state.selection:
                st.session_state.selection.append(stock)

if st.session_state.selection:
    st.write("You stated you would like to invest", "£", amount, "in these stocks:", ", ".join(map(str, st.session_state.selection)))

if st.button("Clear List"):
    st.session_state.selection = []
