from pickle import FALSE
from pyexpat import model
from django.db import models


class Aluno(models.Model):
    name = models.CharField(max_length=30 , null=FALSE)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    def __str__(self):
        return self.name
        

class Curso(models.Model):
    NIVEL = (
        ('B' , 'Basico'),
        ('I' , 'Intermediario'),
        ('A',  'Avançado'),
    )
    codigo_curso = models.CharField(max_length=20)
    descricao = models.CharField(max_length=20)
    nivel = models.CharField(max_length=1 , choices=NIVEL , blank=False,null=False,default='B')

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    PERIODO = (
        ('M' , 'Matutino'),
        ('V', 'Vespertino'),
        ('N', "Noturno")
    )
    aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    periodo = models.CharField(max_length=1,choices=PERIODO,blank=False,null=False,default='M')

    def __str__(self):
        return self.aluno


# Create your models here.
