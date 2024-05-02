from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.prompts import PromptTemplate

import streamlit as st
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# A list of intents for dialogflow
INTENTS = [
    "Asking for a list of courses",
    "General questions or small talk",
]

ENTITIES = {
    "courses": [
        "Arithmetic and Basic Algebra",
        "Geometry and Trigonometry",
        "Algebra and Linear Algebra",
        "Calculus and Differential Equations",
        "Probability and Statistics",
        "Discrete Mathematics",
        "Number Theory and Abstract Algebra",
        "Applied Mathematics and Computer Science",
        "Mathematical Logic and Foundations",
        "Advanced Topics and Specialized Fields"
    ]
}


def render_header():
    st.set_page_config(
        page_title="ExamCraft: AI-Powered Study Companion",
        page_icon="📖")

    st.title("📖 ExamCraft")

    """
    AI-powered study companion designed to enhance exam preparation methods 
    by analyzing past exam papers, generating personalized study materials
    """


def get_llm():
    llm = GoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=GOOGLE_API_KEY,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm


def gen_intent(prompt):
    template = """<s>[INST] You are an AI chatbot having a conversation with a human. Provide only the list index of the relevant intent (e.g., 0).[/INST]
    Intents: {intents}
    Question: {question}
    Answer:
    """

    prompt = PromptTemplate.from_template(template)
    llm = get_llm()

    chain = prompt | llm

    question = prompt
    return chain.invoke({"question": question, "intents": INTENTS})


def gen_dialogflow(index):
    print(index)


def main():
    render_header()

    # Set up memory
    msgs = StreamlitChatMessageHistory(key="langchain_messages")

    if len(msgs.messages) == 0:
        msgs.add_ai_message("How can I help you?")

    # Sidebar to display message history
    with st.sidebar.title("Message History"):
        view_messages = st.expander(
            "View the message contents in session state")

    # Set up the LangChain, passing in Message History

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI chatbot having a conversation with a human."),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    llm = get_llm()
    chain = prompt | llm

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="history",
    )

    # Render current messages from StreamlitChatMessageHistory
    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content)

    # If user inputs a new prompt, generate and draw a new response
    if prompt := st.chat_input():
        st.chat_message("human").write(prompt)

        #   testing dialogue
        intent = gen_intent(prompt)

        # akd;kadflkjd dj;fkdj
        answer = gen_dialogflow(intent)

        # Note: new messages are saved to history automatically by Langchain during run
        # config = {"configurable": {"session_id": "any"}}
        # response = chain_with_history.invoke({"question": prompt}, config)
        # st.chat_message("ai").write(response)

    # Draw the messages at the end, so newly generated ones show up immediately
    with view_messages:
        """
        Message History initialized with:
        ```python
        msgs = StreamlitChatMessageHistory(key="langchain_messages")
        ```

        Contents of `st.session_state.langchain_messages`:
        """
        view_messages.json(st.session_state.langchain_messages)


if __name__ == "__main__":
    main()
