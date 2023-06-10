import streamlit as st
from streamlit_chat import message

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'userInput' not in st.session_state:
    st.session_state['userInput'] = []

if 'input' not in st.session_state:
    st.session_state['input'] = ''


def getText():
    input = st.text_input("What can we help with?",
                          value=st.session_state.input)
    return input


placeholder = st.empty()
inputIdx = 0
userInput = getText()
if userInput:
    st.session_state.userInput.append(userInput)
    st.session_state.generated.append("test answer")

with placeholder.container():
    if st.session_state['generated']:
        size = len(st.session_state['generated'])
        for i in range(0, size):
            message(st.session_state['userInput'][i],
                    is_user=True, key='user message ' + str(i))
            message(st.session_state["generated"]
                    [i], key='bot message ' + str(i))
