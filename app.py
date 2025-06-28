# Q&A Chatbot with GPT-4o
from langchain_openai import ChatOpenAI  # For chat models like GPT-4o
from langchain.schema import HumanMessage
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os

## Function to load OpenAI model and get responses
def get_openai_response(question):
    if not question.strip():  # Handle empty input
        return "Please enter a question."
    
    llm = ChatOpenAI(
        model="gpt-4o",  # Valid model name for ChatOpenAI
        temperature=0.5,
        openai_api_key=os.getenv("OPENAI_API_KEY")  # Explicit API key
    )
    
    # For chat models, we need to format the input as messages
    messages = [HumanMessage(content=question)]
    response = llm.invoke(messages)
    return response.content

## Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

## If ask button is clicked
if submit:
    if input_text:
        with st.spinner("Getting response..."):
            response = get_openai_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question first.")