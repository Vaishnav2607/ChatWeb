import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def get_response(user_input):
    return "IDK IDK IDK IDK"

# app config
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
    AIMessage(content="Hello I am Jarvis I can chat with websites, How ca I help you?"),
    ]
# sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")
if website_url is None or website_url =="":
    st.info("Please enter a website url")
else:
# user input
    user_query = st.chat_input("Type your message here")
    if user_query is not None and user_query !="":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
    # with st.sidebar:
    #     st.write(st.session_state. chat_history)

    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("Jarvis"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Me"):
                st.write(message.content)
