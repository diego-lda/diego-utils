"""
Module containing the functions to build a list of Document objects from a dict.

It creates and loads a FAISS database using HuggingFace embeddings.
It also fetches similar text from the FAISS database based on a query.
"""

from langchain.schema import Document
from langchain.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


def build_content_list(content_dict: dict) -> list:
    """
    Convert a dictionary of content into a list of Document objects.

    Args:
        content_dict (dict): A dictionary where keys are file paths and values are
                            dictionaries containing metadata information.

    Returns
    -------
        list: A list of Document objects created from the content dictionary.
    """
    documents = [
        Document(
            page_content=value["text"],
            metadata={
                "author": value["author"],
                "date": value["date"],
                "file_path": key,
            },
        )
        for key, value in content_dict.items()
    ]

    return documents


def create_faiss_db(model: str, documents: list, store_path: str = False) -> None:
    """
    Create a FAISS database from a list of documents and save it locally.

    Args:
        model (str): The name of the embedding model to use.
        documents (list): A list of Document objects to be indexed.
        store_path (str, optional): The local path to save the FAISS database.
                        Defaults to False.

    Returns
    -------
        None
    """
    embeddings = HuggingFaceEmbeddings(model_name=model)
    faiss_db = FAISS.from_documents(documents, embeddings)

    if store_path != False:
        # Save the FAISS database locally
        faiss_db_path = store_path
        faiss_db.save_local(faiss_db_path)


def load_faiss_db(store_path: str, model: str) -> FAISS:
    """
    Load a FAISS database from a local path.

    Args:
        store_path (str): The local path where the FAISS database is stored.
        model (str): The name of the embedding model to use.

    Returns
    -------
        FAISS: The loaded FAISS database.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model)
    faiss_db = FAISS.load_local(
        store_path,
        embeddings,
        allow_dangerous_deserialization=True,
    )

    return faiss_db


def fetch_similar(query: str, faiss_db: FAISS) -> list:
    """
    Fetch similar documents from the FAISS database based on a query.

    Args:
        query (str): The query string to search for similar documents.
        faiss_db (FAISS): The FAISS database to search in.

    Returns
    -------
        list: A list of Document objects that are similar to the query.
    """
    results = faiss_db.similarity_search(query, k=2)

    return results


if __name__ == "__main__":
    import os

    # Load the dictionary of documents
    base_information = {
        "pdf_file_1": {
            "author": "Joe Bloggs",
            "date": "01/01/2024",
            "text": "The cat sat on the mat.",
        },
        "pdf_file_2": {
            "author": "Peter Sticks",
            "date": "21/11/2024",
            "text": "The dog barked at the moon.",
        },
        "pdf_file_3": {
            "author": "Alice Apples",
            "date": "15/04/2024",
            "text": "The bird sang a song.",
        },
    }

    # Convert them to a list of relevant entries of the Document class
    documents = build_content_list(base_information)

    # Use the desired embedding model to produce a FAISS index database with metadata
    model = os.getenv("embedding_model")
    faiss_db_path = os.getenv("embedding_store")
    faiss_database = create_faiss_db(
        model=model,
        documents=documents,
        store_path=faiss_db_path,
    )

    # Load the faiss_database
    loaded_faiss_db = load_faiss_db(store_path=faiss_db_path, model=model)

    # Query the FAISS index
    query = "Where is the cat?"
    similar = fetch_similar(query=query, faiss_db=loaded_faiss_db)

    # Print results
    print(f"Query: {query}")
    for i, match in enumerate(similar):
        print(f"Result {i + 1}:")
        print(f"Document: {match.page_content}")
        print(f"Metadata: {match.metadata}")
