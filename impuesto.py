from abc import ABC, abstractmethod
from datetime import date


class Persona(ABC):
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
    @abstractmethod
    def mostrar():
        pass

class Contribuyente(Persona):
    def __init__(self, id, nombre, email):
        super().__init__(id, nombre)
        self.email = email
    def mostrar(self):
        return f"{self.email}"
class Local:
    def __init__(self, id, descripcion, contribuyente):
        self.id = id
        self.descripcion = descripcion
        self.contribuyente = contribuyente 
    def mostrar(self):
        return f"{self.id} {self.descripcion} {self.contribuyente.nombre}"

class DetalleImpuesto:
    def __init__(self, id, anio, total):
        self.id = id
        self.anio = anio
        self.total = total
    def mostrar(self):
        return f"{self.id} {self.anio} {self.total}"

class CabeceraImpuesto:
    def __init__(self, id, nombreMiembro,  total, local):
        self.id = id
        self.nombreMiembro = nombreMiembro
        self.fecha = date.today()
        self.total = total
        self.local = local
        self.detalle = [] 
    def addDetalle(self, id, anio, total):
        detalle = DetalleImpuesto(id, anio, total) 
        self.detalle.append(detalle)
    def mostrar(self):
        print(f"Codigo: {self.id}     Miembro: {self.nombreMiembro}")
        print(f"Fecha: {self.fecha}  Local: {self.local.descripcion}    Total: {self.total}")
        print("="*10,"Detalles","="*10)
        print("Codigo   Año      Total")
        for det in self.detalle:
            print("{:5}   {:10} {}".format(det.id, det.anio, det.total))


contr = Contribuyente(1,"Hola","DJSK")
local = Local(1, "Nuevo Local",contr)
cab = CabeceraImpuesto(1,"Adriana Mora", "450.5",local)
cab.addDetalle(1,"2023","5000")
cab.addDetalle(2,"2024","5000")
cab.mostrar()
