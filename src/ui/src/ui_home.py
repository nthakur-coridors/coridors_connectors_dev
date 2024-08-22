import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_elements import elements, mui


st.set_page_config(layout="wide")
# def sidebar_header():
#     # st.markdown(
#     #     """
#     #     <style>
#     #     /* Adjust the sidebar width and apply custom styles */
#     #     [data-testid="stSidebarHeader"] {
#     #         <h2>Sidebar Header</h2>
            
#     #     }
#     #     </style>
#     #     """,
#     #     unsafe_allow_html=True
#     # )
#     # st.markdown("<h2>Sidebar Header</h2>", unsafe_allow_html=True)
#     html_content = """
#     <div data-testid="stSidebarHeader">
#         <div style="color: green;">
#             <h2>test</h2>
#         </div>
#     </div>
#     """

#     # Display the custom HTML in the sidebar
#     st.html(html_content)


def sidebar_components():
    l,m,r = st.columns([0.7,1,1])
    with m:
        with stylable_container(
            key="st_side_main_logo",
            css_styles="""
                img {
                    display: flex;
                    position: static;
                    width: 128px;
                    height: 128px;
                    flex-shrink: 0;
                }
                """
        ):
            st.image("./resources/logo.svg", width=120)
    # st.image("./logo.png", width=120)
    # l,m,r = st.columns([0.2,1,1])
    # with m:     
    #     with stylable_container(
    #         key="btn_create_ingestion",
    #         css_styles="""
    #             # div.stButton > button{
    #             #     display: flex;
    #             #     # width:  224px;
    #             #     width: 17rem;
    #             #     # height: 48px;
    #             #     height: 42px;
    #             #     # padding: 10px;
    #             #     justify-content: center;
    #             #     align-items: center;
    #             #     gap: 16px;
    #             #     flex-shrink: 0;
    #             #     # color: rgb(#000);
    #             #     # background-color: blue;
    #             #     # left: 50px;
    #             #     left: -1.5rem;
    #             #     border-radius: 10px;
    #             #     background: var(--Blue---button, #0062F6);
    #             #     position: relative;
    #             #     top: 40px;
    #             # }
    #             # div.stButton > button:hover {
    #             #     background: transparent;
    #             #     background-color: green; /* color on hover */
    #             # }
    #             div.stButton > button {
    #                 display: inherit;
    #                 position: inherit;
    #                 background-color: #0062F6;
    #                 color: white;
    #                 border-radius: 5px;
    #                 # border: none;
    #                 # display: flex;
    #                 # width: 17rem;
    #                 # height: 42px;
    #                 # justify-content: center;
    #                 # align-items: center;
    #                 # gap: 16px;
    #                 # flex-shrink: 0;
    #                 # border-radius: 10px;
    #                 # position: relative;
    #                 # top: 40px;
    #                 # left: -1.5rem;
    #                 display: flex;
    #                 width: 224px;
    #                 height: 48px;
    #                 padding: 10px;
    #                 justify-content: center;
    #                 align-items: center;
    #                 gap: 16px;
    #                 flex-shrink: 0;
    #                 # position: relative;
    #                 # left: -50px 
    #             }
    #             # div.stButton > button:hover {
    #             #     background-color: darkblue;
    #             #     color: white;
    #             # }
    #             """,
    #     ):
    #         m.button("Create Ingestion")
    l,m,r = st.columns([0.1,3,0.1])
    with m:
        with elements("sidebar_ingestion_btn"):
            # Create the first button with red color
            mui.Button(
                "Create Ingestion",
                target="_blank",
                size="small",
                variant="contained",
                startIcon=mui.icon.add_box,  # Correct usage for the startIcon
                style={"display": "flex","color": "white", "background": "#0062F6", "width": "224px", "border-radius": "5px", "height": "48px", "padding": "10px", "justify-content": "center", "align-items": "center", "font-family": "sans-serif", "font-size": "12px", "font-style": "normal", "font-weight": "600", "line-height": "24px"},  # Set width to 200px
                href="#"
            )

    # st.button("Normal button")
