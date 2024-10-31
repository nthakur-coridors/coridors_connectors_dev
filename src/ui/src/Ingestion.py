import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# from streamlit_elements import elements, mui
from sidebar_styles import styles

st.set_page_config(layout="wide")
styles()

l,m,r = st.columns([0.15, 0.7, 0.15])

with m:
    # st.write("Ingestion")

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

    st.subheader("Supported Connectors")
    connectors = ["Salesforce", "GitHub", "Freshsales", "Confluence", "HubSpot", "Google Sheets", "Microsoft Ads"]

    c1,c2,c3,c4,c5 = st.columns([0.15,0.2,0.2,0.2,0.2])
    with stylable_container(
        key="Salesforce",
        css_styles="""

            div[class="row-widget stPageLink"]{
                display: inline-flex;
                # position: relative;
            }
            a[data-testid="stPageLink-NavLink"]{
                height:48px;
                border-radius:20px;
                background: rgba(128, 128, 128, 0.1);
                # display:block;
                # position:absolute;
                
            }
            a[data-testid="stPageLink-NavLink"]:hover{
                background: rgba(0, 0, 255, 0.3);
            }

            a[data-testid="stPageLink-NavLink"]:active{
                background: rgba(0, 0, 255, 0.8);
                font-weight: 500;
            }

            """
        ):
            with c1:
                st.page_link("https://app.snowflake.com/mlpadyh/gj36557/worksheets", label=f"Salesforce", icon="🌎")
            
            with c3:
                 st.page_link("pages/configuration.py", label=f"GitHub", icon=":material/cloud:")


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
    #     mui.Button(
    #         "Create New Ingestion",
    #         target="_blank",
    #         size="small",
    #         variant="contained",
    #         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
    #         style={"display": "flex","color": "white", "background": "#0062F6", "width": "100%", "border-radius": "5px", "height": "48px", "padding": "10px", "justify-content": "center", "align-items": "center", "font-family": "sans-serif", "font-size": "12px", "font-style": "normal", "font-weight": "600", "line-height": "24px"},  # Set width to 200px
    #         href="#"
    #     )
    # url = "login.salesforce.com"

    # l,m,r = st.columns([0.1,3,0.1])
    with m:
        with stylable_container(
            key="btn2",
            css_styles="""
                div.stButton > button {
                    width: 92%;
                    height:48px;
                    border-radius:5px;
                    margin-left:4%;
                    font-weigtht: 300;
                    
                }
                """
        ):
            st.button('☁️ingestion :cloud:', type='primary')

    # st.markdown(
    #         """
    #         <style>
    #         div[data-testid="column"]{
    #         height: 300px,
    #         }
    #         """,
    #         unsafe_allow_html=True
    #     )
    media_link, r1, media_video, l1 = st.columns([0.1,0.05,0.23,0.02])
    with media_link:
        # Tutorials Section
        st.subheader("Tutorials")
        st.markdown("[YouTube Video Tutorial](#)")
        st.markdown("[Quick Guide to Connector](#)")
        st.markdown("[Documentation](#)")
        st.markdown("[Walkthrough](#)")

    # with media_video:
    #     # st.write("video")
    #     st.video("resources/1 Minute Sample Video.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

    # FAQ's
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
with r:
    # Adding a help icon with a tooltip using HTML
    st.markdown("""
        <style>
        .help-icon {
            color: #999;
            font-size: 1.2em;
            cursor: pointer;
        }
        .tooltip {
            display: inline-block;
            position: relative;
        }
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 200px; /* Increased width to accommodate more text */
            background-color: black;
            color: #fff;
            text-align: left; /* Align text to the left */
            border-radius: 5px;
            padding: 10px; /* Increased padding for better readability */
            position: absolute;
            z-index: 1;
            left: 125%; /* Position the tooltip to the right of the icon */
            top: 50%;
            margin-top: -25px; /* Adjust vertical alignment */
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="tooltip">
            <span class="help-icon">?</span>
            <span class="tooltiptext">
                <p>This is a longer help message. It includes a few sentences to provide more detailed information about the feature or functionality. You can use this space to explain things in more depth and give users additional context or instructions.</p>
            </span>
        </div>
        """, unsafe_allow_html=True)