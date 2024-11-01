import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def example():
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        st.button("Green button")

    st.button("Normal button")

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px);
                color: blue;
                background-color: green;
            }
            """,
    ):
        st.markdown("This is a container with a border.")

with st.sidebar:
    example()