import os
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader,UnstructuredMarkdownLoader, UnstructuredWordDocumentLoader, UnstructuredPowerPointLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()

def create_vector_db():
    
    data_path = os.getenv('DATA_PATH')
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".csv"):
            loader = CSVLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".md"):
            loader = UnstructuredMarkdownLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".docx"):
            loader = UnstructuredWordDocumentLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".doc"):
            loader = UnstructuredWordDocumentLoader(os.path.join(data_path,file))
            documents += loader.load()
        elif file.endswith(".pptx"):
            loader = UnstructuredPowerPointLoader(os.path.join(data_path,file))
            documents += loader.load()
            
    print(f"Processed {len(documents)} files")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    
    vector_store = Chroma.from_documents(
        documents=texts,
        embedding=OllamaEmbeddings(show_progress=True,model="nomic-embed-text"),
        persist_directory=os.getenv('DB_PATH')
    )
    
    vector_store.persist()
    
def main():
    """Main function to create the vector database."""
    create_vector_db()


if __name__ == "__main__":
    main()
    