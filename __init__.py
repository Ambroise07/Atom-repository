"""
init file
"""

# append this module in the sys variable
import sys
import pathlib

module_path = pathlib.Path()


# varables
messages = {
	
	'fr':{
		'1':'Entrez le nom du project: ',
		'2': 'Choisissez le repectoire: \n (1) repetoire courant \n (2) entrez le chemin ',
		'3': 'chemin absolue ou relatif du repectoire :\n'
		},
	
	'en':{
		'1':'Entrer the project\'s name: ',
		'2': 'Choose the directory: \n (1) current working directory \n (2) entrer the directory path ',
		'3': 'absolut or relative path of project:\n'
		}
	
	}

# default
language = "none"


