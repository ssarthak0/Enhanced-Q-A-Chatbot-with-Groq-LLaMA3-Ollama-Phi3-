# 🧠 Enhanced Q&A Chatbot with Groq (LLaMA3)/ Ollama(Phi3)

This Streamlit application is an interactive Q&A chatbot powered by Groq's LLaMA3 and  Ollama's Phi3 models. Users can input questions and receive AI-generated responses, with customizable settings for model selection, temperature, and token limits.

---

## 🚀 Features

- **Model Selection**: `Llama3-8b-8192`
- **Adjustable Parameters**: Modify temperature and max token settings to control response creativity and length.
- **Secure API Key Input**: Enter your Groq API key securely via the sidebar.
- **Real-time Responses**: Get instant answers to your queries.

---

## 🛠️ Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ssarthak0/Enhanced-Q-A-Chatbot-with-Groq-LLaMA3-Ollama-Phi3-
   cd Enhanced-Q-A-Chatbot-with-Groq-LLaMA3-Ollama-Phi3-
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional
   ```

---

## 🧾 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

Once running, open your browser and navigate to `http://localhost:8501`. Enter your Groq API key in the sidebar, select your desired model and settings, and start asking questions!

---

## 📁 Project Structure

```
groq-qa-chatbot/
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 📄 Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- langchain-groq
- python-dotenv

Install all requirements using:

```bash
pip install -r requirements.txt
```

---

## 🤖 Example

**Question**: What is the capital of France?

**Answer**: The capital of France is Paris.

---

## 📚 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋‍♀️ Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 🔗 Links

- [Groq API Documentation](https://groq.com/docs/)
- [LangChain Documentation](https://docs.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---


