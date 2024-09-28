"""Tests for the print.py module."""

from diego_utils.print import say_diego, say_hello


class TestSayDiego:
    """Tests for the say_hello() function."""

    def test_say_diego(self, capsys):
        """Test that the say_diego function prints "Hello Diego" to stdout."""
        # Call the function
        say_diego()

        # Capture the output
        captured = capsys.readouterr()

        # Assert that the output is as expected
        assert captured.out == "Hello Diego\n"


class TestSayHello:
    """Tests for the say_hello() function."""

    def test_default_say_hello(self):
        """Test whether say_hello() prints what is expected without input."""
        default_say = say_hello()
        assert default_say == "Hello Default"
