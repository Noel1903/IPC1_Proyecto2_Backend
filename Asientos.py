class Asiento:
    def __init__(self,pelicula,asiento,hora):
        self.pelicula=pelicula
        self.asiento=asiento
        self.hora=hora


    def getPelicula(self):
        return self.pelicula
    
    def getAsiento(self):
        return self.asiento

    def getHora(self):
        return self.hora   

    def setPelicula(self,pelicula):
        self.pelicula=pelicula

    def setAsiento(self,asiento):
        self.asiento=asiento

    def setHora(self,hora):
        self.hora=hora
