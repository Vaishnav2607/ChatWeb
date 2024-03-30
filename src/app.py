import streamlit as st
st.set_page_config(page_title="Chat with websites", page_icon="🤖")
st.title("Chat with websites")
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")


user_query = st.chat_input("Type your message here")
if user_query is not None and user_query !="":
    with st.chat_message("Me"):
        st.write("I want to know about your Langchain")

    with st.chat_message("Jarvis"):
        st.write("IDK IDK IDK IDK")
