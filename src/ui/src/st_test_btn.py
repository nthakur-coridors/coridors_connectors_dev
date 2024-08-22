# # First, import the elements you need

# from streamlit_elements import elements, mui, html
# # import streamlit as st
# # from streamlit_elements import Elements

# # Create a frame where Elements widgets will be displayed.
# #
# # Elements widgets will not render outside of this frame.
# # Native Streamlit widgets will not render inside this frame.
# #
# # elements() takes a key as parameter.
# # This key can't be reused by another frame or Streamlit widget.

# with elements("new_element"):

#     # Let's create a Typography element with "Hello world" as children.
#     # The first step is to check Typography's documentation on MUI:
#     # https://mui.com/components/typography/
#     #
#     # Here is how you would write it in React JSX:
#     #
#     # <Typography>
#     #   Hello world
#     # </Typography>

#     mui.Typography("Hello world")

# with elements("multiple_children"):

#     # You have access to Material UI icons using: mui.icon.IconNameHere
#     #
#     # Multiple children can be added in a single element.
#     #
#     # <Button>
#     #   <EmojiPeople />
#     #   <DoubleArrow />
#     #   Hello world
#     # </Button>

#     mui.Button(
#         mui.icon.EmojiPeople,
#         mui.icon.DoubleArrow,
#         "Button with multiple children"
#     )

#     # You can also add children to an element using a 'with' statement.
#     #
#     # <Button>
#     #   <EmojiPeople />
#     #   <DoubleArrow />
#     #   <Typography>
#     #     Hello world
#     #   </Typography>
#     # </Button>

#     with mui.Button:
#         mui.icon.EmojiPeople()
#         mui.icon.DoubleArrow()
#         mui.Typography("Button with multiple children")



# mt = elements()

# mt.button(
# "I am a button!", 
# target="_blank", 
# size="medium", 
# variant="contained", 
# start_icon=mt.icons.add_box, 
# onclick=mt.rerun, 
# style={"color":"#FFFFFF", "background":"#FF4B4B"}, 
# href="https://mui.com/components/buttons/")

# mt.show(key = "450")

# import streamlit as st
# from streamlit_elements import elements, html

# # Set page configuration
# st.set_page_config(page_title="Custom Buttons", layout="centered")

# # Use Streamlit Elements to create custom buttons
# with elements("custom_buttons"):
#     html.button(
#         "Small Red Button", 
#         style={
#             "background-color": "red", 
#             "color": "white", 
#             "border": "none", 
#             "padding": "5px 10px", 
#             "font-size": "12px", 
#             "cursor": "pointer"
#         }
#     )
    
#     html.button(
#         "Medium Green Button", 
#         style={
#             "background-color": "green", 
#             "color": "white", 
#             "border": "none", 
#             "padding": "10px 20px", 
#             "font-size": "16px", 
#             "cursor": "pointer"
#         }
#     )
    
#     html.button(
#         "Large Blue Button", 
#         style={
#             "background-color": "blue", 
#             "color": "white", 
#             "border": "none", 
#             "padding": "15px 30px", 
#             "font-size": "20px", 
#             "cursor": "pointer"
#         }
#     )



# import streamlit as st
# from streamlit_elements import elements

# mt = elements()

# mt.button(
# "I am a button!", 
# target="_blank", 
# size="medium", 
# variant="contained", 
# start_icon=mt.icons.add_box, 
# onclick=mt.rerun, 
# style={"color":"#FFFFFF", "background":"#FF4B4B"}, 
# href="https://mui.com/components/buttons/")

# mt.show(key = "450")

# import streamlit as st
# from streamlit_elements import elements, mui

# # Initialize Streamlit Elements container
# with elements("my_elements"):
#     # Create the button with a custom width of 200px
#     mui.Button(
#         "I am a button!",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         style={
#             "color": "#FFFFFF",
#             "background": "#FF4B4B",
#             "width": "700px",
#             "transition": "transform 0.2s ease-in-out",  # Smooth transition
#         },
#         href="https://mui.com/components/buttons/",
#         onMouseEnter={
#             "transform": "scale(1.05)"
#             "background": "#FF4B4B",  # Scale up slightly on hover
#         },
#         onMouseLeave={
#             "transform": "scale(1)"  # Reset scale when not hovered
#         }
#     )



# import streamlit as st
# from streamlit_elements import elements, mui

# # Custom CSS for hover effect with color change
# hover_css = """
#     <style>
#     .custom-button {
#         width: 200px;
#         color: #FFFFFF;
#         background: #FF4B4B;
#         transition: transform 0.2s ease-in-out, background-color 0.2s ease-in-out;
#     }
#     .custom-button:hover {
#         transform: scale(1.05);
#         background-color: #FF0000;  # Change the background color on hover
#     }
#     </style>
#     """

