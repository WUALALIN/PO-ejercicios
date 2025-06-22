
class Examen:
    def __init__(self, tema, nota):
        if 1.0 <= nota <= 7.0:
            self.tema = tema
            self.nota = nota
        else:
            raise ValueError("La nota debe estar entre 1.0 y 7.0")


class EstudianteEvaluado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.examenes = []

    def agregar_examen(self, examen):
        self.examenes.append(examen)

    def calcular_promedio(self):
        if not self.examenes:
            return 0
        return sum(e.nota for e in self.examenes) / len(self.examenes)

    def mostrar_examenes(self):
        for e in self.examenes:
            print(f"{e.tema}: {e.nota}")
