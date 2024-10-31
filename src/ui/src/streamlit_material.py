import streamlit as st

# Custom CSS to mimic Material Design and add a new green button style
st.markdown(
    """
    <style>
    .material-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: 500;
        color: white;
        background-color: #6200ea;
        border-radius: 4px;
        text-align: center;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }

    .material-button:hover {
        background-color: #3700b3;
    }

    .green-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: 500;
        width: 80%;
        color: #fff;
        background-color: #4CAF50; /* Green background */
        border-radius: 4px;
        text-align: center;
        text-decoration: none;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .green-button:hover {
        background-color: #FF9800; /* Orange background on hover */
        color: #000; /* Black text on hover */
    }

    .material-card {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
        background-color: #fff;
    }

    .material-card h3 {
        color: #333;
        margin-bottom: 10px;
    }

    .material-card p {
        color: #666;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating a Material Design styled button
st.markdown('<a href="#" class="material-button">Material Button</a>', unsafe_allow_html=True)

# Creating a green button with custom hover effects
st.markdown('<a href="#" class="green-button">Green Button</a>', unsafe_allow_html=True)

# Creating a material design styled card
st.markdown('<div class="material-card">', unsafe_allow_html=True)
st.markdown('<h3>Material Card</h3>', unsafe_allow_html=True)
st.markdown('<p>This is a simple card that mimics Material Design principles using custom CSS.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Adding a few more components
st.write("This is a simple text element outside of the Material card.")

# Another card with Material Design
st.markdown('<div class="material-card">', unsafe_allow_html=True)
st.markdown('<h3>Another Material Card</h3>', unsafe_allow_html=True)
st.markdown('<p>Material Design principles focus on clean, modern aesthetics and smooth interactions.</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.button("btn1")
st.button('btn2', type="primary")