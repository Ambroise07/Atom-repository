"""
core functionnalities of inline and commands.

author : Gnabro Israel
date: 6 - 05 - 2026

"""

import subprocess
import tools
import pathlib
import shutil

from __init__ import messages 




class BasicCommands:

    def __init__(self, *kwargs):
        self.lang: str = tools.get_lang()



    def get_working_dir(self) -> pathlib.Path:
        """ return Path.cwd() """
        return pathlib.Path.cwd()


    def get_absolute_path(self, path)-> pathlib.Path:
        """ return the absolute path """
        return pathlib.Path(path).absolute()



    def get_path(self, folder:str)->pathlib.Path:
        """ return the path of folder """
        return self.get_absolute_path(folder)


    def get_message(self, msg_id):
		""" return message to display in the cmd """
		# first get the current language of the system.
		# language
		id = str(msg_id)
		return messages[self.lang][id]


    def create_files(self):
		""" creates files of any packages..."""
		temp_path = pathlib.Path(__file__).parent.resolve() / 'template'

		for folder in temp_path.iterdir():
			if folder.is_dir():
				shutil.copytree(folder, self.project_dir / folder.name, dirs_exist_ok=True)
			else:
				shutil.copy2(folder, self.project_dir / folder.name) 



    def create_project(self):
		""" create the project """
		# the project_name is get by the get_args function
		self.path = self.path if hasattr(self, 'path') else pathlib.Path.cwd() 
		self.project_dir = self.path / self.project_name
		
		# Create the basic structure
		(self.project_dir / 'src').mkdir(parents=True, exist_ok=True)
		(self.project_dir / 'tests').mkdir(parents=True, exist_ok=True)
		
		self.packages = self.project_dir 

        self.create_files()            



    def create_virtual_env(self):
		""" create virtual environnement """
		venv_name = input(self.get_message(5))
		
		if not venv_name.strip() == '':
			subprocess.run(["python3", "-m", "venv", venv_name], check=True)
			print(self.get_message(6))



    def activate_virtual_env(self):
		""" activate the virtual environnement """
		subprocess.run(["source", 
			            str(self.project_dir / 'venv' / 'bin' / 'activate')], 
						shell=True, check=True)                         