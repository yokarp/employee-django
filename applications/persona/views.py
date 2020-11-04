from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
# Models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name: 'persona/empleado_list.html'
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'lista'


class ListByAreaEmpleado(ListView):
    """ Lista empleados de una area"""
    template_name = "persona/list_by_area.html"
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista =  Empleado.objects.filter(
            departamento__shot_name=area
        )
        return lista
    context_object_name = 'lista'

class ListEmpleadosByKword(ListView):
    """ Lista de empleados palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    """Lista dehabilidades"""
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=2)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
