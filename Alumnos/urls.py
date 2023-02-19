from django.urls import path
from . import views


urlpatterns = [
    path('panel/', views.Panel, name='panel_alumnos'),
]
