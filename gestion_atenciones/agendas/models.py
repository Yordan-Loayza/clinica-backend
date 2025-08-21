from django.db import models

# Create your models here.


class Atencion:
    def __init__(self, rut, nombre_paciente, motivo_atencion, fecha, hora):
        self.rut = rut
        self.nombre_paciente = nombre_paciente
        self.motivo_atencion = motivo_atencion
        self.fecha = fecha
        self.hora = hora


class Agenda:
    def __init__(self):
        p1 = Atencion('20820422-k', 'Yordan',
                      'Le dolia la watita', '18-08-2025', 10)
        p2 = Atencion('20780492-4', 'Dayan',
                      'se comio una cachurreta', '17-08-2025', 12)

        self.lista_agenda = [p1, p2]

    def agregar_atencion(self, atencion):
        if (self.buscar_atencion_por_rut(atencion.rut)):
            return {'message': 'paciente ya existe'}

        self.lista_agenda.append(atencion)
        return {'message': 'paciente agregado'}

    def buscar_atencion_por_rut(self, rut):
        for b in self.lista_agenda:
            if b.rut == rut:
                return b
        return None

    def eliminar_atencion(self, rut):
        atencion = self.buscar_atencion_por_rut(rut)
        if atencion is not None:
            self.lista_agenda.remove(atencion)
            return {'message': 'paciente eliminado'}
        return {'errors': 'paciente no encontrado'}

    def modificar_atencion(self, rut, nombre_paciente, motivo_atencion, fecha, hora):
        atencion = self.buscar_atencion_por_rut(rut)
        if atencion is not None:
            atencion.nombre_paciente = nombre_paciente
            atencion.motivo_atencion = motivo_atencion
            atencion.fecha = fecha
            atencion.hora = hora
            return {'message': f'Se actualizo el paciente con el rut {atencion.rut}'}
        return {'errors': 'No se encontro el paciente a editar'}
