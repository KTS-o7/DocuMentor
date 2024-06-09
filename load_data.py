# Import necessary modules
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()


def create_vector_db():
    """Create a vector database from PDF documents."""
    # Load documents from the specified directory
    loader = PyPDFDirectoryLoader(os.getenv('DATA_PATH'))
    documents = loader.load()
    print(f"Processed {len(documents)} pdf files")

    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    # Create a vector store from the document chunks
    vectorStore = Chroma.from_documents(
        documents=texts,
        embedding=OllamaEmbeddings(),
        persist_directory=os.getenv('DB_PATH')
    )

    # Persist the vector store to disk
    vectorStore.persist()


def main():
    """Main function to create the vector database."""
    create_vector_db()


if __name__ == "__main__":
    main()