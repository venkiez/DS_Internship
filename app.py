import streamlit as st

st.title("Hello! This is Venkatesh")


btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :happy:")
    st.balloons()
