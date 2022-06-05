# Generated by Django 3.2.9 on 2022-04-03 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accesoTerapeutas', '0026_alter_terapeutas_apellidos'),
        ('englishAccess', '0007_rename_name_diagnostics_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sessions',
            options={'ordering': ['-creado'], 'verbose_name': 'Session', 'verbose_name_plural': 'Sessions'},
        ),
        migrations.RenameField(
            model_name='patientform',
            old_name='date',
            new_name='dia',
        ),
        migrations.RenameField(
            model_name='patientform',
            old_name='hours',
            new_name='horas',
        ),
        migrations.RenameField(
            model_name='patientform',
            old_name='moment',
            new_name='momento',
        ),
        migrations.RenameField(
            model_name='patientform',
            old_name='patient',
            new_name='paciente',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='created',
            new_name='actualizado',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='updated',
            new_name='creado',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='exercises',
            new_name='ejercicios',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='sended',
            new_name='enviado',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='finalDate',
            new_name='fechaFinal',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='initialDate',
            new_name='fechaInicial',
        ),
        migrations.RenameField(
            model_name='sessions',
            old_name='patient',
            new_name='paciente',
        ),
        migrations.RenameField(
            model_name='sessionsexercices',
            old_name='exercices',
            new_name='ejercicios',
        ),
        migrations.RenameField(
            model_name='sessionsexercices',
            old_name='reps',
            new_name='repeticiones',
        ),
        migrations.RenameField(
            model_name='sessionsexercices',
            old_name='sessions',
            new_name='sesiones',
        ),
        migrations.RemoveField(
            model_name='sessions',
            name='therapist',
        ),
        migrations.AddField(
            model_name='sessions',
            name='terapeuta',
            field=models.ForeignKey(blank=True, help_text='Seleccione el terapeuta de esta sesión.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.terapeutas', verbose_name='Terapeuta'),
        ),
    ]