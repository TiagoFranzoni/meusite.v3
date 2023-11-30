"""Docstring"""
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('bibliotecas_python.urls', 'bibliotecas'), namespace='bibliotecas')),
    path('logout/', auth_views.LogoutView.as_view(next_page='bibliotecas:biblioteca-home'), name='logout'),

    path('api/', include(('bibliotecas_python.urls', 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
