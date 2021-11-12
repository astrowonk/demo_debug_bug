import unittest
from bad_code import function_should_crash


class TestFunc(unittest.TestCase):
    """Debugging this test"""
    def test_crash(self):
        function_should_crash()