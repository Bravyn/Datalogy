import streamlit as st

def contact_me():
    st.caption(":red Created by Ian Bravyn Abwoto.")
    with st.expander(":blue[Contact Me]"):
        st.caption("Email: ianbravynsa@gmail.com")
        st.caption("Phone: :blue[+254792744154]")
        st.caption("Share website url")
        st.code("datalogy.streamlit.app")
        feedback = st.text_input("Send me feedback as sms")
        name = st.text_input("Name")