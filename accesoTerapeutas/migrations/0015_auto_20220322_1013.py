# Generated by Django 3.2.9 on 2022-03-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accesoTerapeutas', '0014_diagnosticos_english_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ejercicios',
            name='english_description',
            field=models.TextField(blank=True, help_text='If you wish, add an explanatory description.', max_length=500, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='english_name',
            field=models.CharField(blank=True, help_text='Set the name of the new exercise.', max_length=40, null=True),
        ),
    ]
