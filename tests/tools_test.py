import pathlib
import sys
path = pathlib.Path(__file__).resolve().parent.parent / 'src'
sys.path.append(str(path))


import unittest
from tools import get_project_stats

class TestTools(unittest.TestCase):

    _tools = get_project_stats('datas')

    def test_get_project_stats(self):
        """ get the stats of the project """
        
        # get the stats of the project
        self.assertIsInstance(self._tools[1], int)
        self.assertIsInstance(self._tools[0], int)


if __name__ == '__main__':
    unittest.main()        