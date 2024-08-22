import streamlit as st
from streamlit_extras.stylable_container import stylable_container

def sidebar_components():
    # Apply custom CSS to the sidebar content
    st.markdown(
        """
        <style>
        /* Adjust the sidebar width and apply custom styles */
        [data-testid="stSidebar"] {
            background-color: green;  /* Set sidebar background color */
            width: 20px;
            height: 934px;
            flex-shrink: 0;
        }

        [data-testid="stSidebar"] > div:first-child {
            padding: 20px;
        }

        /* Ensure text inside the sidebar is white */
        [data-testid="stSidebar"] > div > div {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Supported Connectors")

st.write("Main content area") 

# Render the sidebar components
with st.sidebar:
    sidebar_components()
