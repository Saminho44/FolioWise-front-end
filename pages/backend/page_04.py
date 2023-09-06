import requests
import streamlit as st
import numpy as np
import pandas as pd

from functions import hello

st.set_page_config(page_title="Hello", page_icon="👋")

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

# Create a dictionary to store options for the outer and inner select boxes
options = {
    "Industry": industry,
    "Stocks": stocks,
}

# Create an empty list to store selected options
selected_options = []


# Outer select box to choose a category
selected_category = st.selectbox("Select a category:", options)

# Initialize inner select box options
inner_options = []

if selected_category == "Industry":
    # Options for the "Industry" category
    inner_options = industry
elif selected_category == "Stocks":
    # Options for the "Stocks" category
    inner_options = stocks


sec_options = ["Cat", "Goat", "Dog"]

# Display the inner select box if the user selects "Industry"
if selected_category == "Industry":
    display_inner_select = st.checkbox("Show inner select box")
    if display_inner_select:
        selected_industry = st.selectbox("Select an industry:", inner_options)
        st.write(f"You selected the industry: {selected_industry}")
        display_inner_select = st.checkbox("Show inner select box")
        if display_inner_select:
            selected_ind_stock = st.multiselect("Select a stock:", sec_options)

elif selected_category == "Stocks":
    display_inner_select = st.checkbox("Show inner select box")
    if display_inner_select:
        selected_stock = st.multiselect("Select a stock:", inner_options)
        # st.write(f"You selected the stocks: {selected_stock}")


# Streamlit button to add selected option to the list
if st.button("Add to List"):
    selected_options.append(selected_stock)

# Streamlit widget to display the list
# Streamlit widget to display the list horizontally
if selected_options:
    st.header("Selected Options:")
    st.write("You selected:")
    st.write(", ".join(map(str, selected_options)))
else:
    st.info("No options selected yet.")

# Streamlit button to clear the list
if st.button("Clear List"):
    selected_options = []
