import streamlit as st

st.title('Hello! This is Venkatesh' :blue[colors] and emojis :sunglasses:')


btn_click = st.button("Click Me!")

if btn_click == True:
    st.success('Yay!', icon="✅")
    st.balloons()
