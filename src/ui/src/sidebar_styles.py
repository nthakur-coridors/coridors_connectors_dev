import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# from streamlit_elements import elements, mui


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
            st.image("logo.svg", width=120)


def styles():
    # st.set_page_config(layout="wide")
    st.markdown(
    """
    <style>
    
    section[data-testid="stSidebar"]{
        background-color: #FCFCFC;
    }
    div[data-testid="stSidebarNav"]{
        boder: none;
    }
    div[data-testid="stSidebarNavItems"]{
        # display: flex;
        # flex-direction: column;
        # min-height: 75vh;
        # position: absolute;
        # top: 300px;
        # width:100%;
        justify-content: center;
        align-items: center;
    }
    ul{
        # border-bottom: 200px;
        display: flex;
        flex-direction: column;
        min-height: 67vh;
        position: absolute;
        top: 200px;
        width:100%;
        # margin-top: 100px;
        # justify-content: center;
        # align-items: center;

    }
    div[data-testid="stSidebarNavSeparator"]{
        padding-top: 0;
        border-bottom : none;
    }
    li {
        # display: flex;
        justify-content: space-around;
        padding: 8px 0px 8px 0px;
        margin: 0;
    }
    # li > div{
    #     background-color: #D9D9D91A;
    #     # border-left: 5px solid blue;
    # }
    # li > div:hover{
    #     # background-color: #CBE0FF;
    #     backgound-color: rgba(203, 224, 255, 0.3);
    #     border-left: 5px solid blue;
    #     color: white;
    # }
    # li > div:active{
    #     background-color: #CBE0FF;
    #     border-left: 5px solid blue;
    #     color: white;
    # }
    # li a{
    #     display: flex;
    #     position: relative;
    #     margin: 0;
    #     # top: 80px;
    #     left: -18px;
    #     width: 326px;
    #     height: 48px;
    #     padding: 8px 0px;
    #     align-items: center;
    #     gap: 16px;
    #     flex-shrink: 0;
    #     # justify-content: center;
    #     # align-items: center;
    #     # gap: 16px;
    #     # flex-shrink: 0;
    #     color: black;
    #     background-color: black;
    #     # # left: 50px;
    #     # left: -25px;
    #     # border-radius:100px;
    #     # background: orange;
    #     # background-color: rgba(0, 0, 255, 0.2);
    #     # border-left: 5px solid blue;
    # }

    a[data-testid="stSidebarNavLink"]{
        background: rgba(217, 217, 217, 0.1);
    }

    # a[data-testid="stSidebarNavLink"]{
    #     background-color: grey;
    # }
    # a[data-testid="stSidebarNavLink"]:hover{
    #     background-color: rgba(0, 128, 0, 0.8);
    #     border-left: 5px solid blue;
    # }
    # a[data-testid="stSidebarNavLink"]:active{
    #     background-color: rgba(0, 128, 0, 0.8);
    #     border-left: 5px solid blue;
    # }
    # a[data-testid="stSidebarNavLink"]:visited{
    #     background-color: rgba(0, 128, 0, 0.8);
    #     border-left: 5px solid blue;
    # }
    li a:hover {
        # background-color: darkblue;
        # border-left: 10px solid blue;
        color: white;
    }
    li a:visited{
        background-color: #D9D9D9;
        # border-left: 5px solid blue;
        color: white;;
    }
    li a:active {
        background-color: #CBE0FF;
        # background-color: blue;
        # border-left:10 solid blue;
        color: white;
    }
    li > div> a> span{
        display: flex;
        position: relative;
        left: 10px;
        # margin-left :20px;
    }
    li > div> a> span: hover{
        display: flex;
        position: relative;
        left: 10px;
        # color: green;
        
    }
    li:nth-child(3) {
        margin-bottom: 30vh;
    }
    
    # div[data-testid="stSidebarNavSeparator"]{
    #     display: flex;
    #     position: absolute;
    #     # display: none;
    # }

    
    </style>
    """,
    unsafe_allow_html=True,
    )
    # styles()
    with st.sidebar:
        # st.logo("../resources/Logo.png")
        # st.markdown('<p class="text-logo">MyApp</p>', unsafe_allow_html=True)
        sidebar_components()



# def main():
#     styles()
#     with st.sidebar:
#         sidebar_components()


if __name__ == "__main__":
    # main()
    # st.logo("Logo.png")

    styles()









