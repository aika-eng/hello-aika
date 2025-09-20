from flask import Flask #Importa somente o modulo flask da biblioteca

app = Flask(__name__) #app é uma variavel que inicia nossa aplicação 

from routes import *

if __name__ == "__main__":
    app.run(debug=True)







