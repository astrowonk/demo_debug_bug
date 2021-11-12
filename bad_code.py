def function_should_crash():
    """
    This function should crash
    """

    print("Hello")

    x = 1 / 0

    print("Goodbye")


if __name__ == "__main__":

    # Debugging this file and the debugger keeps active after the error, as expected.
    function_should_crash()
