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

amount = st.number_input("How much would you like to invest?")
st.write("You entered", "£",amount)

# Create a dictionary to store options for the outer and inner select boxes
options = {
    "Industry": industry,
    "Stocks": stocks,
}

st.write("How would you like to invest this?")

# Outer select box to choose a category
selected_category = st.selectbox("Select a category:", options,  key=1)

# Initialize inner select box options
inner_options = []
selection = []


if selected_category == "Industry":
    # Options for the "Industry" category
    selected_industry = st.selectbox("Select an industry:", industry, key=2)

    # Create options for stocks within the selected industry
    if selected_industry:
        inner_options = stocks_in_industry(selected_industry)

    selected_stocks = st.multiselect("Select stocks within the industry:", inner_options)
    if st.button("Add to List"):
        selection.append(selected_stocks)
    st.write(f"You selected the industry: {selected_industry}")
    st.write(f"You selected the stocks: {selection}")



    # Add an option to select stocks from another industry in a loop
    select_another_industry = st.checkbox("Would you like to select from another industry?")

    while select_another_industry:
        selected_industry_2 = st.selectbox("Select another industry:", industry)

        if selected_industry_2:
            inner_options_2 = stocks_in_industry(selected_industry_2)
        selected_stocks_2 = st.multiselect("Select stocks within the other industry:", inner_options_2)

        if st.button("Add to List"):
            selection.append(selected_stocks_2)

        st.write(f"You selected the other industry: {selected_industry_2}")
        st.write(f"You selected the other stocks:", selection)


        # Add a button to exit the loop
        if st.button("End Loop"):
            break

    st.write(f"Your final stock selection is:", selection)


if selected_category == "Stocks":
    # Options for the "Stocks" category
    stocks = stocks
    selected_stocks = st.multiselect("Select stocks:", stocks)
    if st.button("Add to List"):
        selection.append(selected_stocks)


if selection:
    st.header("Selected Options:")
    st.write("You selected:")
    st.write(", ".join(map(str, selected_stocks)))
    st.write("You stated you would like to invest", "£",amount, "in these stocks:", ", ".join(map(str, selected_stocks)))
else:
    st.info("No options selected yet.")

if st.button("Clear List"):
    selected_options = []
