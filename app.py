from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Usuarios import Usuario
from Films import Film
app=Flask(__name__)
CORS(app)
Users=[]
Peliculas=[]
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
        
@app.route('/IniciarSesion/',methods=['POST'])
def Login():
    global Users
    user=request.json['usuario']
    passw=request.json['contraseña']
    for usuarios in Users:
        if usuarios.getUsuario()==user and usuarios.getContraseña()==passw:
            Mensaje={
                'mensaje':'Correcto',
                'usuario': usuarios.getUsuario()
            }
            break
        else:
            Mensaje={
                'mensaje':'Error',
                'usuario':''
            }
    respuesta=jsonify(Mensaje)
    return respuesta      
    

@app.route('/Registrar/',methods=['POST'])
def agregarUser():
    global Users
    nuevo= Usuario(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['contraseña'])
    Users.append(nuevo)
    return("Se agregó el usuario")

@app.route('/CargarPeliculas',methods=['POST'])
def csvPeliculas():
    global Peliculas 
    nuevaP=Film(request.json['titulo'],request.json['url'],request.json['puntuacion'],request.json['duracion'],request.json['sinopsis'])
    Peliculas.append(nuevaP)
    return("se agregaron las peliculas")

if __name__ == "__main__":
    app.run(debug=True,port=3000)