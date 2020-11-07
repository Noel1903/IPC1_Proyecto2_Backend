class Reseña:
    def __init__(self,titulo,usuario,reseña):
        self.titulo=titulo
        self.usuario=usuario
        self.reseña=reseña


    def getTitulo(self):
        return self.titulo
    
    def getUsuario(self):
        return self.usuario

    def getReseña(self):
        return self.reseña


    def setTitulo(self,titulo):
        self.titulo=titulo

    def setUsuario(self,usuario):
        self.usuario=usuario

    def setReseña(self,reseña):
        self.reseña=reseña
