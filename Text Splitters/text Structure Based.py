from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader  

loader = PyPDFLoader("dl-curriculum.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap=0,
)
result = splitter.split_documents( docs)
print(result[0].page_content)
print(len(result))
