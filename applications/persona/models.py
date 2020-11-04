from django.db import models

from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)


    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del personal'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad



# Create your models here.
class Empleado(models.Model):
    """ Modelo para tabla empleados """


    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField( upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    #Personalización de modelos para vista de administrador
    class Meta:
        verbose_name = 'Mi Personal'
        verbose_name_plural = 'Personal de la empresa'
        ordering = ['-first_name']
        #unique_together = ('name', 'shot_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name