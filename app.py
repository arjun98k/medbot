import os
import streamlit as st
from langchain_community.llms import OpenAI
from langchain_experimental.agents import create_csv_agent
# DONT SET TO ALWAYS RERUN THE SCRIPT AS IT WILL RELOAD THE AGENT EVERYTIME AND WILL USE OPEN AI API CREDITS


def main():
    # HIDE THIS IF WE ARE GOING TO DEPLOY
    OPENAI_API_KEY = "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"

    st.header("GenMed - General Medical Chatbot 💊") 
    st.markdown("GenMed is a general medical chatbot that can answer questions about your medication. 😊")
    st.write("""
    Tasks it can perform:
    * Provide generic prices for common medications 💰
    """)

    st.sidebar.markdown("*About MedBot*")
    st.sidebar.info("This chatbot is designed for informational purposes. Always consult a doctor for medical advice. ")
    st.sidebar.markdown("""
    *Data Source:* 
    1. Jan Aushadi Kendra Website : For Generic Medicine and Drug Information.
    2. Tata 1mg Website: For Normal Medicine Name and Price.""")

    agent = create_csv_agent(
        OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY),
        'data.csv',
        verbose=True
    )

    user_question = st.text_input("Ask a question about your medication: ")

    if user_question: 
        with st.spinner(text="Consulting the medical database... 🧠"):
            response = agent.run(user_question)
            st.write(response)

if __name__ == "__main__":
    main()