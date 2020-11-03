from django.contrib import admin
from django.urls import path

def DesdeApp(self):
    print('==============Chupame un webo=====================')

urlpatterns = [
    path('departamento/', DesdeApp),
]
