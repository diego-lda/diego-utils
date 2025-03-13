"""Module to generates responses using a pre-trained locally run language model."""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Choose your model (e.g., Mistral-7B, DeepSeek, Llama-3, etc.)
MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"  # Change this if needed

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,  # Use float16 for efficiency if using a GPU
    device_map="auto",  # Automatically selects GPU if available
)


# Define a function to generate responses
def generate_response(question):
    """
    Generate a response to the given question using the pre-trained model.

    Args:
        question (str): The input question to generate a response for.

    Returns
    -------
        str: The generated response.
    """
    input_ids = tokenizer(question, return_tensors="pt").input_ids.to(model.device)
    output = model.generate(input_ids, max_new_tokens=200)
    return tokenizer.decode(output[0], skip_special_tokens=True)


# Example usage
if __name__ == "__main__":
    user_input = "What is the capital of France?"
    response = generate_response(user_input)
    print(response)
