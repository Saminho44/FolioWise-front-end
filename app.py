import streamlit as st
import pandas as pd
import os
import time

from PIL import Image

from streamlit_extras.metric_cards import style_metric_cards
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Home", page_icon="🏡", layout="wide")

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo
my_logo = add_logo(logo_path="images/FolioWise_logo.png", width=200, height=200)


col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write(' ')
with col2:
    st.write(' ')
with col3:
    st.image(my_logo)
with col4:
    st.write(' ')
with col5:
    st.write(' ')



selected = option_menu(
        menu_title=None,
        options=["Home", "Optimization", "Validation", "About"],
        icons=["house", "gear", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )



if selected == "Home":
    st.markdown("<h1 style='text-align: center; color: black;'>Welcome to FolioWise</h1>", unsafe_allow_html=True)

    st.markdown("We are so glad you stopped by!")


    """
    🚀 Welcome to FolioWise - Where Your Portfolio Soars to New Heights! 📈

    🌟 Are you ready to embark on an exhilarating journey into the world of investment?\
        Look no further! FolioWise is here to revolutionize your stock portfolio and maximize your returns. 🌟

    📊 Our Mission 📊
    At FolioWise, we're on a mission to empower investors like you to make informed decisions and achieve financial success.\
        We believe that investing should be accessible, exciting, and profitable for everyone, from beginners to seasoned pros.

    💼 What We Offer 💼
    🌐 Cutting-Edge Technology: Our state-of-the-art portfolio optimization algorithms are designed to supercharge your investments.\
        Say goodbye to guesswork and hello to data-driven insights!

    🌐 Your Success, Our Priority 🌐
    Your financial goals are our top priority. Whether you're planning for retirement, saving for a dream vacation,\
        or simply looking to grow your wealth, we've got the tools and expertise to make it happen. With FolioWise\
            by your side, you're not just investing – you're investing smart!

    👉 Get Started Now! 👈

    """



if selected == "Optimization":
    st.header('Optimization', divider='rainbow')
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
                    stock_names = ["Visa Inc", "Texas Instruments Incorporated", "QUALCOMM Incorporated", "PayPal Holdings",\
                        "Oracle Corporation","NVIDIA Corporation", "Microsoft", "Mastercard", "Intel Corporation",\
                            "International Business Machines Corporation", "Cisco Systems", "Salesforce", "Broadcom Limited",\
                                "Advanced Micro Devices", "Adobe Systems Incorporated", "Accenture", "Apple"]
                    st.write(", ".join(map(str, stock_names)))


            st.write("Double click to clear list:")
            if st.button("Clear List"):
                st.session_state.selection = []

            st.header("Portfolio Amount")
            amount = st.number_input("How much would you like to invest?", key="portfolio1")
            st.write("You entered", "£",amount)


            st.write("Prediction")
            if st.button("Predict", key="portfolio11"):
                with st.spinner(text='In progress'):
                    time.sleep(3)
                    st.success('Done')
                main_col1, main_col2 = st.columns(2, gap="small")

                with main_col1:
                    cols = ["Stock", "Amount"]
                    data = pd.read_csv(os.path.join(csv_path,"raw_data","DeepDow_weights1.csv"), index_col=0, names=cols)

                    for index, row in enumerate(data):
                        st.write(round((data[row] * amount/100)), 2)

                with main_col2:
                    col1, col2 = st.columns(2)
                    col1.metric(label="Return", value="+53.35%")
                    col2.metric(label="Drawdown", value="-1.78%")

                    style_metric_cards()

                    col3, col4 = st.columns(2)
                    col3.metric(label="Volatility", value="24.98%")
                    col4.metric(label="Sharpe Ratio", value=2.54)
                    style_metric_cards()

                st.image("images/DeepDow_portfolio1.png")


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
            with st.spinner(text='In progress'):
                time.sleep(3)
                st.success('Done')
            st.write("Diversified stocks:")
            st.session_state.selection = ["Apple", "Adobe", "Abbolt", "Bristol Myers", "Capital One", "Goldman Sachs",\
                "Simon Property", "American Tower", "Philip Morris", "Heinz Company", "Duke Energy", "NextEra Energy",\
                    "Netflix", "AT&T", "Exxon Mobil", "ConocoPhillips", "Emerson Electric Company", "Lowes Companies", "McDonalds"]
            st.write(", ".join(map(str, st.session_state.selection)))


        if st.button("Add to list", key="tab2"):
            for stock in selected_stocks:
                if stock not in st.session_state.selection:
                    st.session_state.selection.append(stock)


        st.header("Selected Options:")
        st.write("You selected:")
        st.write(", ".join(map(str, st.session_state.selection)))

        st.write("Double click to clear list:")
        if st.button("Clear List", key="industry"):
            st.session_state.selection = []

        st.header("Portfolio Amount")
        amount = st.number_input("How much would you like to invest?")
        st.write("You entered", "£",amount)


        st.write("Prediction")
        if st.button("Predict", key="portfolio2"):
            with st.spinner(text='In progress'):
                time.sleep(3)
                st.success('Done')
            main_col1, main_col2 = st.columns(2, gap="small")


            with main_col1:
                cols = ["Stock", "Amount"]
                data = pd.read_csv(os.path.join(csv_path,"raw_data","DeepDow_weights2.csv"), index_col=0, names=cols)

                for index, row in enumerate(data):
                    st.write(round((data[row] * amount / 100)), 2)

            with main_col2:
                col1, col2 = st.columns(2)
                col1.metric(label="Return", value="+12.49")
                col2.metric(label="Drawdown", value="-8.62%")

                style_metric_cards()

                col3, col4 = st.columns(2)
                col3.metric(label="Volatility", value="19.04%")
                col4.metric(label="Sharpe Ratio", value=0.76)
                style_metric_cards()

            st.image("images/DeepDow_portfolio2.png")


if selected == "Validation":
    st.header('Validation', divider='rainbow')
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



if selected == "About":
    st.markdown("<h1 style='text-align: center; color: black;'>Meet the founders!</h1>", unsafe_allow_html=True)
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    st.write("   ")
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/Sam.png", caption="Sam", use_column_width=False)


        st.image("images/Maalya.png", caption="Maalya", use_column_width=False)


    with col2:
        st.image("images/Dimitri.png", caption="Dimitri", use_column_width=False)


        st.image("images/Minerva.png", caption="Minerva", use_column_width=False)
