import unittest
from bad_code import function_should_crash


class TestFunc(unittest.TestCase):
    """Debugging this test and the debugger exits, no way to use the debug console, etc."""
    def test_crash(self):
        function_should_crash()