from django.contrib import admin
from django.urls import path

def DesdeApp(self):
    print('==============Chupame un webote=====================')

urlpatterns = [
    path('persona/', DesdeApp),
]
