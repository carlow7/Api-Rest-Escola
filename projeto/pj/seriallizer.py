

from rest_framework import serializers
from pj.models import Aluno,Curso,Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','name','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source=Curso.descricao)
    periodo = serializers.SerializerMethodField()
    class Meta:
        model= Matricula
        fields = ('curso','periodo')

    def get_periodo(self, obj):
        return obj.get_periodo_display()



