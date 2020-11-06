from django.shortcuts import render
from django.views.generic.edit import FormView

from applications.persona.models import Empleado
from .models import Departamento

from .forms import NewDepartamentoForm

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('**********Estamos ready********')
        #
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shot_name=form.cleaned_data['shorname']
        )
        depa.save()

        name = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
             first_name=name,
             last_name=apellido,
             job='1',
             departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)