# Generated by Django 3.2.9 on 2021-11-28 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo nivel de clasificación de la movilidad funcional [1-6,C y N]', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Clasificación',
                'verbose_name_plural': 'Clasificaciones',
            },
        ),
        migrations.CreateModel(
            name='Diagnosticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo diagnóstico.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Diagnóstico',
                'verbose_name_plural': 'Diagnósticos',
            },
        ),
        migrations.CreateModel(
            name='Edad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo rango de edad', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Edad',
                'verbose_name_plural': 'Edades',
            },
        ),
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Indique el código del ejercicio.', max_length=8, verbose_name='Código')),
                ('nombre', models.CharField(help_text='Indique un nombre para el nuevo ejercicio.', max_length=60, verbose_name='Nombre del Ejercicio')),
                ('descripcion', models.TextField(blank=True, help_text='Si lo desea, añade una descripción explicativo.', max_length=500, null=True, verbose_name='Descripción')),
                ('video', models.FileField(blank=True, help_text='Seleccione el video que quieres asociar al ejercicio. Con el siguiente formato: codigo_ejercicio.mp4', null=True, upload_to='ejercicios', verbose_name='Video')),
                ('visible', models.BooleanField(default=True, help_text='Cuando quieras dejar oculto un Ejercicio, desmarca la casilla', verbose_name='Sin ocultar')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.ManyToManyField(help_text='Seleccione los diagnósticos asociadosa a este ejercicio.', to='accesoTerapeutas.Diagnosticos', verbose_name='Diagnostico')),
                ('edad', models.ManyToManyField(help_text='Seleccione los rangos de edad para este ejercicio.', to='accesoTerapeutas.Edad', verbose_name='Rangos de Edad')),
            ],
            options={
                'verbose_name': 'Ejercicio',
                'verbose_name_plural': 'Ejercicios',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='EjerciciosRealizados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ejercicio', models.CharField(max_length=80, verbose_name='Ejercicio')),
                ('fecha', models.CharField(max_length=30, verbose_name='Fecha de realización')),
                ('sesion', models.IntegerField(default=0, verbose_name='ID Sesión')),
            ],
            options={
                'verbose_name': 'Ejercicio realizado en la sesion',
                'verbose_name_plural': 'Ejercicios realizados en la sesión',
            },
        ),
        migrations.CreateModel(
            name='Extremidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nombre de una nueva extremidad', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Extremidad',
                'verbose_name_plural': 'Extremidades',
            },
        ),
        migrations.CreateModel(
            name='FormularioPacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=100, verbose_name='Día preferido')),
                ('momento', models.CharField(max_length=30, verbose_name='Momento del día')),
                ('horas', models.CharField(max_length=120, verbose_name='Horario preferido')),
                ('usuario', models.CharField(max_length=30, verbose_name='Usuario')),
                ('idUser', models.IntegerField(default=0, verbose_name='Id Usuario')),
            ],
            options={
                'verbose_name': 'Formulario',
                'verbose_name_plural': 'Formularios',
            },
        ),
        migrations.CreateModel(
            name='Gmfcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo nivel de función motora gruesa.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'GMFCS',
                'verbose_name_plural': 'GMFCS',
            },
        ),
        migrations.CreateModel(
            name='Lateralidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo nombre de lateralidad.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Lateralidad',
                'verbose_name_plural': 'Lateralidad',
            },
        ),
        migrations.CreateModel(
            name='Macs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo nivel de habilidad manual.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'MACS',
                'verbose_name_plural': 'MACS',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoTerapeutico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada un nuevo objetivo terapéutivo.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Indique el nombre completo del paciente.', max_length=80, verbose_name='Nombre')),
                ('apellidos', models.CharField(default='prueba', help_text='Indique los apellidos del paciente.', max_length=60, verbose_name='Apellidos')),
                ('fechaNacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('usuario', models.CharField(help_text='Indique el usuario que desea asignar al paciente.(Longitud mínima 5 caracteres [a-z, 0-9 y guiones bajos]', max_length=30, verbose_name='Usuario del BOT')),
                ('contraseña', models.CharField(help_text='Indique la contraseña que se usará en las funciones del bot.', max_length=15, verbose_name='Contraseña del BOT')),
                ('visible', models.BooleanField(default=True, help_text='Cuando quieras dejar oculto un Paciente, desmarca la casilla', verbose_name='Sin ocultar')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('calificacion5', models.ForeignKey(help_text='Indica la calificacion FMS5 para una distacia de 5 metros', on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_cinco', to='accesoTerapeutas.calificaciones', verbose_name='FMS5 - Clasificación')),
                ('calificacion50', models.ForeignKey(help_text='Indica la calificacion FMS50 para una distacia de 50 metros', on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_cincuenta', to='accesoTerapeutas.calificaciones', verbose_name='FMS50 - Clasificación')),
                ('calificacion500', models.ForeignKey(help_text='Indica la calificacion FMS500 para una distacia de 500 metros', on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_quinientos', to='accesoTerapeutas.calificaciones', verbose_name='FMS500 - Clasificación')),
                ('diagnostico', models.ForeignKey(help_text='Seleccione el diagnostico de este paciente.', on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.diagnosticos', verbose_name='Diagnóstico')),
                ('gmfcs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.gmfcs', verbose_name='GMFCS')),
                ('macs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.macs', verbose_name='MACS')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Pci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada una nuevo pci', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PCI',
                'verbose_name_plural': 'PCI',
            },
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Añada una nueva posición.', max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Posición',
                'verbose_name_plural': 'Posiciones',
            },
        ),
        migrations.CreateModel(
            name='RegistroSesiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaI', models.CharField(max_length=30, verbose_name='Fecha de inicio')),
                ('fechaF', models.CharField(max_length=30, verbose_name='Fecha de finalización')),
                ('sesion', models.IntegerField(default=0, verbose_name='ID Sesión')),
                ('comentario', models.CharField(default='sin comentario', max_length=100, verbose_name='Comentarios')),
            ],
            options={
                'verbose_name': 'Registro de la sesión',
                'verbose_name_plural': 'Registros de la sesión',
            },
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodicidad', models.IntegerField(default=1, help_text='Indique las veces que puede realizar el paciente esta sesión a lo largo de la semana.', verbose_name='Periodicidad')),
                ('fechaInicial', models.DateField(verbose_name='Fecha de Inicio')),
                ('fechaFinal', models.DateField(verbose_name='Fecha de Final')),
                ('visible', models.BooleanField(default=True, help_text='Cuando quieras dejar oculto una Sesión, desmarca la casilla', verbose_name='Sin ocultar')),
                ('enviado', models.BooleanField(default=False, help_text='Si la casilla no se encuentra marcada, las sesion no ha sido programada', verbose_name='Enviado')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sesion',
                'verbose_name_plural': 'Sesiones',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='Terapeutas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(help_text='Indique el nombre de usuario del terapeuta.', max_length=30, verbose_name='Usuario')),
                ('nombre', models.CharField(help_text='Indique el nombre del terapeuta.', max_length=30, verbose_name='Nombre')),
                ('apellidos', models.CharField(default='prueba', help_text='Indique los apellidos del terapeuta.', max_length=20, verbose_name='Apellidos')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Terapeuta',
                'verbose_name_plural': 'Terapeutas',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='ValoracionPacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30, verbose_name='Paciente')),
                ('ejercicio', models.CharField(max_length=30, verbose_name='Momento del día')),
                ('valoracion1', models.IntegerField(help_text='¿Te ha parecido claro el ejercicio? [0 poco claro y 5 muy claro]', verbose_name='Pregunta 1')),
                ('valoracion2', models.IntegerField(help_text='¿Te ha parecido difícil el ejercicio? [0 poco difícil y 5 muy fácil]', verbose_name='Pregunta 2')),
                ('valoracion3', models.IntegerField(help_text='¿Te ha parecido útil el ejercicio para tus objetivos? [0 poco útil y 5 muy útil]', verbose_name='Pregunta 3')),
                ('valoracion4', models.IntegerField(help_text='¿Has sentido algún tipo de dolor? [0 nada y 5 muchísimo]', verbose_name='Pregunta 4')),
                ('valoracion5', models.CharField(help_text='¿Te gustaría repetir el ejercicio en un futuro?', max_length=4, verbose_name='Pregunta 5')),
                ('fecha', models.CharField(max_length=30, verbose_name='Fecha')),
                ('sesion', models.IntegerField(default=0, verbose_name='ID Sesión')),
            ],
            options={
                'verbose_name': 'Valoración de los ejercicios',
                'verbose_name_plural': 'Valoraciones de los ejercicios',
            },
        ),
        migrations.CreateModel(
            name='SesionesEjercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeticiones', models.SmallIntegerField(default=1, verbose_name='Repeticiones')),
                ('ejercicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.ejercicios', verbose_name='Ejercicios')),
                ('sesiones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.sesiones', verbose_name='Sesiones')),
            ],
            options={
                'verbose_name': 'Ejercicio de la sesión',
                'verbose_name_plural': 'Ejercicios de la sesión',
            },
        ),
        migrations.AddField(
            model_name='sesiones',
            name='ejercicios',
            field=models.ManyToManyField(help_text='Seleccione los ejercicios para esta sesión.', through='accesoTerapeutas.SesionesEjercicios', to='accesoTerapeutas.Ejercicios', verbose_name='Ejercicios'),
        ),
        migrations.AddField(
            model_name='sesiones',
            name='paciente',
            field=models.ForeignKey(help_text='Selecciona al paciente asigando para esta sesión.', on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.pacientes', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='sesiones',
            name='terapeuta',
            field=models.ForeignKey(help_text='Seleccione el terapeuta de esta sesión.', on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.terapeutas', verbose_name='Terapeuta'),
        ),
        migrations.AddField(
            model_name='pacientes',
            name='terapeuta',
            field=models.ForeignKey(help_text='Seleccione el terapeuta de este paciente.', on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.terapeutas', verbose_name='Terapeuta'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='extremidades',
            field=models.ManyToManyField(help_text='Seleccione las extremidades involucradas eneste ejercicio.', to='accesoTerapeutas.Extremidades', verbose_name='Extremidades'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='lateralidad',
            field=models.ForeignKey(help_text='Seleccione la lateralidad de este ejercicio.', on_delete=django.db.models.deletion.CASCADE, to='accesoTerapeutas.lateralidad', verbose_name='Lateralidad'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='objetivoTerapeutico',
            field=models.ManyToManyField(help_text='Selecciona los objetivos terapéuticos asociados este ejercicio.', to='accesoTerapeutas.ObjetivoTerapeutico', verbose_name='Objetivos Terapéuticos'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='pci',
            field=models.ManyToManyField(to='accesoTerapeutas.Pci', verbose_name='PCI'),
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='posicion',
            field=models.ManyToManyField(help_text='Seleccione la posicion asociada a este ejercicio.', to='accesoTerapeutas.Posicion', verbose_name='Posición'),
        ),
    ]
