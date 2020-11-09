from flask import Flask,jsonify,request
from flask_cors import CORS
import json
from Usuarios import Usuario
from Films import Film
from Reseñas import Reseña
from Funciones import Funcion
from Asientos import Asiento
import datetime
import pytz
import os
import numpy as np
app=Flask(__name__)
CORS(app)
Users=[]
Peliculas=[]
Reseñas=[]
Funciones=[]
Asientos=[]
Users.append(Usuario('Usuario','Maestro','admin','admin','administrador'))


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
                'usuario': usuarios.getUsuario(),
                'tipo':usuarios.getTipo()

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
    usuario=request.json['usuario']
    for i in range(len(Users)):
        if usuario!=Users[i].getUsuario():
            nuevo= Usuario(request.json['nombre'],request.json['apellido'],request.json['usuario'],request.json['contraseña'],request.json['tipo'])
            Users.append(nuevo)
            mensaje={
                'mensaje':'Correcto'
            }
            respuesta=jsonify(mensaje)
        else:
            mensaje={
                'mensaje':'Error'
            }
            respuesta=jsonify(mensaje)
            break

            
    
    return(respuesta)



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

@app.route('/Modificar',methods=['POST'])
def modificar():
    titulo=request.json['titulo']
    tituloN=request.json['tituloN']
    url=request.json['url']
    puntuacion=request.json['puntuacion']
    duracion=request.json['duracion']
    sinopsis=request.json['sinopsis']
    global Peliculas
    for a in range(len(Peliculas)):
        if titulo==Peliculas[a].getTitulo():
            Peliculas[a].setTitulo(tituloN)
            Peliculas[a].setUrl(url)
            Peliculas[a].setPuntuacion(puntuacion)
            Peliculas[a].setDuracion(duracion)
            Peliculas[a].setSinopsis(sinopsis)
        break
    mensaje={
        'mensaje':'correcto'
    }
    respuesta=jsonify(mensaje)
    return(respuesta)
        
@app.route('/Eliminar/<string:titulo>',methods=['DELETE'])
def eliminar(titulo):
    global Peliculas
    for i in range(len(Peliculas)):
        if titulo==Peliculas[i].getTitulo():
            del Peliculas[i]
            break
    mensaje={
        'mensaje':'correcto'
    }
    respuesta=jsonify(mensaje)
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
                'usuario':usuarios.getUsuario(),
                'contraseña':usuarios.getContraseña()
            }
            break
    respuesta=jsonify(Mensaje)
    return respuesta          

@app.route('/Recuperar',methods=['POST'])
def recuperar():
    global Users
    usuario=request.json['usuario']
    for i in range(len(Users)):
        if usuario==Users[i].getUsuario():
            mensaje={
                'mensaje':'correcto',
                'contraseña':Users[i].getContraseña()
            }
            break
    respuesta=jsonify(mensaje)
    return(respuesta)   

@app.route('/Modificarperfil',methods=['POST'])
def modificarP():
    usuario=request.json['usuario']
    usuarioN=request.json['usuarioN']
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    contraseña=request.json['contraseña']
    global Users
    for i in range(len(Users)):
        if usuario==Users[i].getUsuario():
            for a in range(len(Users)):
                if usuarioN!=Users[a].getUsuario():
                    Users[i].setUsuario(usuarioN)
                    Users[i].setContraseña(contraseña)
                    Users[i].setNombre(nombre)
                    Users[i].setApellido(apellido)
                    mensaje={
                        'mensaje':'correcto'
                    }
                    respuesta=jsonify(mensaje)
                else:
                    mensaje={
                        'mensaje':'Error'
                    }
                    respuesta=jsonify(mensaje)

                break
    return(respuesta)
            

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

@app.route('/Eliminar/<string:titulo>/<string:hora>',methods=['DELETE'])
def eliminarF(titulo,hora):
    global Funciones
    for i in range(len(Funciones)):
        if titulo==Funciones[i].getPelicula() and hora==Funciones[i].getHora():
            del Funciones[i]
            break
    mensaje={
        'mensaje':'correcto'
    }
    respuesta=jsonify(mensaje)
    return(respuesta)

                                         
@app.route('/Asientos',methods=['POST'])
def asientos():
    global Asientos
    nuevoAs=Asiento(request.json['pelicula'],request.json['asiento'],request.json['hora'])
    Asientos.append(nuevoAs)
    return "Aceptado"
   
@app.route('/Asientos/Apartados',methods=['GET'])
def verasientos():
    global Asientos
    asi=[]
    for i in Asientos:
        datos={
            'pelicula':i.getPelicula(),
            'asiento':i.getAsiento(),
            'hora':i.getHora()
        }
        asi.append(datos)
    respuesta=jsonify(asi)
    return(respuesta)
    

if __name__ == "__main__":
    puerto=int(os.environ.get('PORT',3000))
    app.run(host='0.0.0.0',port=puerto)