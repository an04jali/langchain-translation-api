🚀 LangChain Translation API

A simple LLM-powered Translation API built using FastAPI + LangChain (LCEL) + Groq (Llama 3.1).
This project demonstrates how to create a production-style AI API server using modern GenAI tools.

📌 Features

🌐 Translate text into any language

⚡ Fast inference using Groq LLM (Llama 3.1)

🔗 LangChain LCEL pipeline (Prompt → Model → Parser)

🚀 FastAPI backend with LangServe routes

📡 REST API ready (/chain/invoke)

🧠 Clean modular chain architecture

🔐 Environment variable based secret handling

🛠 Tech Stack

Python

FastAPI

LangChain (LCEL)

Groq LLM (Llama 3.1)

LangServe

Uvicorn

python-dotenv

📂 Project Structure
langchain-translation-api/
│
├── serve.py              # FastAPI + LangChain server
├── requirements.txt      # Dependencies
├── .env                  # API keys (not pushed to GitHub)
├── .gitignore
└── README.md
⚙️ Setup & Run Locally
1️⃣ Clone repo
git clone https://github.com/YOUR_USERNAME/langchain-translation-api.git
cd langchain-translation-api
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Create .env

Create .env file:

GROQ_API_KEY=your_groq_api_key_here

⚠️ Never share .env publicly.

5️⃣ Run server
python serve.py

Server will start at:

http://localhost:8000
🧪 Test API

Open Swagger UI:

http://localhost:8000/docs

Use endpoint:

POST /chain/invoke

Request body:

{
  "input": {
    "language": "French",
    "text": "Hello, how are you?"
  }
}
🔄 API Flow
User Input → Prompt Template → Groq LLM → Output Parser → API Response
🔐 Security
API keys stored in .env

.env excluded via .gitignore

No secrets committed to repository

Output can be see in postman api also. 


Open:

http://localhost:8000/docs

Use endpoint:

POST /chain/invoke

Body:

{
  "input": {
    "language": "French",
    "text": "Hello, how are you?"
  }
}
