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
		'3': 'chemin absolue ou relatif du repectoire :\n',
		'4':'creer un environnement virtuel ? (O/N) :\n',
		'5':'nom de l\'environnement virtuel : \n',
		'6':'environnement virtuel créé avec succès',
		'7':'veuillez patienter pendant que l\'environnement virtuel est en cours de création...',
		'8':'le projet a été créé avec succès',
		'9':'veuillez entrez les chiffres  1 ou 2 pour le choix',
		'10':'project déjà initialisé'
		
		},
	
	'en':{

		'1':'Entrer the project\'s name: ',
		'2': 'Choose the directory: \n (1) current working directory \n (2) entrer the directory path ',
		'3': 'absolut or relative path of project:\n',
		'4':'create a virtual environnement ? (Y/N) :\n',
		'5':'virtual environnement name: \n',
		'6':"virtual environnement created successfully",
		'7':'please wait while the virtual environnement is being created...',
		'8':'the project has been created successfully',
		'9':'bad choice, please pressed 1 or 2'

		}
	
	}

# default
language = "none"


