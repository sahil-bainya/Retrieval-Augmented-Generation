from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",  # path of the directory
    glob="*.pdf",  # files of that directory those will be included
    loader_cls=PyPDFLoader,  # loader that will load the pdfs of that directory
)

# docs = loader.load() <-- Resource is loaded immediately when needed/page starts.

docs = loader.lazy_load() # <-- 	Resource is loaded only when actually needed.

for document in docs:
    print(document)

