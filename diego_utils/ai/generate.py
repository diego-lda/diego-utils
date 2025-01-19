"""Module to generate LLM-based responses.

The module uses the Hugging Face API to generate responses from a large language model.
"""

import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint


def generate_response(
    question: str,
    hf_key: str,
    model_id: str = "mistralai/Mistral-7B-Instruct-v0.3",
) -> str:
    """Generates a response from the LLM model.

    Args:
        question (str): The question to ask the model.
        hf_key (str): The Hugging Face API key.
        model_id (str, optional): The LLM ID. Defaults to "Mistral-7B-Instruct-v0.3".

    Returns
    -------
        str: The response from the model.
    """
    # Check if the question is empty
    if not question.strip():
        empty_response = "The question cannot be empty."
        raise ValueError(empty_response)

    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        model_kwargs={
            "max_length": 512,
        },
        temperature=0.1,
        token=hf_key,
    )

    # Invoke the model with your question
    response = llm.invoke(question)

    return response


if __name__ == "__main__":
    # Load the token for Hugging Face
    load_dotenv()
    sec_key = os.getenv("HF_TOKEN")
    sample_question = "What is the capital of France?"
    response = generate_response(question=sample_question, hf_key=sec_key)
    print(response)
