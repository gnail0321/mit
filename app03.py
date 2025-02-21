import streamlit as st
import random

if not 'counter' in st.session_state:
    st.session_state.counter = 1
if not 'clicked' in st.session_state:
    st.session_state.clicked = 1
clearb= st.button('clear counter')
addb= st.button('increase counter')
sub= st.button('decrease counter')
if addb: st.session_state.counter+=1
if sub: st.session_state.counter-=1
if clearb: st.session_state.counter=1
clicked = st.button("click me", key="clicked")
if st.session_state.clicked:
    name = st.text_input('your name?', key='name')
st.title("session state")
st.header(f'counter = {st.session_state.counter}')
n = st.session_state.counter
data= {
    'name' :[random.choice(["Anna", "Betsy", 'Cathy']) for i in range(n)],
    'GPA' :[random.choice([3.9,4.0,3.3]) for i in range(n)],
    'country' :[random.choice(["Russia","Ukraine",'USA']) for i in range(n)],
}
st.table(data)