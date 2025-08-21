from django.shortcuts import render
from .models import Atencion, Agenda

agenda = Agenda()

# Create your views here.


def home(request):
    return render(request, 'agendas/base.html')


def agenda_list(request):
    context = {'atencion': agenda.lista_agenda}
    return render(request, 'agendas/agenda_list.html', context)


def agenda_form(request):
    return render(request, 'agendas/agenda_form.html')

def agenda_create(request):
    rut = request.POST.get('rut')
    nombre_paciente = request.POST.get('nombre_paciente')
    motivo_atencion = request.POST.get('motivo_atencion')
    fecha = request.POST.get('fecha')
    hora = request.POST.get('hora')

    if rut.strip() == '' or nombre_paciente.strip() == '' or motivo_atencion.strip() == '' or fecha.strip() == '' or hora.strip() == '':
        context = {'errors': 'Campos vacios'}
        return render(request, 'agendas/agenda_create.html', context)

    atencion = Atencion(rut, nombre_paciente,motivo_atencion,fecha, hora)
    context = agenda.add_atencion(atencion)
    print(context)
    return render(request, 'agendas/agenda_create.html', context)

def confirm_delete(request):
    rut = request.POST.get('rut')
    return render(request, 'agendas/agenda_confirm_delete.html', {'rut': rut})

def delete_atencion(request):
    rut = request.POST.get('rut')

    if rut.strip() == "":
        context = {'errors': 'Debe enviar rut'}
        return render(request, 'agendas/atencion_delete.html', context)

    context = agenda.delete_atencion(rut)
    return render(request, 'agendas/atencion_delete.html', context)


def edit_form(request, rut):
    atencion = agenda.search_atencion(rut)
    if atencion is not None:
        return render(request, 'agendas/atencion_edit_form.html', {'atencion': atencion})
    return render(request, 'agendas/atencion_edit_form.html', {'errors': 'No se encontro libro a editar.'})


def edit_atencion(request):
    rut = request.POST.get('rut')
    nombre_paciente = request.POST.get('nombre_paciente')
    motivo_atencion = request.POST.get('motivo_atencion')
    fecha = request.POST.get('fecha')
    hora = request.POST.get('hora')

    if rut.strip() == '' or nombre_paciente.strip() == '' or motivo_atencion.strip() == '' or fecha.strip() == '' or hora.strip() == '':
        context = {'errors': 'Campos vacios'}
        return render(request, 'agendas/atencion_create.html', context)

    context = agenda.update_atencion(rut, nombre_paciente,motivo_atencion,fecha,hora)

    return render(request, 'agendas/atencion_edit.html', context)