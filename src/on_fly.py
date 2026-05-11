"""
date : 27/04/2026
author: Gnabro Israel

"""

from core import BasicCommands


class Automate(BasicCommands):
	
	def __init__(self, *kwargs):
		super(Automate, self).__init__()

		self.get_ags()
		self.create_project()
		

	def get_ags(self):
		""" get the argument typed in the cmd """
		
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
				print(self.get_message(9))
				continue
			break
		
		
		match self.path:
			case 1:
				self.path = self.get_working_dir()
			case _:
				path = input(self.get_message(3))
				self.path = self.get_absolute_path(path)

		
		# create virtual environnement:
		can_create_venv = input(self.get_message(4))
		if can_create_venv.strip().lower() in  ['o', 'y']:
			self.create_virtual_env()
					

if __name__ == '__main__':
	automatebot = Automate()

