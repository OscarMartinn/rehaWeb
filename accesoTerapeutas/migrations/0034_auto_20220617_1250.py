# Generated by Django 3.2.9 on 2022-06-17 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesoTerapeutas', '0033_rename_fechanacimiento_pacientes_fecha_nacimiento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ObjetivoTerapeutico',
            new_name='Objetivo_Terapeutico',
        ),
        migrations.RemoveField(
            model_name='ejercicios',
            name='objetivoTerapeutico',
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='objetivo_Terapeutico',
            field=models.ManyToManyField(help_text='Selecciona los objetivos terapéuticos asociados este ejercicio.', to='accesoTerapeutas.Objetivo_Terapeutico', verbose_name='Objetivos Terapéuticos'),
        ),
    ]
