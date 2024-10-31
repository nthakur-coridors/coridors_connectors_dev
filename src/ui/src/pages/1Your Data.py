import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# from streamlit_elements import elements, mui
from sidebar_styles import styles

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    # st.logo("../resources/logo.png")
    brn = st.button("Click me")
    if brn:
        st.session_state.nav = "home"
        st.session_state.page_nav = "page2"

        st.page_link("Home.py", label="your_connections")
    styles()