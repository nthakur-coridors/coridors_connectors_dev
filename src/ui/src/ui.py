from dataclasses import dataclass
from dateutil import parser
from datetime import date, datetime
import json
import random
import pandas as pd
import streamlit as st
import snowflake.permissions as permission
from snowflake.snowpark.functions import call_udf, col, lit
from snowflake.snowpark import Session
from streamlit_extras.stylable_container import stylable_container


session = Session.builder.getOrCreate()

@dataclass
class Reference:
    name: str
    label: str
    type: str
    description: str
    bound_alias: str


def setup():
   st.header("First-time setup")
   st.caption("""
        Follow the instructions below to set up your application.
        Once you have completed the steps, you will be able to continue to the main example.
    """)

   refs = get_references()
   for ref in refs:
      name = ref.name
      label = ref.label

      if not ref.bound_alias:
         st.button(f"{label} ↗", on_click=permission.request_reference, args=[name], key=name)
      else:
          st.caption(f"*{label}* binding exists ✅")     

      if not ref.bound_alias: return
   
   if st.button("Continue to app", type="primary"):
      result = session.call('create_eai_objects')
      if result == 'SUCCESS':
         st.session_state.privileges_granted = True
         st.experimental_rerun()
      else:
         st.error('Connection to `api.coincap.io` failed. Try again later', icon="🚨")

def get_references():
   app_name = session.get_current_database()
   data_frame = session.create_dataframe([''])
   refs = data_frame.select(call_udf('system$get_reference_definitions', lit(app_name))).collect()[0][0]
   references = []
   for row in json.loads(refs):
      bound_alias = row["bindings"][0]["alias"] if row["bindings"] else None
      references.append(Reference(row["name"], row["label"], row["object_type"], row["description"], bound_alias))
   return references


def run_streamlit():
   # st.title('Hello Snowflake!')

   # st.header('External Access Integration Example')
   # st.write(
   #    """
   #    Shows the price timeline of the selected currency in a specified date range
   #    using the `api.coincap.io` API to get real-time prices.
   #    Coin names and prices are retrieved from the `core.get_coin_story` and `core.get_crypto_coins`
   #    stored procedures who use an External Access Integration.
   #    """)
   # sales = session.call('core.salesforce')
   # st.write(sales)
   # import streamlit as st

   # Sidebar
   # st.sidebar.image("https://via.placeholder.com/150", width=100)  # Placeholder for logo
   # st.sidebar.title("Coridors Connector")
   # st.sidebar.button("Create Ingestion")
   # st.sidebar.write("---")
   # st.sidebar.write("Help & Support")
   # st.sidebar.write("Settings")

   with st.sidebar:
    # st.button("normal button")
    # st.logo("./logo.png")
    # sidebar_header()
    # st.header("Coridors Connector")
    # sidebar_components()q
    sidebar_components()

   

   # Main Page
   st.title("Welcome to Coridors Connector")
   st.write("[OpenAI](https://www.openai.com)")
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
   st.button("Create New Ingestion",type="primary" )

   # Tutorials Section
   st.subheader("Tutorials")
   st.markdown("[YouTube Video Tutorial](https://app.snowflake.com/mlpadyh/gj36557/worksheets)")
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
    l,m,r = st.columns([0.2,1,1])
    with m:     
        with stylable_container(
            key="btn_create_ingestion",
            css_styles="""
                div.stButton > button {
                    display: inherit;
                    position: inherit;
                    background-color: red;
                    color: white;
                    border-radius: 5px;
                    display: flex;
                    width: 224px;
                    height: 48px;
                    padding: 10px;
                    justify-content: center;
                    align-items: center;
                    gap: 16px;
                    flex-shrink: 0;
                    # position: relative;
                    # left: -50px 
                }
                # div.stButton > button:hover {
                #     background-color: darkblue;
                #     color: white;
                # }
                """,
        ):
            m.button("Create Ingestion", type="primary")

if __name__ == '__main__':
   if 'privileges_granted' not in st.session_state:
      setup()
   else:
      run_streamlit()
