import streamlit as st

st.title("interactive widgets")
clicked = st.button('register')
f=st.text_input('first name?')
l=st.text_input('last name?')
da=st.date_input("date")
st.color_picker("color picker")
st.feedback("faces")
fa=st.file_uploader("file")
note=st.text_input('note?')
#if clicked:
if f:
    st.write(f)
if l:
    st.write(l)
