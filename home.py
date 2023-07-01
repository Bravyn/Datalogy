import streamlit as st
from analogies import analogies
from data_fuels_science import data_fuel
from data_cleaning import data_cleaning
from data_alchemists import data_alchemy
from styles import format_list_with_css, format_title,format_subtitle, colors
from contacts import contact_me

format_title("DATALOGY", colors["steel_blue"])
contact_me()
format_subtitle("Learn Data Science by Analogy.", colors["dark_purple"])

def show_analogies(analogies = analogies):
    more = ":blue[...**Learn More**]"
    for index, analogy in enumerate(analogies):
        st.caption(f"**Analogy:** {index + 1} :white_check_mark:")
        format_list_with_css([analogy], card_type="analogy",color=colors['navy_blue'])
        
        if index == 0:
            with st.expander(f"{data_fuel[:44]}{more}"):
                format_list_with_css(data_fuel.split("\n"))
        
        if index == 1:
            with st.expander(f"{data_cleaning[:44]}{more}"):
                data = data_cleaning.split('\n')
                format_list_with_css(data)
        
        if index == 2:
            with st.expander(f"{data_alchemy[:44]}{more}"):
                data = data_alchemy.split('\n')
                format_list_with_css(data)
show_analogies()