from Tools.chat_bot import data_processining 
from Tools.chat_bot import create_vectorstores
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

if __name__ == "__main__":
    model = ChatOllama(model='gemma2:2b')
    patch_pdf = "caminho do pdf"

    docs = data_processining(patch_pdf)
    retriever = create_vectorstores(docs)

    prompt_templat = """Responda à pergunta com base apenas no seguinte contexto:
    {context}
    Pergunta: {question}
    """
    prompt = ChatPromptTemplate.from_template(prompt_templat)
    chain = ({'context': retriever, 'question': RunnablePassthrough()} |
                    prompt | model | StrOutputParser())
    while True:
        question = input("Digite a pergunta : ")
        print("Pensando:\n")
        print(chain.invoke(question))