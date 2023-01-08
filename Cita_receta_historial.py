class cita:
    def __init__(self,fecha,nombre,telefono):
        self.fec=fecha
        self.nombr=nombre
        self.__tel=telefono
       

    @property
    def telefono(self):
        return self.__tel


    def OptenerDatos(self):
        pass

class HistoriaClinica(cita):
    def __init__(self, fecha, nombre, telefono, enfermedad="No posee enfermedades"):
        super().__init__(fecha, nombre, telefono)
        self.__enf=enfermedad
    @property
    def enfermedad(self):
        self.__enf

    def obtenerDatos(self):
        pass

class Diagnostico(HistoriaClinica):
    def __init__(self, fecha, nombre, telefono, enfermedad="No posee enfermedades", causa="Presenta dolores estomacales"):
        super().__init__(fecha, nombre, telefono, enfermedad)
        self.cas=causa

    def MostrarDiagnostico(self):
        print("\nNombre: ",self.nombr, "\nTelefono: ",self.telefono,"\nCausa: ",self.cas)


class Receta(Diagnostico):
    def __init__(self, fecha, nombre, telefono ,enfermedad="No posee enfermedades", causa="dolor estomacal",medicamento="Buscapina",tratamiento="tomar 1 despues de cada comida",cedula="0932455232"):
        super().__init__(fecha, nombre, telefono, enfermedad, causa)
        self.me=medicamento
        self.tra=tratamiento
        self.__ce=cedula
    @property
    def cedula(self):
        return self.__ce

    def MostrarReceta(self):
        print(print("\nNombre: ",self.nombr, "\nCedula: ",self.cedula,"\nMedicamento: ",self.me,"\nTramiento: ",self.tra))





print("-------------Diagnostico----------------------")
diag=Diagnostico("2/1/2023","Mauro","098434366")
diag.MostrarDiagnostico()

print("------------------Receta---------------------")
rec=Receta("2/1/2023","Mauro","098434366")
rec.MostrarReceta()








