import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_calculator_lorem(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

    def test_calculator_pkg(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

    def test_calculator_temp(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)

if __name__ == "__main__":
    unittest.main()