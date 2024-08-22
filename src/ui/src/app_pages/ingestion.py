import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_elements import elements, mui

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

    with elements("container"):
        with mui.Box(sx={"display": "flex", "gap": "20px", "flexWrap": "wrap"}):
            for connector in connectors:
                # mui.Button(f"connector", variant="contained")
                mui.Button(
                    f"{connector}",
                    target="_blank",
                    size="small",
                    variant="contained",
                    startIcon=mui.icon.Cloud,  # Using cloud icon for the startIcon
                    style={
                        "display": "inline-flex",
                        "color": "black", 
                        "background": "#D9D9D9", 
                        "width": "auto",
                        "border": "1px solid var(--Grey---outer-stroke, #D9D9D9)",
                        "border-radius": "5px",
                        "height": "48px", 
                        "padding": "10px 16px",
                        "border-radius": "10px",
                        "justify-content": "center", 
                        "align-items": "center", 
                        "font-family": "sans-serif", 
                        "font-size": "12px", 
                        "font-style": "normal", 
                        "font-weight": "600", 
                        "line-height": "24px" 
                    },  # Set width to 224px
                    href="#"
                )

    with elements("main_ingestion_btn"):
        mui.Button(
            "Create New Ingestion",
            target="_blank",
            size="small",
            variant="contained",
            startIcon=mui.icon.add_box,  # Correct usage for the startIcon
            style={"display": "flex","color": "white", "background": "#0062F6", "width": "100%", "border-radius": "5px", "height": "48px", "padding": "10px", "justify-content": "center", "align-items": "center", "font-family": "sans-serif", "font-size": "12px", "font-style": "normal", "font-weight": "600", "line-height": "24px"},  # Set width to 200px
            href="#"
        )
    url = "login.salesforce.com"

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

    with media_video:
        # st.write("video")
        st.video("https://www.youtube.com/watch?v=wDchsz8nmbo", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)

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