# def sidebar_components1():
#     with stylable_container(
#         key="btn_ingestion",
#         css_styles="""
#             div.stButton > button{
#                 display: flex;
#                 position: relative;
#                 top: 80px;
#                 left: -23px;
#                 width: 116%;
#                 height: 48px;
#                 # padding: 8px 0px;
#                 align-items: center;
#                 gap: 16px;
#                 flex-shrink: 0;
#                 # justify-content: center;
#                 # align-items: center;
#                 # gap: 16px;
#                 # flex-shrink: 0;
#                 color: black;
#                 # # background-color: blue;
#                 # # left: 50px;
#                 # left: -25px;
#                 border-radius: 0px;
#                 background: var(--Blue---selected, #CBE0FF);
#                 border-left: 10px solid blue;    
#             }
#             div.stButton > button:hover {
#                 background-color: darkblue;
#                 color: white;
#             }
#             # div.stButton > button {
#             #     background-color: lightblue;
#             #     color: white;
#             #     border-radius: 5px;
#             #     border: none;
#             #     padding-left: 10px;
#             #     transition: all 0.3s ease;
#             # }
#             # div.stButton > button:hover {
#             #     background-color: grey;
#             #     border-left: 10px solid blue;
#             #     padding-left: 20px;  /* Adjust padding to account for the added border */
#             # }
#             """,
#         ):
#             st.button("Ingestion")




with st.sidebar:
    # st.button("normal button")
    # st.logo("./logo.png")
    # sidebar_header()
    # st.header("Coridors Connector")
    sidebar_components()
    # sidebar_components1()

ingestion = st.Page(
    "app_pages/ingestion.py", title="Ingestion", icon=":material/stream:", default=True
)
cost_n_billing = st.Page("app_pages/cost_n_billing.py", title="Cost & Billing", icon=":material/credit_card:")
connected_resources = st.Page(
    "app_pages/connected_resources.py", title="Connected Resources", icon=":material/cloud_sync:"
)
help_n_suppport = st.Page(
    "app_pages/help_n_support.py", title="Help & Suppport", icon=":material/contact_support:"
)
settings = st.Page(
    "app_pages/settings.py", title="Settings", icon=":material/settings:"
)

# search = st.Page("tools/search.py", title="Search", icon=":material/search:")
# history = st.Page("tools/history.py", title="History", icon=":material/history:")

pg = st.navigation([ingestion, cost_n_billing, connected_resources, help_n_suppport, settings])

# nav2 = st.navigation([history, search])

