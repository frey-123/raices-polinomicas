from django.contrib import admin
from django.urls import path
from calculadora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.calcular_raiz, name='calcular_raiz'),  # ← esta línea es clave
    path('generar-pdf/', views.generar_pdf, name='generar_pdf'),
]
