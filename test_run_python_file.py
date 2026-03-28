import unittest
from functions.run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_calculator_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_calculator_main_args(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_calculator_test(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_calculator_main_path(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_calculator_no_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)

    def test_calculator_lorem(self):
        result = run_python_file("calculator", "lorem.txt")
        print(result)


if __name__ == "__main__":
    unittest.main()