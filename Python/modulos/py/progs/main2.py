from sys import path
import os 

path.append(os.path.join(os.path.dirname(__file__),'..\\packages'))
#path.append('C:\\Users\Juanito\Documents\GitHub\Sistema_Gestion\Python\modulos\py\packages\extra')
print(path)

import extra.iota
print(extra.iota.FunI())
