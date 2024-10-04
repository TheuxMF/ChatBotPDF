# ChatBotPDF
Chat Bot usando o Retrieve Argument Generation(RAG)

O que é RAG?
RAG, ou Retrieval Augmented Generation, é uma técnica que combina a capacidade dos modelos de linguagem de grande porte (LLMs) com a recuperação de informações relevantes de um banco de dados. Em vez de depender apenas da sua própria base de conhecimento, o LLM pode acessar e processar informações externas para fornecer respostas mais precisas e contextualmente relevantes. Isso aumenta a precisão das respostas utilizando informações contextuais relevantes contidas no PDF, também tornando o mais versátil podendo responder perguntas de várias área de conhecimento dependendo da qualidade do PDF

Como funciona um chatbot com RAG?

1. Chatbot recebe um PDF e faz o processamento dos textos do arquivo para transformar em embeddings e armazena em um banco de dados vetorial 
2. Em sequida ele recebe uma pergunta do usuário.
3. A recuperação de informações relevantes faz o sistema utilizar um mecanismo de busca, para encontrar os trechos de texto mais relevantes no banco de dados que se relacionam com a pergunta. 
4. O LLM , recebe a pergunta original e os trechos relevantes recuperados. Ele processa essas informações e gera uma resposta coerente e informativa.
5. A resposta gerada pelo LLM é apresentada ao usuário.


![DBBLOG-3334-image001](https://github.com/user-attachments/assets/c6e9c15c-93e4-4a5a-a92e-9ebad3adcadc)
