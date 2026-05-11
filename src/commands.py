"""
Atom program design to make project with ease.

# create a project:
 `atom init .`  or  `atom init name`
 if the . is given the current dir is the project name
 otherwise, the project is the name given by the string `name`
 the project contains the `atom.proj`.


# remove a project:
 `atom remove .` remove the project. please the project to remove should be a 
 Atom project, which mean that it contains a `atom.proj` file.
 `atom remove name` will remove the project located at `name` id.

# save a session:
after a long coding session, save you're project as you do a commit one github.
`atom save session_message` or `atom save .` So you can enter : `atom save ajout des donnees`
or you can do `atom .`. Notice that, the last command will use the date and hour as session message.

# restart a project:
 with atom you can restart a removed project. Because atom use matrix to store
 you're project log, so you can acess it with easy.
 `atom search name` will make atom search for you're project. and then enter
 `atom restart session_name` to restart a session of you project.
 Note: A session is just a copy of you're project save with `atom save session_name`
 hack: write `atom init name` where the name is project's name that exist is the same as
 `atom search name`, my favorite hack! :) 

# Project size
 Any project have a maximun size of 2500. with mean that in the matrix of the 
 project (matrix use to store the session of one project ) have size 50 x 50.
 you can by your own update (increase or decrease ) this size.
 when this matrix is full, atom show you message like :
 `FullProject: space has run out for "name" `

# Remove session
 To have more space, use `atom save last ` wich will save the last of the current project.
 also `atom save name last `

# session's log
 1. Count a session with : `atom count name` or `atom count .`
 2. get the project date creation : `atom begin name` or `atom beguin .`
 3. get the free space : `atom free name` or `atom free .`
 

# End.
 if you love atom. email me at ambroiseisrael5@gmail.com or 
 run ` atom author ` to get more info.

"""

from core import BasicCommands


class AtomCommands(BasicCommands):
    
    def __init__(self, *kwargs):
        # TODO: create 
        # `Storage.get_projects`
        self.projects = Storage.get_projects()

    def atom_init(self, name: str ='.'):
        """ make or seek for a new project """

        # get the path of the project
        if name == '.':
            name = self.get_working_dir()
        else:
            try:
                name = self.get_path(name)
            except:
                # we will create the project in the next blocs
                pass


        is_created = False
        if name in self.projects.names:
            # go to the project 
            # located at name id 
            # for this project
            self.atom_goto(name)
            is_created = True
            return

        # because create_project need the project_name attribute
        self.project_name = name
        self.create_project() 

        message = self.get_message(8) if not is_created else self.get_message(10)

        #print(message)


    def remove(self, name):
        """ remove project store with id 'name' """
        if name in self.projects.names:
            self.projects.delete(name)


