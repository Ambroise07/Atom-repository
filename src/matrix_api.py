"""

matrix api - 9, may 2026 - Gnabro Israel
----------------------------------------

READONLY_APIS: class design to access only the projects
it come with names, search, exist, first_neightboors, last_neightboors, coords, size_of.
   ATTRIBUES:
    - name: (EXCEPTED) the name of the project
    - coords: (RETURNED) the coordinates of the project in the projects matrix
    - first_neightboors: (RETURNED) a tuple of two strings that represent the names of the first projects wich come BEFORE this project with `name`.
    - last_neightboors: (RETURNED) a tuple of two strings that represent the names of the last projects wich come AFTER this project with `name`.
    - size_of: (RETURNED) the size of the project with `name`.
    - projects: (RETURNED) a list of all the projects names in the projects matrix.

    METHODS:
    - exist(name): return True if project with `name` is found in the `pmatrix` or the projects matrix else, False.
    - coords(name): return the coords of the projects.
    - search(name): search the project store with name into the projects matrix if not found, return None otherwise the project coordinates.
    - first_neightboors(name): return a tuple of two strings that represent the names of the first projects wich come BEFORE this project with `name`.  


EDIT_APIS: class design to access only the projects
it come with names, search, exist, first_neightboors, last_neightboors, coords, size_of.

"""

import numpy as np
import tools
import os




class READONLY_APIS:
    """ 
        class design to access only the projects
        it come with names, search, exist, first_neightboors,
        last_neightboors, coords, size_of.

    """



    def __init__(self, *kwargs):
        """ READONLY_PROJECT """ 
        self.file_path =  tools.get_abspath('datas/projects_matrix.npy')


 
    def exist(self, name):
        """
        return True if project with `name`
        is found in the `pmatrix` or the projects matrix 
        else, False.
        """
        projects = self.get_projects()

        # not useful to go far, there's no project.
        if projects.size == 0:
            raise ValueError("The projects matrix is empty.")

        # return answer...
        return True if  np.any(projects == name.encode('utf-8')) else False



    def coords(self, name):
        """
        return the coords of the projects.
        """
        pass


    def search(self, name):
        """ 
        search the project store with name
        into the projects matrix if not found, 
        return None otherwise the project coordinates.
        """
        pass



    def neightboors(self, name):
        """
        return a tuple of two strings that represent 
        the names of the first projects wich come BEFORE 
        this project with `name` and the last projects wich come AFTER
        this project with `name`.
        """

        if  not self.exist(name):
            raise ValueError("Project  {name} is not found in the projects matrix.")

        projects = self.get_projects()
        name_byte = name.encode('utf-8')  # Encode the name to bytes for comparison


        # if project is not found, index is < 0.
        # so index - 1 will be < 0 too. 
        index = projects.index(name_byte)
        _before = projects[index - 1] if index - 1 >= 0 else None
        _after = projects[index + 1] if index + 1 < len(projects) else None

        return (_before, _after)



    def first_neightboors(self, name):
        """
        return a tuple of two strings that represent 
        the names of the first projects wich come BEFORE 
        this project with `name`.
        """
        return self.neightboors(name)[0]



    def last_neightboors(self, name):
        """
        return a tuple of two strings that represent 
        the names of the last projects wich come AFTER
        this project with `name`.
        """
        return self.neightboors(name)[1]



    def size_of(self, name):
        """
        return the size of the project with `name`.
        if not found, raise NotFoundError
        """
        total_size, _ = tools.get_project_stats(tools.get_abspath(name))
        return total_size 



    def number_of_files(self, name):
        """
        return the number of files in the project with `name`.
        if not found, raise NotFoundError
        """
        _, file_count = tools.get_project_stats(tools.get_abspath(name))
        return file_count     



    def get_projects(self)->list:
        """ return projects database in `readonly mode ` """

        # open the file where projects matrix is stored
        if os.path.exists(self.file_path):
            projects_matrix = np.load(self.file_path, allow_pickle=True)
            return projects_matrix['project']

        else:
            return [] 






class EDIT_APIS:
    """ 
        class design to access only the projects
        it come with names, search, exist, first_neightboors,
        last_neightboors, coords, size_of.

    """



    def __init__(self, *kwargs):
        """ EDIT_APIS """ 
        self.readonly = READONLY_APIS(*kwargs)

        self.atomtype = [('project', 'S20'), 
                        ('version', 'S20'),
                        ('message', 'O'),
                        ('timestamp', 'M8[s]'),
                        ('file_count', 'i4'), 
                        ('total_size', 'f8'), 
                        ]
        


 
    def create(self, project: str, version: str, message: str):
        """
        create a numpy array.
        and add it to the projects matrix.

        -------------------------------------------
        Args:
             - project: the name of the project
             - version: the version of the project
             - message: the message of the project
        Return:
            None
        -------------------------------------------

        """

        # get the numbers  of files of the project
        files = self.readonly.number_of_files(project)

        # size of the project 
        size = self.readonly.size_of(project)

        # encode the message to integer
        message = tools.encode_string(message)

        # get the timestamp of the project
        timestamp = np.datetime64('now')

        # create a numpy array with the project data
        project_array = np.array([(project, version, message, timestamp, files, size)], dtype=self.atomtype)

 
        # add the project to the projects matrix
        self.add_project(project_array)




    def add_project(self, project: np.ndarray):
        """
        add the project to the projects matrix.

        -------------------------------------------
        Args:
             - project: the numpy array of the project to add.
        Return:
            None
        -------------------------------------------

        """

        # 1.open the files where projects matrix is stored
        if os.path.exists(self.readonly.file_path):
            try:
                current = np.load(self.readonly.file_path, allow_pickle=True)

                # 3.add the project to the projects matrix
                new_matrix = np.concatenate([current, project])

                # order the projects matrix by name
                new_matrix.sort(order=['project', 'timestamp']) 


            except Exception as e:
                print(f"Error occurred while loading existing matrix: {e}")
                new_matrix = project

    
        # 4.write the projects matrix to the file
        np.save(self.readonly.file_path, new_matrix, allow_pickle=True)
