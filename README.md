# 🚀 Startup Idea Generator

Generate AI-powered startup ideas based on your interests using LangChain and Groq, and run the app via Streamlit.

## 🧠 Features

- Input a problem, topic, or area of interest
- Get a unique startup idea with a brief description
- Powered by LangChain and Groq LLM
- Simple and clean Streamlit web UI

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — for building the interactive frontend
- [LangChain](https://www.langchain.com/) — for LLM chaining and prompt templates
- [Groq API](https://console.groq.com/) — for fast, cheap inference with open models like LLaMA 3

---

## 📂 Project Structure

startup_generator/
├── .env # Stores the GROQ_API_KEY (not to be committed)
├── main.py # Streamlit app entry point
├── langchain_helper.py # Handles LangChain logic and prompt setup
├── requirements.txt # Required Python dependencies

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mallikharjun9999/startup_suggest
cd startup_generator

Install Dependencies

pip install -r requirements.txt

Run the App
streamlit run main.py

Open http://localhost:8501 in your browser.
