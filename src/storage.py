"""
store projects with a numpy array (for their names)
and use the binary method to compress the data (the code source wrote).

design by Gnabro Israel.

"""
import numpy as np

class Storage:

    def __init__(self, *kwargs):
        pass


    def get_projects(self)->Storage:
        """ return projects database in `readonly mode ` """
        # of course you wish 
        return READONLY_PROJECT()