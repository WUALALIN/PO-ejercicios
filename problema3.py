
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def inscribirse(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.inscribir_estudiante(self)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inscritos = []

    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.inscritos:
            self.inscritos.append(estudiante)
