"""
date : 27/04/2026
author: Gnabro Israel

"""

import pathlib
import shutil
import argparse
import subprocess

from __init__ import messages 



class Automate:
	
	def __init__(self, *kwargs):
		self.get_ags()
		self.create_project()
		
	def get_ags(self):
		""" get the argument typed in the cmd """
		
		# the language of the system
		self.lang = 'en'

		# default way to make a project insead the currrent working directory
		# with default language
		args = argparse.ArgumentParser()
		args.add_argument('--name')
		filename = args.parse_args()
		if filename.name:
			self.project_name = filename.name 
			return 
		
		# otherwise create the project by informations
		self.project_name = input(self.get_message(1))
		while True:
			self.path = int(input(self.get_message(2)))
			if not (self.path in [1, 2]):
				print('veuillez entrez les chiffres  1 ou 2 pour le choix')
				continue
			break
		
		match self.path:
			case 1:
				self.path = pathlib.Path.cwd()
			case _:
				path = input(self.get_message(3))
				self.path = pathlib.Path(path).absolute()
		
		# create virtual environnement:
		can_create_venv = input(self.get_message(4))
		if can_create_venv.strip().lower() == 'o':
			self.create_virtual_env()
		
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
		
	def create_virtual_env(self):
		""" create virtual environnement """
		venv_name = input(self.get_message(5))
		
		if not venv_name.strip() == '':
			subprocess.run(["python3", "-m", "venv", venv_name], check=True)
		
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


if __name__ == '__main__':
	automatebot = Automate()

