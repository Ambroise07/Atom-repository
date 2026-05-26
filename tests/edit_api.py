"""
tests for the edit api of the matrix api.

"""

import sys
import numpy as np
import os
import pathlib
import unittest

path = pathlib.Path(__file__).resolve().parent.parent / 'src'
sys.path.append(str(path))


from apis import EDIT
from unittest import TestCase

class TestEditApi(TestCase):
    
    def test_create(self):
        api = EDIT()
        project = "test_project"
        version = "1.0"
        message = "Initial commit"
        api.create(project, version, message)

        # check if the project is created in the projects matrix
        projects = api.readonly.get_projects()
        self.assertTrue(len(projects) > 0)

    def test_delete(self):
        api = EDIT()
        project = "test_project"
        api.delete(project)

        # check if the project is removed from the projects matrix
        projects = api.readonly.get_projects()
        self.assertFalse(len(projects) > 0)



class TestEditApi2:
    def main(self):
        """ test again and again the edit api, but with a different approach """

        print('test de l\'edit api avec une approche différente : \n')
        print('création d\'un projet : \n')

        api = EDIT()
        project = "test_project"
        version = "1.0"
        message = "Initial commit"
        api.create(project, version, message)

        print(f'donees :  project : {project} \n version : {version} \n message : {message} \n')


        if os.path.exists(api.readonly.file_path):
            print(f'le fichier {api.readonly.file_path}  est detecté \n')

            try:
                current = np.load(api.readonly.file_path, allow_pickle=True)
                print(f'les données du fichier sont :  {current} \n')

            except Exception as e:
                print(f"Error occurred while loading existing matrix: {e}")
           


if __name__ == "__main__":
    unittest.main()
    #test_edit_api2 = TestEditApi2()
    #test_edit_api2.main()