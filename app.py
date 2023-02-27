import streamlit as st

st.title("Hello! This is Venkatesh")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()