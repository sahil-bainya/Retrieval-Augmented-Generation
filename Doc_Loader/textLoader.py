from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

loader = TextLoader("Doc_Loader/sample.txt")

docs = loader.load()

# print(type(docs))  # <-- list
# print(docs[0])
# print(docs[0].page_content)
# print(docs[0].metadata)
# docs will have two things
# 1. page_content
# 2. metadata

prompt = PromptTemplate(
    template="Summarize the following text \n {text}", input_variables=["text"]
)

chain = prompt | model | parser

result = chain.invoke({"text": docs[0].page_content})

print(result)
