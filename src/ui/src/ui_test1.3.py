# import streamlit as st

# # Custom CSS to change button color to blue
# st.markdown("""
#     <style>
#     div.stButton > button {
#         background-color: #0062F6;
#         color: white;
#         border-radius: 5px;
#         border: none;
#     }
#     div.stButton > button:hover {
#         background-color: darkblue;
#         color: white;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Example Streamlit button
# st.button("Click Me!")


# import streamlit as st

# # Custom CSS to style buttons inside containers
# st.markdown("""
#     <style>
#     #container1 button {
#         background-color: grey;
#         color: white;
#         border-radius: 5px;
#         border: none;
#         padding-left: 10px;
#         transition: all 0.3s ease;
#     }
#     #container1 button:hover {
#         background-color: grey;
#         border-left: 10px solid blue;
#         padding-left: 20px;
#     }
    
#     #container2 button {
#         background-color: lightgrey;
#         color: black;
#         border-radius: 5px;
#         border: none;
#         padding-left: 10px;
#         transition: all 0.3s ease;
#     }
#     #container2 button:hover {
#         background-color: lightgrey;
#         border-left: 10px solid green;
#         padding-left: 20px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Create two containers
# with st.container() as container1:
#     st.markdown('<div id="container1">', unsafe_allow_html=True)
#     st.button("Button in Container 1")
#     st.markdown('</div>', unsafe_allow_html=True)

# with st.container() as container2:
#     st.markdown('<div id="container2">', unsafe_allow_html=True)
#     st.button("Button in Container 2")
#     st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()