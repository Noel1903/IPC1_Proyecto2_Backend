from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Usuarios import Usuario
from Films import Film
from Reseñas import Reseña
from Funciones import Funcion
import datetime
import pytz
app=Flask(__name__)
CORS(app)
Users=[]
Peliculas=[]
Reseñas=[]
Funciones=[]
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

@app.route('/CargarPeliculas/',methods=['POST'])
def csvPeliculas():
    global Peliculas 
    nuevaP=Film(request.json['titulo'],request.json['url'],request.json['puntuacion'],request.json['duracion'],request.json['sinopsis'])
    Peliculas.append(nuevaP)
    mensaje={
        'mensaje':'Aceptado'
    }
    respuesta=jsonify(mensaje)
    return respuesta

@app.route('/TablaPeliculas/',methods=['GET'])
def TablaPelis():
    global Peliculas
    pelis=[]
    for p in Peliculas:
        film={
            'titulo':p.getTitulo(),
            'url':p.getUrl(),
            'puntuacion':p.getPuntuacion(),
            'duracion':p.getDuracion(),
            'sinopsis':p.getSinopsis()
        }
        pelis.append(film)
    respuesta=jsonify(pelis)
    return(respuesta)

@app.route('/Cartelera/',methods=['GET'])
def cartelera():
    carteles=[]
    global Peliculas
    for pel in Peliculas:
        cartel={
            'titulo':pel.getTitulo(),
            'url_img':pel.getUrl()
        }
        carteles.append(cartel)
    respuesta=jsonify(carteles)
    return (respuesta)

@app.route('/Cartelera/Ver',methods=['POST'])
def mostrarpeli():
    global Peliculas
    titulo=request.json['titulo']
    for pelis in Peliculas:
        if pelis.getTitulo()==titulo:
            Mensaje={
                'titulo': pelis.getTitulo(),
                'url':pelis.getUrl(),
                'puntuacion':pelis.getPuntuacion(),
                'duracion':pelis.getDuracion(),
                'sinopsis':pelis.getSinopsis()
            }
            break
    respuesta=jsonify(Mensaje)
    return(respuesta)

@app.route('/verUsuario',methods=['POST'])
def verUser():
    global Users
    user=request.json['usuario']
    for usuarios in Users:
        if usuarios.getUsuario()==user:
            Mensaje={
                'nombre':usuarios.getNombre(),
                'apellido': usuarios.getApellido(),
                'usuario':usuarios.getUsuario()
            }
            break
    respuesta=jsonify(Mensaje)
    return respuesta          

@app.route('/Reseñas',methods=['POST'])
def reseñas():
    global Reseñas
    nuevaR=Reseña(request.json['titulo'],request.json['usuario'],request.json['reseña'])
    Reseñas.append(nuevaR)
    return ("Reseña creada")

@app.route('/Reseñas/Ver',methods=['GET'])
def devolverReseñas():
    global Reseñas
    comentarios=[]
    for rese in Reseñas:
        datos={
            'titulo':rese.getTitulo(),
            'usuario':rese.getUsuario(),
            'reseña':rese.getReseña()
        }
        comentarios.append(datos)
    respuesta=jsonify(comentarios)
    return(respuesta)

@app.route('/Funciones',methods=['POST'])
def cargarFunciones():
    pelicula=request.json['titulo']
    horariofuncion=request.json['hora']
    disponible=True
    global Peliculas
    for a in Peliculas:
        if pelicula==a.getTitulo():
            timezone=pytz.timezone('America/Guatemala')
            fecha_completa=datetime.datetime.now(tz=timezone)
            hora=fecha_completa.strftime("%H")
            minutos=fecha_completa.strftime("%M")
            hora_actual=int(hora)
            min_actual=int(minutos)
            tiempofuncion=horariofuncion.split(":")
            hora_funcion=int(tiempofuncion[0])
            minutos_funcion=int(tiempofuncion[1])
            if hora_funcion<=hora_actual and minutos_funcion<min_actual:
                disponible=False
            datos={
                'mensaje':'Correcto',
                'estado':disponible
            }    
        
    respuesta=jsonify(datos)
    global Funciones
    nuevaF=Funcion(pelicula,disponible,horariofuncion)
    Funciones.append(nuevaF)
   
    return(respuesta)    
    
@app.route('/Funciones/Ver',methods=['GET'])
def verFunciones():
    global Funciones
    func=[]
    for a in Funciones:
        datos={
            'pelicula':a.getPelicula(),
            'estado':a.getEstado(),
            'hora':a.getHora()
        }
        func.append(datos)
    respuesta=jsonify(func)
    return(respuesta)
                                         

if __name__ == "__main__":
    app.run(debug=True,port=3000)