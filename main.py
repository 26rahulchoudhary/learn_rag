from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader, UnstructuredURLLoader
from dotenv import load_dotenv

load_dotenv()

# =========================
# DEFINITIONS (SAFE TO IMPORT)
# =========================
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_store = InMemoryVectorStore(embeddings)


# =========================
# INGEST FUNCTION (FIXED)
# =========================
def ingest_url(url: str):
    print(f"Loading: {url}")

    loader = WebBaseLoader(web_paths=(url,))
    docs = loader.load()

    # Fallback
    if not docs or not docs[0].page_content.strip():
        print("Using fallback loader...")
        loader = UnstructuredURLLoader(urls=[url])
        docs = loader.load()

    if not docs or not docs[0].page_content.strip():
        raise ValueError("Failed to extract content")

    print(f"Characters: {len(docs[0].page_content)}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )

    splits = splitter.split_documents(docs)
    print(f"Chunks: {len(splits)}")

    vector_store.delete()  # Clear existing data
    vector_store.add_documents(splits)

    print("Vector store updated")

    return splits


# =========================
# RETRIEVAL TOOL
# =========================
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query."""
    retrieved_docs = vector_store.similarity_search(query, k=3)

    if not retrieved_docs:
        return "No relevant context found", []

    serialized = "\n\n".join(
        f"{doc.page_content}" for doc in retrieved_docs
    )

    return serialized, retrieved_docs