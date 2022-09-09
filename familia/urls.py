from django.contrib import admin
from django.urls import path, include
from familia.views import listar_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_familia),
]
