class Film:
    def __init__(self,titulo,Url,puntuacion,duracion,sinopsis):
        self.titulo=titulo
        self.Url=Url
        self.puntuacion=puntuacion
        self.duracion=duracion
        self.sinopsis=sinopsis

    def getTitulo(self):
        return self.titulo
    
    def getUrl(self):
        return self.Url

    def getPuntuacion(self):
        return self.puntuacion

    def getDuracion(self):
        return self.duracion

    def getSinopsis(self):
        return self.sinopsis    

    def setTitulo(self,titulo):
        self.titulo=titulo

    def setUrl(self,Url):
        self.Url=Url

    def setPuntuacion(self,puntuacion):
        self.puntuacion=puntuacion

    def setDuracion(self,duracion):
        self.duracion=duracion 

    def setSinopsis(self,sinopsis):
        self.sinopsis=sinopsis          