"""
tests for the readonly api of the matrix api.


"""

import pathlib
import sys
path = pathlib.Path(__file__).resolve().parent.parent / 'src'
sys.path.append(str(path))


import unittest
from apis import READONLY



class TestReadApi(unittest.TestCase):
    api = READONLY()



    def test_exist(self):
        self.assertEqual(self.api.exist("read"), False)


    def test_get_projects(self):
        """ 
        check if projects are created.
        if you want to print the projects
        or get size use one of the code bellow.
        """
        self.assertEqual(len(self.api.get_projects()), 2)
        

    def test_neightboors(self):
        """ test of the neightboors """
        # can't run this test because neightboors method has issue.
        self.assertEqual(len(self.api.neightboors('test_project')), 2)
        

    def test_first_neightboors(self):
        self.assertEqual(self.api.first_neightboors('test_project'), (None, None))


    def test_last_neightboors(self):
        self.assertEqual(self.api.last_neightboors('test_project'), (None, None))

    def test_search(self):
        self.assertIsNotNone(self.api.search('test_project'))

    def test_coords(self):
        self.assertIsNotNone(self.api.coords('test_project'))    


    def test_size_of(self):
        pass


    def test_number_of_files(self):
        pass




class PrintReadApiAtrributes:

    api = READONLY()


    def test_get_project(self):
        """ ... """
        print(len(self.api.get_projects()))



if __name__ == "__main__":
    unittest.main()
    #PrintReadApiAtrributes().test_get_project()
