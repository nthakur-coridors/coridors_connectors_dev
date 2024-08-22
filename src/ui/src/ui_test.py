import streamlit as st
import streamlit_extras.stylable_container as  stylable_container

# Sidebar
# Add logo to the sidebar
st.markdown(
    """
    <div style="width: 100%; height: 100%; background: #FCFCFC; box-shadow: 0px 4px 4px rgba(153, 153, 153, 0.25)"></div>
    """,
    unsafe_allow_html=True,
)
def sidebar_componects():
    st.header("Coridors Connector")
    l,m,r = st.columns([1,1,1])
    m.markdown(
    """
    <style>
    display: flex;
    width: 128px;
    height: 128px;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    </style>
    """,
    unsafe_allow_html=True
    )
    # m.button("Create Ingestion")
    m.image("logo.png", width=120)

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

with st.sidebar:
    sidebar_componects()

st.sidebar.header("Coridors Connector")
# with st.sidebar:
#     st.markdown(
#         """
#         <div style="text-align: center;">
#             <img src="https://via.placeholder.com/150" alt="Logo" width="150">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

with st.sidebar:
    
    l,m,r = st.columns([1,1,1])
    m.markdown(
    """
    <style>
    display: flex;
    width: 128px;
    height: 128px;
    justify-content: center;
    align-items: center;
    flex-shrink: 0;
    </style>
    """,
    unsafe_allow_html=True
)
    # m.button("Create Ingestion")
    m.image("logo.png", width=120)  # Placeholder for logo
# Main content


with st.sidebar:
    
    l,m,r = st.columns([0.3,1,1])
    m.markdown(
    """
    <style>
    div.stButton > button {
    display: flex;
    width: 224px;
    height: 48px;
    padding: 0px;
    justify-content: center;
    align-items: center;
    gap: 16px;
    flex-shrink: 0;
    color: red;

    }
    </style>
    """,
    unsafe_allow_html=True
)
    # with stylable_container(
    #     key="green_button",
    #     css_styles="""
    #         button {
    #             background-color: green;
    #             color: white;
    #             border-radius: 20px;
    #         }
    #         """,
    # ):
    st.button("Green button")
# l,m,r = st.columns([1,3,1])
#     m.markdown(
#         """
#         <style>
#         .custom-button {
#             background-color: blue;
#             color: white;
#             padding: 10px 25px;
#             border: none;
#             border-radius: 5px;
#             font-size: 16px;
#             cursor: pointer;
#         }

#         .custom-button:hover {
#             background-color: darkblue;
#         }
#         </style>
#         <button class="custom-button">Create Ingestion</button>
#         """,
#         unsafe_allow_html=True
#     )

#     # Optionally, handle the button click event using JavaScript
#     if st.button("Create Ingestion"):
#         st.write("Button Clicked!")


    # m.button(":blue-background[Create Ingestion]")
# st.sidebar.button("Create Ingestion")
with st.sidebar:
    st.markdown(
        """
        <div style="width: 100%; height: 100%; padding: 10px; background: #0062F6; border-radius: 10px; overflow: hidden; justify-content: center; align-items: center; gap: 16px; display: inline-flex">
        <div style="color: green; font-size: 18px; font-family: Source Sans Pro; font-weight: 600; line-height: 24px; word-wrap: break-word">Create Ingestion</div>
        </div>

    """,
    unsafe_allow_html=True 
    )
    st.button("Create Ingestion2")

st.sidebar.write("---")
st.sidebar.write("Help & Support")
st.sidebar.write("Settings")
st.logo('logo.png')

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
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

# Supported Connectors
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #ADD8E6;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Use a container to wrap the content
with st.container():
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
