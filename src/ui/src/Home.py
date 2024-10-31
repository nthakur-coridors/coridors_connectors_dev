import streamlit as st
from sidebar_styles import styles
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def page1():
    st.write("This is Page 1")
     

def page2():
    st.write("This is Page 2")
    st.page_link("pages/2Setup.py", label="your_connections")
def page3():
    st.write("This is Page 3")

def chnage_page(page):
    st.session_state.nav = page

def setup_home_ui():
    st.set_page_config(layout="wide")
    styles()
    l_space, main_body, r_apace = st.columns([0.1, 0.80, 0.1])
    with main_body:
        st.title("Welcome to Coridors Connector")
        st.subheader("Seamlessly connect your data and boost productivity with Coridors Connect")
        st.write(
            """
            An ultimate solution for automating your data needs. Our powerful, integrated platform empowers you to effortlessly retrieve data from multiple sources, streamlining your workflows and enhancing productivity.
            """
        )
        st.write(' ')
        st.write(' ')
        st.write(' ')
        l_banner, main_banner, r_banner = st.columns([0.15, 0.7, 0.15])
        with main_banner:
            st.image("Group 60.svg")
        st.write(' ')
        st.write(' ')
        st.write(' ')

        st.header('Data Sources')

        with stylable_container(
            key = "container1",
            css_styles = """
                div[data-testid="stVerticalBlockBorderWrapper"]{
                # border: 1px solid black;
                background: #F9F9F9;
                # padding: 10px;
                }

                a[data-testid="stPageLink-NavLink"]{

                    flex-direction: column;
                    margin-top: 20px;
                }
            """
        ):
            container = st.container(border=True)
        with container:
            l_icon, m_icon ,r_icon = st.columns([0.1, 0.05, 0.7])
            st.write(' ')
            st.write(' ')
            st.write(' ')
            with l_icon:
                st.page_link("https://app.snowflake.com/mlpadyh/gj36557/worksheets", label=f"Salesforce", icon="🌎")
            with r_icon:
                st.page_link("https://app.snowflake.com/mlpadyh/gj36557/worksheets", label=f"Salesforce", icon="🌎")

            st.write(' ')
            st.write(' ')
            # st.write(' ')

            l, m ,r = st.columns([0.3, 0.4, 0.3])
            with m:
                with stylable_container(
                    key="btn2",
                    css_styles="""
                        div.stButton > button {
                            width: 100%;
                            height:48px;
                            border-radius:5px;
                            margin-left:4%;
                            font-weigtht: 300;
                            
                        }
                        """
                ):
                    st.button('Lets Gets Started! ', type='primary')

        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.subheader('Step by step guide')
        with stylable_container(
            key = "container2",
            css_styles = """
                div[data-testid="stVerticalBlockBorderWrapper"]{
                # border: 1px solid black;
                background: #F9F9F9;
                # padding: 10px;
                }

                # a[data-testid="stPageLink-NavLink"]{

                #     flex-direction: column;
                #     margin-top: 20px;
                # }
            """
        ):
            container = st.container(border=True)
        with container:
            st.write("1. Select your connector a.k.a Data Source Platfrom")
            st.write("2. Get the required details like API keys etc by reading our blog")
            st.write("3. Fill these details")
            st.write("4. Now Create Ingestion Configuration")
            st.write("5. Select the fields and objects to Ingest")
            st.write("6. Schedule the Ingestion")
            st.write("Yay, this is it. You will then successfully create your first ingestion")
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

def main():
    st.write("main")
    nav_to_button = st.button("setup")
    if nav_to_button:
        switch_page("Setup")

        # nav_to("Setup")
    
    # st.set_page_config(layout="wide")
    styles()
    # setup_home_ui()

    # col1, col2, col3 = st.columns([1, 1, 1])
    # col1.button("Page 1", on_click=chnage_page, args=("page1",))
    # col2.button("Page 2", on_click=chnage_page, args=("page2",))
    # col3.button("Page 3", on_click=chnage_page, args=("page3",))

    st.write(st.session_state)
    # st.write(st.session_state.current_page)

    if 'fist_time_setup' not in st.session_state:
        st.session_state.fist_time_setup = True


    if 'nav' not in st.session_state:
        st.session_state.nav = "Home"

    if 'page_nav' not in st.session_state:
        st.session_state.page_nav = "page1"

    if st.session_state.page_nav == "page1":
        page1()
    elif st.session_state.page_nav == "page2":
        page2()
    elif st.session_state.page_nav == "page3":
        page3()

        


if __name__ == "__main__":
    main()