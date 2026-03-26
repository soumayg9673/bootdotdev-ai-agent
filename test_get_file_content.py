import unittest
from functions.get_file_content import get_file_content


class TestGetFilesContent(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_calculator_lorem(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)

    def test_calculator_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_calculator_pkgcalc(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_calculator_bincat(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

    def test_calculator_notexist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)
    

if __name__ == "__main__":
    unittest.main()