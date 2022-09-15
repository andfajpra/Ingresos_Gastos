#Cogemos la apilcacion t le metemos la ruta que queremos. 
#La app la traemos de registros_ig  import app
from registro_ig import app

@app.route("/")
def index():
    return "Servidor funcionando"