
"""
# 04-03-2026: usefull functions.
# 07-04-2026: merge_file added
# 08/04/2026 : choice_min and choice_max added.

"""
#some useful functions.
from pathlib import Path
from collections import Counter

import locale
import time
import math
import json
import re
import os



def get_abspath(path):
        """ 
        return the absolut path of a file
        
        I prefer use the absolut path because, 
        working with the notepad++ shortcut change directory 
        when running script.
        """
        base_path = Path(__file__).resolve().parent
        
        return base_path/path
  
  
        
def clean(text:str):

        """
        clean the text by removing ponctuation,
        making it in lower case, removing space and so on.
        """
        
        # make the text in lower case
        text = text.lower()
        
        # remove ponctuation.
        text = re.sub(r'[*.?,/\$[/] "]', '', text)
        
        # remove space
        text = re.sub(r'\s +', ' ', text).strip()
        
        # replace i. by space. where i is a number
        text = re.sub(r'\d+', '\n', text)
        
        # here I add  space arround  emojis.
        text = re.sub(r'([^\w\s])', r' \1 ', text)
        
        return text
        
   
   
def clean_data(raw_dpath:str, clean_dpath:str, debug=False):
        """ 
        clean text store in the CLEAN_DATA_PATH 
        (clean_dpath) the text of  RAW_DATA_PATH (raw_dpath) 
        'cls' means this class.
        """
        
        raw_dpath = get_abspath(raw_dpath)
        clean_dpath = get_abspath(clean_dpath)
        
        
        with open(raw_dpath, "r") as raw_file, open(clean_dpath, "w") as clean_file:
           
           
            for line, text in enumerate(raw_file.readlines()):
                
                # hack use classmethod instead of staticmethod to acess 
                # clean method of this class without make an object of this class.
                text = f'{text}\n'
                clean_file.write(clean(text))
                
                if debug:
                    print("ligne ", line, "netoyée")



def merge_file(path_one:str, path_two:str, source_post:int)->None:
    """ merge file of path_one and path_two into source_post """
    
    path_one = get_abspath(path_one)
    path_two = get_abspath(path_two)
    
    match source_post:
        
        case 1:
            with open(path_one, 'a', encoding="utf-8",
            errors="ignore") as file_one, open(path_two, 'r', encoding="utf-8", 
            errors="ignore") as file_two:
                for line in file_two:
                    print(line, file=file_one, flush=True)
                    
        case _:
            with open(path_one, 'r', encoding="utf-8", 
            errors="ignore") as file_one, open(path_two, 'a', encoding="utf-8", 
            errors="ignore") as file_two:
                for line in file_one:
                    print(line, file=file_twoe, flush=True)            
                

    
def antro_choice(items: list):
    """ 
    chose the max item in items.
    antropic choice or random choice.

    like random.choice but with a undeterministic way by using the sin function.
    """
    stamp = 91511488
    current_time = time.time()
    delta = current_time - stamp
    
    # here you can see the sin function used to 
    # create a undeterministic choice, because the value of delta 
    # is always changing.
    # read the paper : https://fr.wikipedia.org/wiki/Effet_papillon
    # of course the paper is in french but you can use google translate to read it in english.
    keys = str(math.sin(delta) % len(items)).split('.')[1] 
    j = len(keys) - 1
    
    idx = []
    while j != -1:
        i = int(keys[j])
        if i < len(items):
            return items[i]
        j -= 1
    

    
def antro_items(items:list):
    """
    this is why me (Gnabro Israel), 
    I write my own random generator !
    random.choice fuck it :) 
    """
    # the antropics items, you can't compares it 
    # with the first it completed different by the position
    # very useful for the IA.
    antroitems = []
    
    while True:
        item = antro_choice(items)
        
        if not (item in antroitems):
            antroitems.append(item)
            
        if len(antroitems) == len(items):
            return antroitems
            
    # now instead of have items, 
    # put some programs and you'll see that's it 
    # chaotic !
        
     


def get_file(f_name:str, line:int)->int:
    """ 
    get file with name f_name,
    
    """
    path = get_abspath(f_name)
    
    # it create the file if it doesn't exist hack !
    with open(path, "w") as file:
        pass
        
    with open(path, 'r') as file:
        try:
            return file.readlines[line]
        except:
            raise ValueError("The line doesn't exist !")
            
     

def insert(self, item, n, items):
    """ 
    add item, in items at each 2n pos.

    Args:
      item: Any python object that can be add into a list
      items : a collection that have a insert method
      n: a int 
    
    """
    for i in range(len(items)):
      if i % n == 0: items.insert(i, item)

    return tokens


def join_items(items):
  """
     Join items and return a str object.

     Args:
       items: a collections.
  """
  "".join(*[items]) 


def get_lang():
    """ get the language of the system """
    # get the language of the system
    return locale.getlocale()[0][:2]


def encode_string(name:str)->int:
    """ encode the name to integer """
    return [ord(c) for c in name] 



def get_project_stats(folder_path):
    total_size = 0
    file_count = 0
    
    folder_path = get_abspath(folder_path)
    
    # os.walk parcourt l'arborescence complète
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # On vérifie que c'est un fichier réel (pas un lien symbolique)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
                file_count += 1
                
    # Retourne la taille en octets et le nombre de fichiers
    return total_size, file_count

if __name__ == "__main__":
    print(get_lang()) 