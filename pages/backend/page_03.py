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


# Create a dictionary to store options for the outer and inner select boxes
options = {
    "Industry": industry,
    "Stocks": stocks,
}

# Create an empty list to store selected options
selected_options = []

# Streamlit app header
st.title("Nested Select Boxes")

# Streamlit widget for the outer select box
selected_category = st.selectbox("Select a category:", list(options.keys()))

# Get the options for the inner select box based on the selected category
selected_options = options[selected_category]

# Streamlit widget for the inner select box
# Streamlit widget to select options
selected_option = st.multiselect("Select an option:", selected_options)


# Streamlit button to add selected option to the list
if st.button("Add to List"):
    selected_options.append(selected_option)

# Streamlit widget to display the list
# Streamlit widget to display the list horizontally
if selected_options:
    st.header("Selected Options:")
    st.write("You selected:")
    st.write(", ".join(map(str, selected_option)))
else:
    st.info("No options selected yet.")

# Streamlit button to clear the list
if st.button("Clear List"):
    selected_options = []

# Streamlit app footer
st.sidebar.text("Streamlit Example")
