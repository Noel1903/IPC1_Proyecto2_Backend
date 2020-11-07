class Funcion:
    def __init__(self,pelicula,estado,hora):
        self.pelicula=pelicula
        self.estado=estado
        self.hora=hora


    def getPelicula(self):
        return self.pelicula
    
    def getEstado(self):
        return self.estado

    def getHora(self):
        return self.hora   

    def setPelicula(self,pelicula):
        self.pelicula=pelicula

    def setEstado(self,estado):
        self.estado=estado

    def setHora(self,hora):
        self.hora=hora
