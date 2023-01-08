class Consultorio:
    def __init__(self, nombre="Consultorio medico", numeroTelefono="0983456753", direccion="calle 12 de octubre"):
        self.nomb=nombre
        self.Telf=numeroTelefono
        self.direc=direccion
    def MostrarDatos(self):
        return print("Nombre:",self.nomb,"  Telefono:",self.Telf,"  Direccion:",self.direc)
        
c=Consultorio()
c.MostrarDatos()


