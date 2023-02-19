from difflib import context_diff

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from Login.models import Alumno, Credencial, Solicitud
import Login.models


# Create your views here.
@login_required(redirect_field_name='login_alumnos')
def Panel(request):
    if request.user.is_alumno:
        credencial = Credencial.objects.get(usuario=request.user)
        if credencial != None and credencial.estado_credencial == 'activa':
            context = {
                'credencial': credencial
            }
            return render(request, 'Alumnos/panelAlumno.html', context)
        else:
            context = {
                'info': 'No has realizado niguna solicitud para tu credencial o tu solicitud aun no a sido aceptada.',
                'peticion': 'Puedes realizar una solicitud en el apartado de solicitud o ver el tu solicitud.'
            }
            return render(request, 'Alumnos/panelAlumno.html', context)
    else:
        return render(request, 'Login/home.html')

def Solicitud(request):
    if request.user.is_alumno:
        credencial = Credencial.objects.get(usuario=request.user)
        if credencial != None:
            tipo_solicitud = 'nueva'
            estado_solicitud = 'pendiente'
            alumno = Alumno.objects.get(usuario=request.user)
            solicitud = Solicitud(tipo_solicitud=tipo_solicitud, estado_solicitud=estado_solicitud, alumno=alumno)
            solicitud.save()
            context = {
                'info': 'Tu solicitud ha sido enviada.',
                'tipo_solicitud': tipo_solicitud,
                'estado_solicitud': estado_solicitud
            }
            return render(request, 'Alumnos/solicitud.html', context)
        else:
            tipo_solicitud = 'reposision'
            estado_solicitud = 'pendiente'
            alumno = Alumno.objects.get(usuario=request.user)
            solicitud = Solicitud(tipo_solicitud=tipo_solicitud, estado_solicitud=estado_solicitud, alumno=alumno)
            solicitud.save()
            context = {
                'info': 'Tu solicitud ha sido enviada.',
                'tipo_solicitud': tipo_solicitud,
                'estado_solicitud': estado_solicitud
            }
            return render(request, 'Alumnos/panelAlumno.html', context)
    else:
        return render(request, 'Login/home.html')

