import streamlit as st
import pandas as pd

from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Optimization", page_icon="⚙️", layout="wide")

if st.button("🏡Home"):
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

main_tab1, main_tab2 = st.tabs(["Stocks", "Industry"])

with main_tab1:
    selected_stocks = st.multiselect("Select stocks:", stocks, placeholder="Select a stock")

    if st.button("Add to List"):
        st.session_state.selection.extend(selected_stocks)

    st.header("Selected Options:")
    st.write("You selected:")
    st.write(", ".join(map(str, st.session_state.selection)))



with main_tab2:
    st.write("You can either select some stocks based on industries or click Diversified Portfolio to get bit from all industries")

    tab1, tab2 = st.tabs(["Selection by Industry", "Diversified Portfolio"])

    with tab1:
        selected_industry = st.selectbox("Select an industry:", industry, placeholder="Select an industry")
        if selected_industry:
            inner_options = stocks_in_industry(selected_industry)

            container = st.container()
            all = st.checkbox("Select all")

            if all:
                selected_stocks = container.multiselect("Select one or more stocks:", inner_options, inner_options,\
                                                                            placeholder="Select a stock", key="stocks")
            else:
                selected_stocks =  container.multiselect("Select one or more stocks:",inner_options,\
                                                                        placeholder="Select a stock", key="stocks")


            if st.button("Add to list", key="tab1"):
                for stock in selected_stocks:
                    if stock not in st.session_state.selection:
                        st.session_state.selection.append(stock)



        st.header("Selected Options:")
        st.write("You selected:")
        st.write(", ".join(map(str, st.session_state.selection)))



        st.write("Double click to clear list:")
        if st.button("Clear List"):
            st.session_state.selection = []

        st.header("Portfolio Amount")
        amount = st.number_input("How much would you like to invest?")
        st.write("You entered", "£",amount)


        st.write("Prediction")
        if st.button("Predict"):
            main_col1, main_col2 = st.columns(2, gap="small")

            with main_col1:
                cols = ["Stock", "Amount"]
                data = pd.read_csv('raw_data/Baseline_weights1.csv', index_col=0, names=cols)

                for index, row in enumerate(data):
                    st.write(round((data[row] * amount)), 2)

            with main_col2:
                col1, col2 = st.columns(2)
                col1.metric(label="Return", value=1000, delta=300)
                col2.metric(label="Drawdown", value=200, delta=-20)

                style_metric_cards()

                col3, col4 = st.columns(2)
                col3.metric(label="Risk", value=200, delta=-20)
                col4.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
                style_metric_cards()





    with tab2:
        inner_options = industry
        multi_industries = st.container()
        select_all = st.checkbox("Select all", key="select_all")

        if select_all:
            selected_industry = multi_industries.multiselect("Select one or more industries:", inner_options, inner_options,\
                                                                                placeholder="Select an industry",\
                                                                                    key="industry_select")
        else:
            selected_industry =  multi_industries.multiselect("Select one or more industries:",inner_options,\
                                                                            placeholder="Select an industry",\
                                                                                key="industry_select")

        if st.button("Get Exposure"):
            st.write("Print stocks for them")
            # append stocks to selection list
            # predict based on this

        if st.button("Add to list", key="tab2"):
            for stock in selected_stocks:
                if stock not in st.session_state.selection:
                    st.session_state.selection.append(stock)



        st.header("Selected Options:")
        st.write("You selected:")
        st.write(", ".join(map(str, st.session_state.selection)))

        st.write("Double click to clear list:")
        if st.button("Clear List"):
            st.session_state.selection = []

        st.header("Portfolio Amount")
        amount = st.number_input("How much would you like to invest?")
        st.write("You entered", "£",amount)


        st.write("Prediction")
        if st.button("Predict"):
            main_col1, main_col2 = st.columns(2, gap="small")

            with main_col1:
                cols = ["Stock", "Amount"]
                data = pd.read_csv('raw_data/Baseline_weights2.csv', index_col=0, names=cols)

                for index, row in enumerate(data):
                    st.write(round((data[row] * amount / 100)), 2)

            with main_col2:
                col1, col2 = st.columns(2)
                col1.metric(label="Return", value=1000, delta=300)
                col2.metric(label="Drawdown", value=200, delta=-20)

                style_metric_cards()

                col3, col4 = st.columns(2)
                col3.metric(label="Risk", value=200, delta=-20)
                col4.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
                style_metric_cards()

# st.write("Double click to clear list:")
# if st.button("Clear List"):
#     st.session_state.selection = []

# st.header("Portfolio Amount")
# amount = st.number_input("How much would you like to invest?")
# st.write("You entered", "£",amount)




# font_css = """
# <style>
# button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
#   font-size: 24px;
# }
# </style>
# """

# st.write(font_css, unsafe_allow_html=True)
# st.write("Prediction")
# if st.button("Predict"):
#     main_col1, main_col2, main_col3, main_col4, main_col5 = st.columns(5, gap="small")

#     with main_col1:
#         cols = ["Stock", "Amount"]
#         data = pd.read_csv('raw_data/Baseline_weights1.csv', index_col=0, header=cols)

#         for index, row in enumerate(data):
#             st.write(round((data[row] * amount) / 100), 2)

#     with main_col2:
#         col1, col2 = st.columns(2)
#         col1.metric(label="Return", value=1000, delta=300)
#         col2.metric(label="Drawdown", value=200, delta=-20)

#         style_metric_cards()

#         col3, col4 = st.columns(2)
#         col3.metric(label="Risk", value=200, delta=-20)
#         col4.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
        # style_metric_cards()








# col1, col2, col3, col4 = st.columns(4)
# col1.metric(label="Return", value=1000, delta=300)
# col2.metric(label="Drawdown", value=200, delta=-20)
# col3.metric(label="Risk", value=200, delta=-20)
# col4.metric(label="Sharpe Ratio", value=3.00, delta=-1.43)
# style_metric_cards()


# 🏡_Home



# if st.session_state.selection == [AAPL, ACN, ADBE, AMD, AVGO, CRM, CSCO, IBM, INTC, MA, MSFT, NVDA, ORCL, PYPL, QCOM, TXN, V]
