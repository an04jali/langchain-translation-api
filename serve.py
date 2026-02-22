# ================================
# FastAPI + LangChain + Groq Server
# ================================

# ---- Imports ----
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from dotenv import load_dotenv


# ---- Load environment variables (.env) ----
load_dotenv()

# Get Groq API key from .env
groq_api_key = os.getenv("GROQ_API_KEY")


# ---- Initialize LLM Model (Groq) ----
# ⚠️ Use a currently supported model name
model = ChatGroq(
    model="llama-3.1-8b-instant",   # Change if needed
    groq_api_key=groq_api_key
)


# ================================
# 1. Create Prompt Template
# ================================

# System instruction template
system_template = "Translate the following into {language}:"

# Create structured chat prompt
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])


# ================================
# 2. Output Parser (Convert LLM → Text)
# ================================
parser = StrOutputParser()


# ================================
# 3. Create LCEL Chain
# ================================
# Flow: Prompt → Model → Parser
chain = prompt_template | model | parser


# ================================
# 4. Create FastAPI App
# ================================
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Simple API server using LangChain + Groq"
)


# ================================
# 5. Add LangServe Routes
# ================================
# This automatically creates API endpoint:
# POST /chain/invoke
add_routes(
    app,
    chain,
    path="/chain"
)


# ================================
# 6. Run Server
# ================================
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)