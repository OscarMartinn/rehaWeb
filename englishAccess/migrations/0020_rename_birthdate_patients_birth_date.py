# Generated by Django 3.2.9 on 2022-06-15 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('englishAccess', '0019_auto_20220613_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='birthDate',
            new_name='birth_Date',
        ),
    ]
