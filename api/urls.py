from django.urls import path
from .views import index, get_chart, dashboard, actualizar_datos

urlpatterns = [
    path('', index, name='index'),
    path('get_chart/', get_chart, name='get_chart'),
    path('dashboard/', dashboard, name='dashboard'),
    path('actualizar_datos/', actualizar_datos, name='actualizar_datos')
]