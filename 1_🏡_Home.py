import streamlit as st
import pandas as pd
import numpy as np

from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo


st.set_page_config(page_title="Home", page_icon="🏡", layout="wide")

# add_logo("logo.jpeg", height=20)

# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu",
#         options=["Home", "Optimization", "Validation"]
#     )

# if selected == "Optimization":
#     switch_page("Optimization")





st.markdown("""
# Welcome to FolioWise
""")

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

col1, col2 = st.columns(2)

with col1:
    if st.button("⚙️Optimize"):
        switch_page("Optimization")
with col2:
    if st.button("🤑Exposure"):
        switch_page("Valuation")







# make a package / functions.py
# submit for portfolio; no rel
# le wagon website ; lecture friday
