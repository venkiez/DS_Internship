import streamlit as st

st.title( ':blue[Hello! This is Venkatesh] :sunglasses:')


btn_click = st.button("Click Me!")

if btn_click == True:
    st.success('Yay!', icon="✅")
    st.balloons()
