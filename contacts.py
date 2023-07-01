import streamlit as st

def contact_me():
    st.caption(":red Created by Ian Bravyn Abwoto.")
    with st.expander(":blue[Contact Me]"):
        st.caption("Email: ianbravynsa@gmail.com")
        st.caption("Phone: :blue[+254792744154]")
        st.caption("Share website url")
        st.code("datalogy.streamlit.app")
        name = st.text_input("Name")
        feedback = st.text_input("Write me feedback")

        if name:
            if feedback:
                try:
                    with open("feedback.txt", 'w') as f:
                        data = f"{{'name': {name}, 'feedback': {feedback} }}"
                        f.write(str(data))
                        st.caption(f"Feedback sent successfully!")
                except Exception as e:
                    st.caption("Trouble saving your message,don't fret")        
        