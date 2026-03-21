# functions/test_get_info_files.py

import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_calculator_dot(self):
        result = get_files_info("calculator", ".")
        print(result)

    def test_calculator_pkg(self):
        result = get_files_info("calculator", "pkg")
        print(result)

    def test_calculator_bin(self):
        result = get_files_info("calculator", "/bin")
        print(result)

    def test_calculator_dotdot(self):
        result = get_files_info("calculator", "../")
        print(result)
    

if __name__ == "__main__":
    unittest.main()