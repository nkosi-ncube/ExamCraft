import streamlit as st
import yaml
import json
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain_community.chat_message_histories import (
    StreamlitChatMessageHistory,)
from prompt_templates import memory_prompt_template

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


with open("config.yaml") as f:
    config = yaml.safe_load(f)


def get_llm():
    llm = GoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm


def clear_input_field():
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""


def set_send_input():
    st.session_state.send_input = True
    clear_input_field()


def save_chat_history():
    if st.session_state.history != []:
        chat = st.session_state.history

        with open(config["chat_history_path"] + "random" + ".json") as f:
            json_data = [message.dict() for message in chat.messages]
            json.dump(json_data, f)


def main():
    st.title("Multimodal Local Chat App")
    st.sidebar.title("Chat Sessions")

    chat_sessions = ["new_session"] + os.listdir(
        config["chat_histroy_path"]
    )

    chat_container = st.container()

    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    st.sidebar.selectbox(
        "Select a chat session",
        chat_sessions,
        key="session_key"
    )

    chat_history = StreamlitChatMessageHistory(key="history")
    llm = get_llm()
    chat_prompt = PromptTemplate.from_template(memory_prompt_template)

    user_input = st.text_input(
        "Type your message here",
        key="user_input",
        on_change=set_send_input
    )

    send_button = st.button("Send", key="send_button")

    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            with chat_container:
                st.chat_message("user").write(st.session_state.user_question)
                user_input = st.session_state.user_question

                chain = chat_prompt | llm
                stop_tokens = ["<eos>", "bye", "thank you"]

                chain.invoke(
                    {"human_input": user_input, "history": chat_history},
                    stop=stop_tokens
                )

                st.session_state.user_question = ""

    if chat_history.messages != []:
        st.write("chat Histroy")

        with chat_container:
            for message in chat_history.messages:
                st.chat_message(message.type).write(message.content)

    save_chat_history()


if __name__ == "__main__":
    main()
