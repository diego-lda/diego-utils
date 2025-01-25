"""Module to generate LLM-based responses.

The module uses the Hugging Face API to generate responses from a large language model.
"""

import os

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint


def generate_response(
    question: str,
    hf_key: str,
    model_id: str = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
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
    # sample_question = "What is the capital of France?"
    # response = generate_response(question=sample_question, hf_key=sec_key)
    # print(response)

    from huggingface_hub import InferenceClient

    client = InferenceClient(api_key=sec_key)

    messages = [
        {"role": "user", "content": "Can you generate a training plan for cycling?"},
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        messages=messages,
        max_tokens=500,
    )

    print(completion.choices[0].message)

    # Use a pipeline as a high-level helper
    from transformers import pipeline

    messages = [
        {"role": "user", "content": "Who are you?"},
    ]
    pipe = pipeline(
        "text-generation",
        model="deepseek-ai/DeepSeek-R1",
        trust_remote_code=True,
    )
    pipe(messages)
