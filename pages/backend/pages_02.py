import streamlit as st
import pandas as pd

def stocks():
    col_names = ["Stock", "Industry"]
    data  = pd.read_csv("snp100.csv", names=col_names)

    return list(data["Stock"])

sample = stocks()


# Create an empty list to store selected options
selected_options = []

# Streamlit app header
st.title("Selected Options List")

# Streamlit widget to select options
selected_option = st.multiselect("Select an option:", sample)

# Streamlit button to add selected option to the list
if st.button("Add to List"):
    selected_options.append(selected_option)

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

# Streamlit app footer
st.sidebar.text("Streamlit Example")
