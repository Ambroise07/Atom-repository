"""
tests for the readonly api of the matrix api.


"""
import unittest
import pathlib
import sys

import matrix_api.READONLY_APIS as READONLY_APIS 


path = pathlib.Path(__file__).resolve().parent.parent / 'src'
sys.path.append(str(path))

class TestReadApi(unittest):
    
    def test_exist(self):
        pass

    def test_neightboors(self):
        pass

    def test_first_neightboors(self):
        pass

    def test_last_neightboors(self):
        pass

    def test_size_of(self):
        pass

    def test_number_of_files(self):
        pass

    def test_get_projects(self):
        pass



if __name__ == "__main__":
    pass