"""Docstring"""
from rest_framework import serializers
from .models import Bibliotecas

class BibliotecasSerializer(serializers.ModelSerializer):
    """Docstring"""
    class Meta:
        """Docstring"""
        model = Bibliotecas
        fields = '__all__'
