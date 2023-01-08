from abc import ABC,abstractmethod 
class Persona(ABC):
    def __init__(self,nombre,identificacion,numero,correo):
        self.nomb=nombre
        self.id=identificacion
        self.num=numero
        self.corr=correo

    @abstractmethod
    def MostrarPersona(self):
        pass


class Doctor(Persona):
    def __init__(self, nombre, identificacion,  numero, correo,cargo="Doctor"):
        super().__init__(nombre, identificacion,  numero, correo)
        self.car=cargo
    def MostrarPersona(self):
        print("\nNombre: ",self.nomb,"\nCedula: ",self.id,"\nTelefono: ",self.num,"\nCorreo: ",self.corr,"\nCargo: ",self.car)

class Enfermero(Persona):
    def __init__(self, nombre, identificacion, numero, correo,cargo="Enfermero"):
        super().__init__(nombre, identificacion, numero, correo)
        self.car=cargo
    
    def MostrarPersona(self):
       print("\nNombre: ",self.nomb,"\nCedula: ",self.id,"\nTelefono: ",self.num,"\nCorreo: ",self.corr,"\nCargo: ",self.car)

class Paciente(Persona):
    def __init__(self, nombre, identificacion, numero, correo,Paciente="Paciente"):
        super().__init__(nombre, identificacion, numero, correo)
        self.pac=Paciente
    def MostrarPersona(self):
        print("\nNombre: ",self.nomb,"\nCedula: ",self.id,"\nTelefono: ",self.num,"\nCorreo: ",self.corr,"\n",self.pac)


print("---------Personas------------")
Doc= Doctor("Luis","0993781762","093789234","luis@hotmail.com")
Doc.MostrarPersona()
print("-----------------------------")
Enf= Enfermero("Manuel","0934525765","09863452","Manuel@hotmail.com")
Enf.MostrarPersona()
print("-----------------------------")
pac=Paciente("Jose","093443123445","098643234","Jose@hotmail.com")
pac.MostrarPersona()


        
