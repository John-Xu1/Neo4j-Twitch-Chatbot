import streamlit as st
from streamlit_chat import message
from textToCypher import genereateCypher
from queryToText import generateResponse
from neo4jController import runQuery

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'userInput' not in st.session_state:
    st.session_state['userInput'] = []

if 'queryResults' not in st.session_state:
    st.session_state['queryResults'] = []

if 'cyphers' not in st.session_state:
    st.session_state['cyphers'] = []


def getText():
    input = st.text_input("What can we help with?")
    return input


def generateMessages(prompt, context):
    messages = []
    if st.session_state['generated']:
        size = len(st.session_state['generated'])
        for i in range(max(size-3, 0), size):
            messages.append(
                {'role': 'user', 'content': st.session_state['userInput'][i]})
            messages.append(
                {'role': 'assistant', 'content': st.session_state.get(context, [''])[i]})
    messages.append({'role': 'user', 'content': str(prompt)})
    return messages


placeholder = st.empty()
inputIdx = 0
userInput = getText()
if userInput:
    cypher = genereateCypher(generateMessages(userInput, 'queryResults'))
    print(cypher)
    queryResults = runQuery(cypher, {})
    print(queryResults)
    response = generateResponse(generateMessages(
        f"Question was {userInput} and the response should include only information that is given here: {str(queryResults)}", 'generated'))
    print(response)
    st.session_state.userInput.append(userInput)
    st.session_state.generated.append(response)
    st.session_state.cyphers.append(cypher)
    st.session_state.queryResults.append(str(queryResults))


with placeholder.container():
    if st.session_state['generated']:
        size = len(st.session_state['generated'])
        for i in range(max(size-3, 0), size):
            message(st.session_state['userInput'][i],
                    is_user=True, key='user message ' + str(i))
            message(st.session_state["generated"]
                    [i], key='assistant message ' + str(i))
