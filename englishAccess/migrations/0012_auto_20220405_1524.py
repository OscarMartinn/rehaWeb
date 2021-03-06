# Generated by Django 3.2.9 on 2022-04-05 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('englishAccess', '0011_auto_20220403_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercices',
            options={'ordering': ['-creado'], 'verbose_name': 'Exercise', 'verbose_name_plural': 'Exercises'},
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='created',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='code',
            new_name='codigo',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='updated',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='diagnostic',
            new_name='diagnostico',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='age',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='extremities',
            new_name='extremidades',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='laterality',
            new_name='lateralidad',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='name',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='therapeuticObjective',
            new_name='objetivoTerapeutico',
        ),
        migrations.RenameField(
            model_name='exercices',
            old_name='position',
            new_name='posicion',
        ),
    ]
