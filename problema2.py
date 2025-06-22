
class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.ocupada = False

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            return True
        return False

    def liberar(self):
        self.ocupada = False


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitacion = None

    def reservar_habitacion(self, habitacion):
        if habitacion.reservar():
            self.habitacion = habitacion
            return f"Habitación {habitacion.numero} reservada para {self.nombre}"
        return "No se pudo reservar"
