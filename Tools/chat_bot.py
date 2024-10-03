from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def data_processining(path):
    loader = PyPDFLoader(path)

    docs_split = loader.load()
    hf_embeddings = HuggingFaceEmbeddings()
    text_splitter = SemanticChunker(hf_embeddings, breakpoint_threshold_type="standard_deviation") 
    chunks = text_splitter.split_documents(docs_split)

    return chunks

def create_vectorstores(chunks):
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model='nomic-embed-text')
    )
    retriever = vectorstore.as_retriever()

    return retriever