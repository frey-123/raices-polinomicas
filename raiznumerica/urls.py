from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # Añadir esta línea
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calculadora.urls')),
]
