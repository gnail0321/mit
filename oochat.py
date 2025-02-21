import streamlit as st
from ollama import chat
st.title('chat bot')
if 'messages' not in st.session_state:
    st.session_state.messages = []

for messages in st.session_state.messages:
    with st.chat_message(name=messages['role']):
        st.write(messages["content"])


user_message=st.chat_input("type here")
if user_message:
    st.session_state.messages.append({
        'role' : 'user',
        'content' : user_message
    })
    with st.chat_message(name='user'):
        st.write(user_message)
    answer = chat(model="deepseek-r1", messages=[
        {
        'role': 'user',
        'content': user_message
        }
    ])
    st.session_state.messages.append({
        'role': 'assistant',
        'content': (answer['message']['content'])
    })
    with st.chat_message(name='assistant'):
        st.write(answer['message']['content'])