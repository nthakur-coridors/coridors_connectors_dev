import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# default mode wide
st.set_page_config(layout="wide")
# Sidebar
def example():
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            button:hover {
                background-color: blue;
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
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")
st.sidebar.image("https://via.placeholder.com/150", width=100)  # Placeholder for logo
st.sidebar.title("Coridors Connector")
st.sidebar.button("Create Ingestion")
sb = st.sidebar
with sb:
    example()
st.sidebar.write("---")
st.sidebar.write("Help & Support")
st.sidebar.write("Settings")

# Main Page
st.title("Welcome to Coridors Connector")
st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec neque eleifend, 
    blandit augue vitae, mollis lorem. Fusce euismod tellus vitae turpis ullamcorper, 
    quis hendrerit elit finibus. Nulla facilisi. Ut efficitur leo ut massa gravida, 
    at amet mattis lorem ornare. Phasellus imperdiet, odio non vehicula sodales, 
    dolor risus venenatis erat, vel blandit felis leo ut nisi. Donec rutrum nisi quis 
    turpis convallis, non vestibulum felis euismod.
    """
)

# Supported Connectors
st.subheader("Supported Connectors")
connectors = ["Salesforce", "GitHub", "Freshsales", "Confluence", "HubSpot", "Google Sheets", "Microsoft Ads"]
for connector in connectors:
    st.button(connector)

# Get Started
st.subheader("Let's Get Started!")
st.button("Create New Ingestion")

# Tutorials Section
st.subheader("Tutorials")
st.markdown("[YouTube Video Tutorial](#)")
st.markdown("[Quick Guide to Connector](#)")
st.markdown("[Documentation](#)")
st.markdown("[Walkthrough](#)")

# FAQ Section
st.subheader("FAQ's")
st.markdown("### What is Ingestion?")
st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec neque eleifend, 
    blandit augue vitae, mollis lorem. Fusce euismod tellus vitae turpis ullamcorper, 
    quis hendrerit elit finibus. Nulla facilisi. Ut efficitur leo ut massa gravida, 
    at amet mattis lorem ornare. Phasellus imperdiet, odio non vehicula sodales, 
    dolor risus venenatis erat, vel blandit felis leo ut nisi. Donec rutrum nisi quis 
    turpis convallis, non vestibulum felis euismod.
    """
)
st.markdown("### What is Scheduling?")
st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec neque eleifend, 
    blandit augue vitae, mollis lorem. Fusce euismod tellus vitae turpis ullamcorper, 
    quis hendrerit elit finibus. Nulla facilisi. Ut efficitur leo ut massa gravida, 
    at amet mattis lorem ornare. Phasellus imperdiet, odio non vehicula sodales, 
    dolor risus venenatis erat, vel blandit felis leo ut nisi. Donec rutrum nisi quis 
    turpis convallis, non vestibulum felis euismod.
    """
)
