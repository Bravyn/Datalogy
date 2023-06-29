import streamlit as st
from analogies import analogies
from data_fuels_science import data_fuel
from data_cleaning import data_cleaning
from styles import format_list_with_css, format_title,format_subtitle, colors

format_title("DATALOGY", colors["royal_blue"])
st.caption(":red Created by Ian Bravyn Abwoto.")
with st.expander(":blue[Contact Me]"):
    st.caption("Email: ianbravynsa@gmail.com")
    st.caption("Phone: :blue[+254792744154]")
    st.caption("Share website url")
    st.code("datalogy.streamlit.app")
    feedback = st.text_input("Send me feedback as sms")
    name = st.text_input("Name")

format_subtitle("Learn Data Science by Analogy.", colors["navy_blue"])

def show_analogies(analogies = analogies):
    more = ":blue[...**Learn More**]"
    for index, analogy in enumerate(analogies):
        st.caption(f"Analogy: {index + 1}")
        format_list_with_css([analogy])
        if index == 0:
            with st.expander(f"{data_fuel[:44]}{more}"):
                st.success(data_fuel)
        if index == 1:
            with st.expander(f"{data_cleaning[:44]}{more}"):
                data = data_cleaning.split('\n')
                format_list_with_css(data)

show_analogies()