# # Add custom CSS to the Streamlit app
# st.markdown(hover_css, unsafe_allow_html=True)

# # Initialize Streamlit Elements container
# with elements("my_elements"):
#     # Create the button using the custom class
#     mui.Button(
#         "I am a button!",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         className="custom-button",  # Apply the custom CSS class
#         href="https://mui.com/components/buttons/"
#     )


# import streamlit as st
# from streamlit_elements import elements, mui

# # Custom CSS for hover effects with color changes
# hover_css = """
#     <style>
#     .custom-button-red {
#         width: 200px;
#         color: #FFFFFF;
#         background: #FF4B4B;
#         transition: transform 0.2s ease-in-out, background-color 0.2s ease-in-out;
#         margin-right: 10px;  # Add some space between buttons
#     }
#     .custom-button-red:hover {
#         transform: scale(1.05);
#         background-color: #FF0000;  # Change the background color on hover
#     }

#     .custom-button-blue {
#         width: 200px;
#         color: #FFFFFF;
#         background: #4B79FF;
#         transition: transform 0.2s ease-in-out, background-color 0.2s ease-in-out;
#     }
#     .custom-button-blue:hover {
#         transform: scale(1.05);
#         background-color: #0033FF;  # Change the background color on hover
#     }
#     </style>
#     """

# # Add custom CSS to the Streamlit app
# st.markdown(hover_css, unsafe_allow_html=True)

# # Initialize Streamlit Elements container
# with elements("my_elements"):
#     # Create the first button with red color and hover effect
#     mui.Button(
#         "Red Button",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         className="custom-button-red",  # Apply the custom CSS class for the red button
#         href="https://mui.com/components/buttons/"
#     )
    
#     # Create the second button with blue color and hover effect
#     mui.Button(
#         "Blue Button",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         className="custom-button-blue",  # Apply the custom CSS class for the blue button
#         href="https://mui.com/components/buttons/"
#     )


# import streamlit as st
# from streamlit_elements import elements, mui

# # Initialize Streamlit Elements container
# with elements("my_elements"):
#     # Create the first button with red color
#     mui.Button(
#         "Red Button",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         style={"color": "#FFFFFF", "background": "#FF4B4B", "width": "200px"},  # Set width to 200px
#         href="https://mui.com/components/buttons/"
#     )

#     # Create the second button with green color
#     mui.Button(
#         "Green Button",
#         target="_blank",
#         size="medium",
#         variant="contained",
#         startIcon=mui.icon.add_box,  # Correct usage for the startIcon
#         style={"display": "flex","color": "white", "background": "#0062F6", "width": "224px","border-radius": "5px", "height": "48px", "padding": "10px", "justify-content": "center", "align-items": "center", "gap": "16px", "flex-shrink": "px"},  # Set width to 200px and green color
#         href="https://mui.com/components/buttons/"
#     )

# import streamlit as st

# # Initialize session state for button style
# if 'button_color' not in st.session_state:
#     st.session_state['button_color'] = 'primary'

# # Function to change button style
# def toggle_button_color():
#     if st.session_state['button_color'] == 'red':
#         st.session_state['button_color'] = 'green'
#     else:
#         st.session_state['button_color'] = 'red'

# # Display the button with dynamic style
# st.markdown(
#     f"""
#     <style>
#         .stButton > button {{
#             background-color: f"{st.session_state['button_color']}";
#             color: white;
#             border-radius: 8px;
#             padding: 10px 20px;
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# if st.button("Click Me!", on_click=toggle_button_color):
#     st.write("Button clicked!")

# st.write(f"Current Button Color: {st.session_state['button_color']}")


from streamlit_elements import mui, elements, sync

with elements("container"):
    # Create a div with flex display to align buttons horizontally and wrap to the next line if needed
    with mui.Box(sx={"display": "flex", "gap": "10px", "flexWrap": "wrap"}):  # Gap is the space between buttons
        mui.Button("Button 1", variant="contained")
        mui.Button("Button 2", variant="contained")
        mui.Button("Button 3", variant="contained")
        mui.Button("Button 4", variant="contained")
        mui.Button("Button 5", variant="contained")
        mui.Button("Button 6", variant="contained")
        mui.Button("Button 7", variant="contained")
        mui.Button("Button 8", variant="contained")
        mui.Button("Button 9", variant="contained")
        mui.Button("Button 10", variant="contained")

