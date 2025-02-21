from random import choice

import streamlit as st

st.title("hello")
st.header("header 1")
st.latex('f(x) = e')
st.header("code")
st.code('''import streamlit as 
st print("helloo") 
st.header("header 1") ''')
st.image("https://picsum.photos/800/600")
st.header("header 2")
st.text("my fav photo")
st.header("markdown")
st.markdown('''# ''')
n=1000
data= {
    'name' :[choice(["Anna","Betsy",'Cathy']) for i in range(n) ],
    'GPA' :[choice([3.9,4.0,3.3]) for i in range(n)],
    'country' :[choice(["Russia","Ukraine",'USA']) for i in range(n)],
}
st.table(data)

