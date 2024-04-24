# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# .env 파일 로드
# from dotenv import load_dotenv
# load_dotenv()

# 랭체인
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

import streamlit as st
import tempfile
import os

st.title("Leaning Streamlit")
st.write("---")

