# Generated by Django 3.2.9 on 2022-04-02 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accesoTerapeutas', '0021_terapeutas_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='terapeutas',
            old_name='user',
            new_name='usuario',
        ),
    ]