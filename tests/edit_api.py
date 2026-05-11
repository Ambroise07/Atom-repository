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


from matrix_api import EDIT_APIS
from unittest import TestCase

class TestEditApi(TestCase):
    
    def test_create(self):
        edit_api = EDIT_APIS()
        project = "test_project"
        version = "1.0"
        message = "Initial commit"
        edit_api.create(project, version, message)

        # check if the project is created in the projects matrix
        readonly_api = edit_api.readonly
        projects = readonly_api.get_projects()
        self.assertTrue(len(projects) > 0)

    def test_add_project(self):
        pass



class TestEditApi2:
    def main(self):
        """ test again and again the edit api, but with a different approach """

        print('test de l\'edit api avec une approche différente : \n')
        print('création d\'un projet : \n')

        edit_api = EDIT_APIS()
        project = "test_project"
        version = "1.0"
        message = "Initial commit"
        edit_api.create(project, version, message)

        print(f'donees :  project : {project} \n version : {version} \n message : {message} \n')


        if os.path.exists(edit_api.readonly.file_path):
            print(f'le fichier {edit_api.readonly.file_path}  est detecté \n')

            try:
                current = np.load(edit_api.readonly.file_path, allow_pickle=True)
                print(f'les données du fichier sont :  {current} \n')

            except Exception as e:
                print(f"Error occurred while loading existing matrix: {e}")
           


if __name__ == "__main__":
    # unittest.main()

    #test_edit_api2 = TestEditApi2()
    #test_edit_api2.main()