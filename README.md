# 📊 Financial News AI Agent

An AI-powered application that analyzes financial news articles and answers user queries using Retrieval-Augmented Generation (RAG) with LangChain and Google Gemini.

---

## 🚀 Features

* 🔗 Load and analyze any financial/news article via URL
* 🤖 AI-powered question answering using Gemini
* 🧠 Context-aware retrieval using vector embeddings
* 📊 Structured responses (Summary, Key Points, Impact)
* ⚡ Streamlit-based interactive UI

---

## 🏗️ Tech Stack

* **LLM**: Google Gemini (via LangChain)
* **Framework**: LangChain
* **Vector Store**: InMemoryVectorStore
* **Frontend**: Streamlit
* **Parsing**: BeautifulSoup, Unstructured

---

## 📁 Project Structure

```
project/
│
├── main.py        # ingestion + vector store + retrieval tool
├── agent.py       # agent setup and prompt
├── app.py         # Streamlit UI
├── requirements.txt
└── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Add Environment Variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

### 5. Run the App

```
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a news article URL
2. Content is extracted and split into chunks
3. Embeddings are generated and stored
4. User asks a question
5. Relevant context is retrieved
6. Gemini generates a structured answer

---

## 📸 Example Use Cases

* 📈 Analyze stock-related news
* 🏦 Understand financial reports
* 🧾 Extract key insights from articles
* 💡 Get quick summaries and impact analysis

---

## 🔮 Future Improvements

* Persistent vector database (FAISS/Chroma)
* Multi-article comparison
* Chat-based UI
* Source citations
* Deployment (Streamlit Cloud / Docker)

---

## 👨‍💻 Author

Rahul Choudhary

---

## ⭐ If you found this useful, consider giving it a star!
