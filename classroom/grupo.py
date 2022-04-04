from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = f'Grado 12'

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
    
    def __str__(self):
        aux = self._grupo
        if aux == "grupo ordinado":
            aux = "grupo predeterminado"
            return "Grupo de estudiantes: "+ aux
        return "Grupo de estudiantes: "+ aux


    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if lista != []:
            self.listadoAlumnos = self.listadoAlumnos + lista + [alumno]
        else:
            self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
