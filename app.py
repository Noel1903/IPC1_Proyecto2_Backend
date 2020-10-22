from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Usuarios import Usuario
app=Flask(__name__)
CORS(app)
Users=[]
Users.append(Usuario('Usuario','Maestro','admin','admin'))


@app.route('/Obtener',methods=['GET'])
def obtenerUsers():
    global Users
    datos=[]
    for user in Users:
        dato={
            'nombre': user.getNombre(),
            'apellido':user.getApellido(),
            'usuario':user.getUsuario(),
            'contraseña':user.getContraseña()
        }
        datos.append(dato)
    respuesta=jsonify(datos)
    return(respuesta)
        
    
     
 

@app.route('/Registrar/',methods=['POST'])
def agregarUser():
    global Users
    nuevo= Usuario(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['contraseña'])
    Users.append(nuevo)
    return("Se agregó el usuario")

if __name__ == "__main__":
    app.run(debug=True,port=3000)