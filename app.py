import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set Langsmith tracking (optional)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With GROQ"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("user", "Question: {question}")
    ]
)

# Function to generate response using Groq
def generate_response(question, groq_api_key, engine, temperature, max_tokens):
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model=engine,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI
st.title("🧠 Enhanced Q&A Chatbot with Groq (LLaMA3)")

# Sidebar settings
st.sidebar.title("🔧 Settings")
groq_api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")
engine = st.sidebar.selectbox("Select Groq Model", ["Llama3-8b-8192", "Mixtral-8x7b-32768"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main input section
st.write("Ask any question below 👇")
user_input = st.text_input("You:")

if user_input and groq_api_key:
    try:
        response = generate_response(user_input, groq_api_key, engine, temperature, max_tokens)
        st.write(f"**Answer:** {response}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
elif user_input:
    st.warning("⚠️ Please enter the Groq API Key in the sidebar.")
else:
    st.info("💬 Waiting for your question...")
