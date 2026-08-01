import os
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Explicitly set LangSmith environment settings for tracing
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "true")
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
if os.getenv("LANGCHAIN_PROJECT"):
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

# Define prompt template
prompt = ChatPromptTemplate([
    ('system', 'you are a helpful AI assistant'),
    ('human', 'question: {question}')
])

def generate_response(query, llm, temperature, max_tokens):
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            return None, "GROQ_API_KEY not found in .env file."

        model = ChatGroq(
            model=llm,
            temperature=temperature,
            groq_api_key=api_key,
            max_tokens=max_tokens
        )
        parser = StrOutputParser()
        chain = prompt | model | parser
        result = chain.invoke({'question': query})
        return result, None
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

# Streamlit Interface
st.title("Q and A Chatbot (Free Groq LPU)")
query = st.text_input("What is your query?")

st.sidebar.title("Settings")

# Static manual model list from Groq documentation
llm = st.sidebar.selectbox('Select Model:', [
    'llama-3.3-70b-versatile',
    'llama-3.1-8b-instant',
    'openai/gpt-oss-120b',
    'openai/gpt-oss-20b',
    'qwen/qwen3.6-27b'
])

temperature = st.sidebar.slider("Select Temperature: ", min_value=0.0, max_value=2.0, value=0.8)
max_tokens = st.sidebar.slider("Tokens: ", min_value=50, max_value=500, value=100)

if st.button("Answer"):
    if query:
        with st.spinner("Generating response..."):
            response, error = generate_response(query, llm, temperature, max_tokens)
            if error:
                st.error(error)
            else:
                st.write(response)
    else:
        st.warning("Please enter a query.")