st.markdown(
    """
    <style>
    ul{
        # border-bottom: 200px;
        display: flex;
        flex-direction: column;
        min-height: 60vh;
        position: absolute;
        top: 300px;
    }
    li {
        # display: flex;
        justify-content: space-around;
        # background-color: green;
        padding: 8px 0px 8px 0px;
        margin: 0;
    }
    li > div{
        background-color: #D9D9D9;
        # border-left: 5px solid blue;
    }
    li > div:hover{
        background-color: #CBE0FF;
        border-left: 5px solid blue;
        color: white;
    }
    li > div b:visited{
        background-color: #CBE0FF;
        border-left: 5px solid blue;
        color: white;
    }
    li a{
        display: flex;
        position: relative;
        margin : 0;
        # top: 80px;
        left: -24px;
        width: 336px;
        height: 48px;
        padding: 8px 0px;
        align-items: center;
        gap: 16px;
        flex-shrink: 0;
        # justify-content: center;
        # align-items: center;
        # gap: 16px;
        # flex-shrink: 0;
        color: black;
        # background-color: blue;
        # # left: 50px;
        # left: -25px;
        # border-radius:100px;
        background: orange;
        # border-left: 5px solid blue;
    }
    li > a:hover {
        background-color: darkblue;
        # border-left: 10px solid blue;
        color: white;
    }
    # li a:visited{
    #     background-color: #CBE0FF;
    #     border-left: 5px solid blue;
    #     color: white;;
    # }
    li a:visited {
        background-color: #CBE0FF;
        border-left: 5px solid blue;
        color: white;
    }
    li:nth-child(3) {
        margin-bottom: 200px;
    }
    
    div[data-testid="stSidebarNavSeparator"]{
        display: flex;
        position: absolute;
        # display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
pg.run()

# sb = st.sidebar


# def sidebar_components1():
#     with stylable_container(
#         key="btn_footer",
#         css_styles="""
#             div.stButton > button{
#                 display: inline_block;
#                 width: 336px;
#                 height: 48px;
#                 padding: 8px 0px 8px 10px;
#                 align-items: center;
#                 gap: 16px;
#                 flex-shrink: 0;
#                 # display: flex;
#                 position: relative;
#                 top: 500px;
#                 left: -24px;
#                 # width: 116%;
#                 # height: 47px;
#                 # padding: 8px 0px;
#                 # align-items: center;
#                 # gap: 16px;
#                 # flex-shrink: 0;
#                 # justify-content: center;
#                 # align-items: center;
#                 # gap: 16px;
#                 # flex-shrink: 0;
#                 color: black;
#                 # # background-color: blue;
#                 # # left: 50px;
#                 # left: -25px;
#                 border-radius: 0px;
#                 background:#D9D9D9;   
#             }
#             div.stButton > button:hover {
#                 background-color: darkblue;
#                 color: white;
#             }
#             # div.stButton > button {
#             #     background-color: lightblue;
#             #     color: white;
#             #     border-radius: 5px;
#             #     border: none;
#             #     padding-left: 10px;
#             #     transition: all 0.3s ease;
#             # }
#             # div.stButton > button:hover {
#             #     background-color: grey;
#             #     border-left: 10px solid blue;
#             #     padding-left: 20px;  /* Adjust padding to account for the added border */
#             # }
#             # div[data-testid="stVerticalBlockBorderWrapper"]{
#             #     display: block;
#             #     position: absolute;
#             #     top: 75vh;
#             }
#             """,
#         ):
#             st.button("Ingestion")
#             st.button('setiings')

# with st.sidebar:
#     # st.button("normal button")
#     # st.logo("./logo.png")
#     # sidebar_header()
#     # st.header("Coridors Connector")
#     # sidebar_components()
#     sidebar_components1()



# main body
# l,m,r = st.columns([0.2,1,1])
# with m:     
# with stylable_container(
#     key="btn_data_source",
#     css_styles="""
#         # div.stButton > button{
#         #     display: flex;
#         #     # width:  224px;
#         #     width: 17rem;
#         #     # height: 48px;
#         #     height: 42px;
#         #     # padding: 10px;
#         #     justify-content: center;
#         #     align-items: center;
#         #     gap: 16px;
#         #     flex-shrink: 0;
#         #     # color: rgb(#000);
#         #     # background-color: blue;
#         #     # left: 50px;
#         #     left: -1.5rem;
#         #     border-radius: 10px;
#         #     background: var(--Blue---button, #0062F6);
#         #     position: relative;
#         #     top: 40px;
#         # }
#         # div.stButton > button:hover {
#         #     background: transparent;
#         #     background-color: green; /* color on hover */
#         # }
#         div.stButton > button {
#             display: inherit;
#             position: inherit;
#             background-color: #0062F6;
#             color: white;
#             border-radius: 5px;
#             # border: none;
#             # display: flex;
#             # width: 17rem;
#             # height: 42px;
#             # justify-content: center;
#             # align-items: center;
#             # gap: 16px;
#             # flex-shrink: 0;
#             # border-radius: 10px;
#             # position: relative;
#             # top: 40px;
#             # left: -1.5rem;
#             display: flex;
#             width: auto;
#             height: 48px;
#             padding: 10px;
#             justify-content: center;
#             align-items: center;
#             gap: 16px;
#             flex-shrink: 0;
#             # position: relative;
#             # left: -50px 
#         }
#         # div.stButton > button:hover {
#         #     background-color: darkblue;
#         #     color: white;
#         # }
#         """,
# ):
#     st.button("connect data source")
#     # m.button("Create Ingestion")


# st.title("Welcome to Coridors Connector")
# st.write(
#     """
#     Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec neque eleifend, 
#     blandit augue vitae, mollis lorem. Fusce euismod tellus vitae turpis ullamcorper, 
#     quis hendrerit elit finibus. Nulla facilisi. Ut efficitur leo ut massa gravida, 
#     at amet mattis lorem ornare. Phasellus imperdiet, odio non vehicula sodales, 
#     dolor risus venenatis erat, vel blandit felis leo ut nisi. Donec rutrum nisi quis 
#     turpis convallis, non vestibulum felis euismod.
#     """
# )

# st.subheader("Supported Connectors")
# connectors = ["Salesforce", "GitHub", "Freshsales", "Confluence", "HubSpot", "Google Sheets", "Microsoft Ads"]

# with elements("container"):
#     with mui.Box(sx={"display": "flex", "gap": "20px", "flexWrap": "wrap"}):
#         for connector in connectors:
#             # mui.Button(f"connector", variant="contained")
#             mui.Button(
#                 f"{connector}",
#                 target="_blank",
#                 size="small",
#                 variant="contained",
#                 startIcon=mui.icon.Cloud,  # Using cloud icon for the startIcon
#                 style={
#                     "display": "inline-flex",
#                     "color": "black", 
#                     "background": "#D9D9D9", 
#                     "width": "auto",
#                     "border": "1px solid var(--Grey---outer-stroke, #D9D9D9)",
#                     "border-radius": "5px",
#                     "height": "48px", 
#                     "padding": "10px 16px",
#                     "border-radius": "10px",
#                     "justify-content": "center", 
#                     "align-items": "center", 
#                     "font-family": "sans-serif", 
#                     "font-size": "12px", 
#                     "font-style": "normal", 
#                     "font-weight": "600", 
#                     "line-height": "24px" 
#                 },  # Set width to 224px
#                 href="#"
#             )

# with elements("main_ingestion_btn"):
#     # Create the first button with red color
#     mui.Button(
#         "Create New Ingestion",
#         target="_blank",
#         size="small",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         style={"display": "flex","color": "white", "background": "#0062F6", "width": "100%", "border-radius": "5px", "height": "48px", "padding": "10px", "justify-content": "center", "align-items": "center", "font-family": "sans-serif", "font-size": "12px", "font-style": "normal", "font-weight": "600", "line-height": "24px"},  # Set width to 200px
#         href="#"
#     )

# with st.container():
#     st.subheader("Supported Connectors")
#     connectors = ["Salesforce", "GitHub", "Freshsales", "Confluence", "HubSpot", "Google Sheets", "Microsoft Ads"]
#     for connector in connectors:
#         # st.button(connector)
#         with elements(connector):
#             mui.Button(
#                 "Create Ingestion",
#                 target="_blank",
#                 size="small",
#                 variant="contained",
#                 startIcon=mui.icon.Cloud,  # Using cloud icon for the startIcon
#                 style={
#                     "display": "inline-flex",
#                     "color": "black", 
#                     "background": "#D9D9D9", 
#                     "width": "auto",
#                     "border": "1px solid var(--Grey---outer-stroke, #D9D9D9)",
#                     "border-radius": "5px",
#                     "height": "48px", 
#                     "padding": "10px 16px",
#                     "border-radius": "10px",
#                     "justify-content": "center", 
#                     "align-items": "center", 
#                     "font-family": "sans-serif", 
#                     "font-size": "12px", 
#                     "font-style": "normal", 
#                     "font-weight": "600", 
#                     "line-height": "24px" 
#                 },  # Set width to 224px
#                 href="#"
#             )
    
