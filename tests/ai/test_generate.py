from unittest.mock import patch

import pytest

from diego_utils.ai.generate import generate_response


class TestGenerateResponse:
    """
    Test suite for the `generate_response` function.
    This test suite includes the following tests:
    - `test_basic_generate_response`: Verifies that a simple question can be answered.
    - `test_non_normal_distribution`: Verifies that the p-value is less than 0.05 for data that does not follow a normal distribution.
    - `test_small_sample_size`: Verifies that the function returns a float for both d and p-value when given a small sample size.
    """

    @patch("diego_utils.ai.generate.HuggingFaceEndpoint")
    def test_basic_generate_response(self, mock_huggingface_endpoint):
        """
        Test the `generate_response` function to ensure it correctly interacts with the huggingfaceendpoint
        and returns the expected response.
        This test performs the following steps:
        1. Mocks the response from the huggingfaceendpoint to return "Paris".
        2. Calls the `generate_response` function with a sample question, fake hugging face API key, and model ID.
        3. Asserts that the response from `generate_response` is "Paris".
        4. Verifies that the huggingfaceendpoint was called with the correct parameters.
        5. Verifies that the `invoke` method of the huggingfaceendpoint was called with the correct question.
        Args:
            mock_huggingface_endpoint (Mock): A mock object for the huggingfaceendpoint class.
        """
        # Mock the response from the huggingfaceendpoint
        mock_instance = mock_huggingface_endpoint.return_value
        mock_instance.invoke.return_value = "Paris"

        question = "What is the capital of France?"
        hf_key = "fake_hf_key"
        model_id = "mistralai/Mistral-7B-Instruct-v0.3"

        response = generate_response(question, hf_key, model_id)

        # Assert that the response is as expected
        assert response == "Paris"

        # Assert that huggingfaceendpoint was called with the correct parameters
        mock_huggingface_endpoint.assert_called_once_with(
            repo_id=model_id,
            model_kwargs={"max_length": 512},
            temperature=0.1,
            token=hf_key,
        )

        # Assert that invoke was called with the correct question
        mock_instance.invoke.assert_called_once_with(question)

    def test_empty_question_raises_value_error(self):
        """
        Test that an empty question raises a ValueError.
        This test verifies that the `generate_response` function raises a
        `ValueError` when provided with an empty question string. The error
        message is expected to match "The question cannot be empty.".
        Args:
            self: The test instance.

        Raises
        ------
            ValueError: If the question is empty.
        """
        question = ""
        hf_key = "fake_hf_key"
        model_id = "mistralai/Mistral-7B-Instruct-v0.3"

        with pytest.raises(ValueError, match="The question cannot be empty."):
            generate_response(question, hf_key, model_id)


if __name__ == "__main__":
    pytest.main()
