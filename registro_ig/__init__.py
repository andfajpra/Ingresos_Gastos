#---Levantamos servidoor y para ello primero instalamos Flask

from flask import Flask

#instanciamos  Flask

app=Flask(__name__)

from registro_ig.routes import *