import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

loader = DirectoryLoader("./data/new_articles", glob="*.txt", loader_cls=TextLoader)


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

document = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=20,
    separators=["\n\n", "\n"]
)

documents = text_splitter.split_documents(document)

print(f"Number of documents: {len(documents)}")

embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"), model="text-embedding-3-small")

vector_db = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./db/chroma_db_lang_chain"
)
print(f"Number of documents in vector db: {vector_db._collection.count()}")

retriever = vector_db.as_retriever(search_kwargs={"k": 3})

print(retriever.get_relevant_documents("how much did microsoft raise?"))






