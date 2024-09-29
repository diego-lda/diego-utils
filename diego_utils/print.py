"""Contains some test functions for printing."""


def say_diego():
    """Displays the name of Diego.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Displays on the screen the name "Diego"
    """
    print("Hello Diego")


def say_hello(
    input_str: str = "Default",
):
    """Displays the name passed as input.

    Parameters
    ----------
    input_str
        The string to be returned after Hello.

    Returns
    -------
    str
        Retursn a string, which is the input plus a hello at the start.
    """
    new_str = f"Hello {input_str}"
    return new_str
