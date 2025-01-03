import numpy as np
import pytest

from diego_utils.metrics.distributions import ks_test_with_normal


class TestKSTestWithNormal:
    """
    Test suite for the `ks_test_with_normal` function.
    This test suite includes the following tests:
    - `test_normal_distribution`: Verifies that the p-value is greater than 0.05 for data that follows a normal distribution.
    - `test_non_normal_distribution`: Verifies that the p-value is less than 0.05 for data that does not follow a normal distribution.
    - `test_small_sample_size`: Verifies that the function returns a float for both d and p-value when given a small sample size.
    """

    def test_normal_distribution(self):
        """
        Test the Kolmogorov-Smirnov test for data that follows a normal distribution.

        This test generates data from a normal distribution with mean 0 and standard
        deviation 1, and then applies the Kolmogorov-Smirnov test to check if the data
        follows a normal distribution. The test asserts that the p-value is greater than
        0.05, indicating that the null hypothesis (data follows a normal distribution)
        cannot be rejected.

        Raises
        ------
            AssertionError: If the p-value is not greater than 0.05.
        """
        # Test with data that follows a normal distribution
        rng = np.random.default_rng()
        normal_data = rng.normal(loc=0, scale=1, size=1000)
        d, p_value = ks_test_with_normal(normal_data)
        assert (
            p_value > 0.05
        ), "The p-value should be greater than 0.05 for normal distribution data"

    def test_non_normal_distribution(self):
        """
        Test the Kolmogorov-Smirnov test with data that does not follow a normal distribution.

        This test generates a dataset of 1000 samples from a uniform distribution
        between -1 and 1, and then applies the Kolmogorov-Smirnov test to check
        if the data follows a normal distribution. The test asserts that the
        p-value is less than 0.05, indicating that the data does not follow a
        normal distribution.
        """
        # Test with data that does not follow a normal distribution
        rng = np.random.default_rng()
        non_normal_data = rng.uniform(low=-1, high=1, size=1000)
        d, p_value = ks_test_with_normal(non_normal_data)
        assert (
            p_value < 0.05
        ), "The p-value should be less than 0.05 for non-normal distribution data"

    def test_small_sample_size(self):
        """
        Test the Kolmogorov-Smirnov test with a small sample size.

        This test generates a small sample of data from a normal distribution
        and performs the Kolmogorov-Smirnov test to compare the sample with
        a normal distribution. It then asserts that the test statistic (d)
        and the p-value are both floats.

        Raises
        ------
            AssertionError: If the test statistic (d) or the p-value is not a float.
        """
        # Test with small sample size
        rng = np.random.default_rng()
        small_data = rng.normal(loc=0, scale=1, size=10)
        d, p_value = ks_test_with_normal(small_data)
        assert isinstance(d, float), "d should be a float"
        assert isinstance(p_value, float), "p_value should be a float"


if __name__ == "__main__":
    pytest.main()
