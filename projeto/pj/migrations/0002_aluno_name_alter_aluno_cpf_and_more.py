# Generated by Django 4.0.6 on 2022-07-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='name',
            field=models.CharField(max_length=30, null=b'I00\n'),
            preserve_default=b'I00\n',
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='data_nascimento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=11),
        ),
    ]
