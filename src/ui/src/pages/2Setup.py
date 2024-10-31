import streamlit as st
from sidebar_styles import styles
from streamlit_extras.stylable_container import stylable_container
from PIL import Image


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

def main():
    setup_home_ui()

        


if __name__ == "__main__":
    main()