from langchain_community.document_loaders import WebBaseLoader,TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

url='https://www.geeksforgeeks.org/computer-networks/computer-network-tutorials/'
loader = WebBaseLoader(url)

docs=loader.load()

prompt = PromptTemplate(
    template='answer the question -{question} \n from the following text (if the answer is not exist in this text then say NO)- {text}',
    input_variables=['question','text']
)

chain = prompt | model | parser
question = input('Ask a question : ')
result = chain.invoke({'question':question,'text':docs[0].page_content})

print(result)